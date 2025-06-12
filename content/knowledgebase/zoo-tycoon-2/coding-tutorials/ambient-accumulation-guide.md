---
title: Ambient Accumulation Guide
draft: false
date: 2007-07-10T02:35:00+0700
author: Penguinman
---

# Ambient Accumulation Guide

In this tutorial you will be creating ambient animals, but you MUST create it based off an existing ambient animal. Now is the time to figure that out and from now on it will be referred to as the base animal. Also, you should know that the 2 folders contained in the download called entities and world will be referred to as your files.

## Section I: Gathering the Files

The first thing you must do is get the files that you will be editing. To do this, you will need some sort of extracting program such as WinRAR or WinZIP. Go to the Zoo Tycoon Folder which is most likely located in `C:Program Files/Microsoft Games/Zoo Tycoon 2`. Now, there are 2 files to get.

### File 1: The ai file

- If you have ES: You will need to open `x100_000.z2f` with an extracting program and go to `entities/units/animals/ai` and find the xml file that matches the ambient you are basing it off of. For instance `DuckMallard` or `Bullfrog` and then copy and paste that into the corresponding location in your files.
- If you have AA but do NOT have ES: Follow above rules but with the `x101_000.z2f` file.
- If you have no expansions: Follow above with `entities.z2f` file.

### File 2: The model files

- If you are basing it off a normal ZT2 ambient: Go to `entities.z2f` and then go to `entities/units/animals`. Then find and go into the folder with the codename of the base animal. Now select 2 files, the `.bfm`, `.nif` and `.dds` files. Copy and paste them into your files in `entities/units/animals/codename`
- If you are basing it off an ES ambient: Go to `x100_000.z2f` and follow above rules.

Now you have all the files you need and it is time to think of a codename. It must be the same length as the base animal's. For instance, if I was making a blue duck, and I was basing it off of the `DuckMallard`, I would make my codename `DuckBlueblu`. That way it is the same length.

## Section 2: Coding the Entities Folder

In this section you will be coding everything that is in the `entities` folder. Remember your codename and I often have it copied so I can paste it whenever I need to.

### Part 1: The AI File

Start by going in your files to `entities/units/animals/ai`. In there should be the xml file that you got in section 1. Now you will need to rename that to your codename. Then right click on it, say **Open With** then select **Choose Program** and find notepad. Once it is open in notepad, go to **Edit > Replace**. Then a little box will pop up with 2 blank areas for text. In the first one after Find What: Enter in the base animal's codename. In the part after **Replace With**: enter your codename. Then hit **Replace All**. After it finishes go to **File > Save**. Then you can close that window.

### Part 2: The codename Folder

Start by renaming the codename folder to your codename. Then open it and there should be three files. Rename them so you replace the old codename with your codename in the name. For instance with the blue duck I would have these three files: `DuckBlueblu_Adult_F.dds`, `DuckBlueblu_Adult_F.bfm` and `DuckBlueblu_Adult_F.nif`

The .BFM file: Open the .BFM file in notepad by following the instructions in Part 1 for the ai file. Once it is in notepad, you will have to edit two lines. They are the first line and the line beginning with `<Graph name`. For instance with the blue duck I would edit the first line:

```xml
<BFM modelname="entities\units\animals\DuckMallard\DuckMallard_Adult_F.nif">
```

And make it become:
    
```xml
<BFM modelname="entities\units\animals\DuckBlueblu\DuckBlueblu_Adult_F.nif">
```

And I would edit this line:

```xml
<Graph name="DuckMallard_Adult_F" version="1">
```

And it would become:

```xml
<Graph name="DuckBlueblu_Adult_F" version="1">
```

Do not edit any other lines. After you edit those 2 lines save and close the window.

### The .NIF File

For this you will need a hex editor. If you don't already have one, you can get one from this site called XVI32: http://www.chmaas.handshake.de/delphi/f ... /xvi32.htm

Now open the .NIF in the hex editor. You will be editing things in the left section only. The way it works is that when you type it will override the existing text. Begin by going to **Search > Find** in XVI32 or whatever it may be in your hex editor. Then enter .dds and see where it brings you. It will be the name of the old .dds file, for instance `DuckMallard_Adult_F.dds`. So, begin by clicking on the first letter of the name. In my example it would be the first `D`. Then, just type your codename so that it overrides the original. Then save and close.

The .DDS File: This is the skin to be recolored. If you do not know how to recolor, I recommend using the guide I made here: http://z14.invisionfree.com/ZT2_Designi ... wtopic=152

## Section 3: The world Folder

### The biome folder

Go to `world/ambients` and you will see a folder called `biome`. First, decide how many biomes your ambient will be allowed to go in, and then copy and paste the biome folder until you have an equal number of folders as biomes that you want it to be allowed in. For instance if you want it to be in 4 biomes you will end up with 4 folders most likely named:
`biome`, `Copy of biome`, `Copy (2) of biome`, `Copy (3) of biome`

Then you will need to rename each of these folders to one of the biomes that you want it to be. So, pick the biomes from the list and rename the folders accordingly. It is OK to have only one folder and one biome if that is what you want, or you can have all 10.

Here are the names you can rename the folders to:

- `alpine`
- `borealforest`
- `desert`
- `grassland`
- `savannah`
- `scrub`
- `temperateforest`
- `tropicalrainforest`
- `tundra`
- `wetlands`

The codename file: Now open one of the folders and you will see an XML file named codename. Change the name of it to your codename. Now open it with notepad and you will see it is very ****. You will need to change codename in this line:

```xml
<a name="codename"/>
```

So that it matches your codename. For instance:

```xml
<a name="DuckBlueblu"/>
```

Now repeat that step by doing the same thing with the codename file in each of the biome folders.

## Section 4: Finishing the File

Go back to the 2 original folders, `entities` and `world` and select both of them. Now right click and say **Add to Archive** if you have WinRAR. If you have WinZIP it will be something similar to that. If you have WinZip just follow the WinRar instructions the same but with WinZip. A window will pop up. First, only if you have WinRar, make sure that under Archive Format on the left ZIP is selected. The default is RAR and that will NOT work. In the top under Archive Name enter in any name you want and have it end with .z2f Then hit OK and it will archive it for you. Now, you are done!