---
title: How to Install Mods
author: Goosifer
draft: false
date: 2024-10-01T00:00:00+00:00
---

# How to Install Mods

# Important

## Turn off the game

Though it shouldn't cause any issues if we were to install a mod while your game is running, it makes sense to have it shut down so that any changes show up on a re-launch.

## Unzip your files

All files on ZooBerry are in `.zip` format and will require access to a zip utility. Below are resources that can get you started.

1. [Zipping/Unzipping files with the default Windows zip utility](https://support.microsoft.com/en-us/windows/zip-and-unzip-files-f6dde0a7-0fec-8294-e1d3-703ed85e7ebc)
2. Zipping/Unzipping files with 7-Zip
    1. [Download 7-Zip](https://www.7-zip.org/download.html)
    2. [How to use 7-Zip](https://7ziphelp.com/how-to-use-7-zip)


# Zoo Tycoon 1

Depending on the version of Zoo Tycoon 1 you own, the mod install directory might be different. The type of file you want to install might be important as well. Try these out and see which works for you.


## Installing ZT1 Mods

When you unzip your zip file, you will find a `.ztd` file. This is the Zoo Tycoon 1 mod file format which contains all of the cool artsy and codey stuff that makes your game more fun. Drop it into one of the following directories.

First, go to the ZT1 root folder.

`C:\Program Files (x86)\Microsoft Games\Zoo Tycoon\`

If you have a `dlupdate` folder, drop your `.ztd` file there:

`C:\Program Files (x86)\Microsoft Games\Zoo Tycoon\dlupdate`

If you do not have a `dlupdate` folder, drop your `.ztd` file into the `Updates` folder instead:

`C:\Program Files (x86)\Microsoft Games\Zoo Tycoon\Updates`

The install directory changes depending on the version of the game you own but these instructions should be consistent.

## Lang Files

Importantly, Zoo Tycoon 1 mods will often add new strings that show up on the UI, things like guest thoughts, zoopedia entries, and other additions that require the inclusion of a `.dll` file in your installation process. This `.dll` file serves as a serialized data container with most of the strings in the game. Community nomenclature has dubbed these files 'lang files' because they are always prefixed by the 'lang' identifier. Also because they are language files.

If your mod requires a lang file, simply download the referenced version of the lang in the mod instruction blurb, extract the `.dll` file from the zip file (if there is one), and drop it into the root Zoo Tycoon game directory:

`C:\Program Files (x86)\Microsoft Games\Zoo Tycoon\`

> Note: Not all ZT1 mods make use of lang files. 

# Zoo Tycoon 2

## Method 1

Method 1 is the easiest way to install mods and amounts to a simple drag and drop. If your .zip bundle contains folders and something with a .dl extension, simply discard everything and keep the .z2f file. Place your extracted `.z2f` files in here:

`C:/Program Files (x86)/Microsoft Games/Zoo Tycoon 2`

## Method 2

Many legacy mods from ZooMania and the Zoo Tycoon 2 Design Centre contain `.dl` files alongside the main mod files. These files were usually included because they credited the mod author and allowed for the mod to appear as a 'download' within Zoo Tycoon 2. This section is a bit more involved, but is still worth understanding if you wish to have the original mods set up the way they were originally meant to be seen. It is also a great method because it allows to organize your mods a bit more within subdirectories. See ahead for details.

Please note that this does require displaying hidden files on Windows, so if this is a non-negotiable option to you, feel free to stick to the above install method.

### Step 1

Folders are hidden on Windows by default. We need to make them visible to see the install directory.

**To display hidden files and folders on Windows XP, Windows 7**

- Open Folder Options in Control Panel.
- Click Start, and then click Control Panel.
- Click Appearance and Themes, and then click Folder Options.
- On the View tab, under Hidden files and folders, click Show hidden files and folders.

**To display hidden files and folders on modern Windows systems**

- Open a File Explorer window
- In the submenu up top, click on `View` > `Show` > `Hidden Items`

### Step 2

Drop your `.dl` files inside of the following directory:

`C:\Documents and Settings\All Users\Application Data\Microsoft Games\Zoo Tycoon 2\downloads\zootycoon_com_zt2_1033`

This directory should already be populated if you have official DLC installed.

### Step 3

Drop your `.z2f` files into any one of the folders denoted by a four-digit number.

# Questions?

ZooBerry doesn't have a discussion community of its own. Join our [Discord](https://discord.gg/g5FvNrRQGC).

You can also visit the [Other Websites](/knowledgebase/zooberry/community/other-websites) page for other Zoo Tycoon websites that can help with installation problems or shoot me an email if you would like to report a bug.