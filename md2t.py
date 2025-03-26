import zipfile
import os
import sys
import argparse
import yaml
import tomlkit as toml
from tomlkit import array, inline_table
import io
import re
import chardet
from slugify import slugify
import tempfile
import shutil

# Adds a TOML metadata file to each ZTD file in a ZIP archive given a directory with a markdown file and a ZIP file

# CLI entry point
parser = argparse.ArgumentParser(description="Convert from Markdown to TOML")
parser.add_argument("directory", help="Directory to process")
parser.add_argument("-o", "--output", help="Output directory", default=".")
args = parser.parse_args()

mods_with_deps = []
mods_with_toml = []
processed_count = 0

def detect_encoding(file_path):
    """Detect file encoding."""
    with open(file_path, "rb") as f:
        raw_data = f.read(1024)  # Read first 1KB for detection
        result = chardet.detect(raw_data)
        return result["encoding"]

def process_zip_directory(zip_path, ztd_file_list, num_ztd_files_rem):
    """Find all .ztd files inside a ZIP archive."""
    with zipfile.ZipFile(zip_path, 'r') as z:
        for zip_info in z.infolist():
            if zip_info.filename.endswith('.ztd'):
                ztd_file_list.append(zip_info.filename)  # Store filenames, not bytes
                num_ztd_files_rem -= 1
                if num_ztd_files_rem == 0:
                    break

def extract_yaml_from_markdown(md_file_path):
    """Extract only the YAML front matter from a Hugo markdown file, handling encoding issues."""
    encoding = detect_encoding(md_file_path)
    try:
        with open(md_file_path, "r", encoding=encoding) as f:
            content = f.read()
    except UnicodeDecodeError:
        print(f"Warning: Could not decode {md_file_path} with {encoding}. Trying 'latin-1'.")
        with open(md_file_path, "r", encoding="latin-1") as f:
            content = f.read()

    # Match YAML front matter (first block enclosed by ---)
    match = re.match(r"---\n(.*?)\n---", content, re.DOTALL)

    if match:
        yaml_content = match.group(1)  # Extract YAML part
        try:
            return yaml.safe_load(yaml_content)
        except yaml.YAMLError as e:
            print(f"Error parsing YAML in {md_file_path}: {e}")
            return None
    else:
        print(f"Warning: No YAML front matter found in {md_file_path}")
        return None
    
def get_url(deps):
    """Extract URL from dependency list."""
    if deps.get("external", False) is False:
        link = deps.get("url", "")
        prefix = "https://www.zooberry.org"
        return prefix + link
    else:
        return deps.get("url", "")
    
def replace_ztd_file_in_zip(zip_path, ztd_filename, new_ztd_data):
    # Create temporary file for the new zip
    tmp_fd, tmp_zip_path = tempfile.mkstemp(suffix=".zip")
    os.close(tmp_fd)

    with zipfile.ZipFile(zip_path, 'r') as zin, zipfile.ZipFile(tmp_zip_path, 'w') as zout:
        # Copy all files except the one to replace
        for item in zin.infolist():
            if item.filename != ztd_filename:
                zout.writestr(item, zin.read(item.filename))

        # Add the updated ZTD file
        zout.writestr(ztd_filename, new_ztd_data)

    # Replace the original ZIP file with the updated one
    shutil.move(tmp_zip_path, zip_path)

# Process the directory
for root, dirs, files in os.walk(args.directory):
    zip_name = None
    md_name = None

    for file in files:
        if file.endswith(".zip"):
            zip_name = file
        elif file == "index.md":
            md_name = file
        
        if zip_name and md_name:
            break

    if zip_name and md_name:
        print(f"Found {zip_name} and {md_name} in {root}")
    else:
        continue
        
    if zip_name and md_name:
        # get zip directory without filename
        zip_dir = os.path.splitext(zip_name)[0]
        
        try:
            with open(os.path.join(root, file), "r") as f:
                data = extract_yaml_from_markdown(os.path.join(root, md_name))
        except yaml.YAMLError as e:
            print(f"Error parsing YAML in {file}: {e}")
            continue

        mod_list = data.get("mod_list", [])
        mod_dict = {mod["name"]: mod for mod in mod_list if "name" in mod}
        num_ztd_files_rem = len(mod_list) if mod_list else 1
        ztd_file_list = []

        process_zip_directory(os.path.join(root, zip_name), ztd_file_list, num_ztd_files_rem)

        for ztd_file in ztd_file_list:
            # Read the ZTD file from the ZIP and modify it in-memory
            with zipfile.ZipFile(os.path.join(root, zip_name), "r") as parent_zip:
                with parent_zip.open(ztd_file) as ztd_content:
                    ztd_data = io.BytesIO(ztd_content.read())

                    with zipfile.ZipFile(ztd_data, "a") as ztd_zip:
                        if "meta.toml" in ztd_zip.namelist():
                            print(f"meta.toml already exists in {ztd_file}. Skipping.")
                            mods_with_toml.append(ztd_file)
                            continue

                        # Extract metadata
                        ztd_file_no_ext = os.path.splitext(ztd_file)[0]
                        if ztd_file_no_ext in mod_dict:
                            title = mod_dict[ztd_file_no_ext].get("title", data.get("title", "Unknown Mod"))
                            description = mod_dict[ztd_file_no_ext].get("description", data.get("summary", "No description"))
                        else:
                            # If ztd_file_no_ext is not found in mod_list, use general data
                            title = data.get("title", "Unknown Mod")
                            description = data.get("summary", "No description")
                        authors = data.get("author", [])
                        tags = data.get("zt1tags", [])
                        mod_id = slugify(authors[0]) + "." + slugify(title)
                        
                        # Process dependencies
                        dependencies = array()
                        # dependencies = [
                        #     {
                        #         "name": dep.get("title", "Unknown"),
                        #         "mod_id": "",
                        #         "min_version": "1.0.0",
                        #         "optional": False,
                        #         "ordering": "before",
                        #         "link": get_url(dep),
                        #     }
                        #     for dep in data.get("dependencies", [])
                        # ]

                        for dep in data.get("dependencies", []):
                            entry = inline_table()
                            entry["name"] = dep.get("title", "Unknown")
                            entry["mod_id"] = ""
                            entry["min_version"] = "1.0.0"
                            entry["optional"] = False
                            entry["ordering"] = "before"
                            entry["link"] = get_url(dep)
                            dependencies.append(entry)

                        if dependencies:
                            mods_with_deps.append(mod_id)

                        # Write TOML metadata
                        toml_data = {
                            "name": title,
                            "description": description,
                            "authors": authors,
                            "mod_id": mod_id,
                            "version": "1.0.0",
                            "tags": tags,
                        }
                        # If dependencies exist store as flat array
                        if dependencies:
                            toml_data["dependencies"] = dependencies 
                            mods_with_deps.append(mod_id)
                        else:
                            toml_data["dependencies"] = []

                        # write tomlkit to string then write to ztd_zip
                        toml_str = toml.dumps(toml_data)
                        ztd_zip.writestr("meta.toml", toml_str)

                        # 

                    # Write back modified ZTD to parent ZIP in zip directory
                    replace_ztd_file_in_zip(os.path.join(root, zip_name), ztd_file, ztd_data.getvalue())

                    processed_count += 1
        print(f"Processed {zip_name} at {root}")

print(f"Processed {processed_count} files.")
print(f"Mods with dependencies: {mods_with_deps}")
print(f"Mods with TOML: {mods_with_toml}")