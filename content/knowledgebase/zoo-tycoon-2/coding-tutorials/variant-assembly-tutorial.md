---
title: Variant Assembly Tutorial
draft: false
date: 2007-07-10T02:35:00+0700
author: Penguinman
---

# Variant Assembly Tutorial

Welcome to VAT, a guide made by penguinman to help you create a variant skin for an animal in ZT2. This will only work for members with the Endangered Species (ES) expansion pack. 

Before we begin, there are some programs you will want. One thing you must have is an extracting program. WinRar and WinZip are highly recommended free downloads which serve this purpose. The second one is called DxtBmp and it is so useful during the re-coloring stage. It is a free download here: [http://www.mnwright.btinternet.co.uk/pr ... dxtbmp.htm](https://www.mwgfx.co.uk/programs/dxtbmp.htm) The download is at the bottom of the page. (And yes, its an aircraft site).

This tutorial contains all the folders you will need so place everything in the entities folder that is included.

## Part 1: Getting the files

To begin, go to `C:\Program Files\Microsoft Games\Zoo Tycoon 2`. If you cannot find this file, you must find the folder named `Zoo Tycoon 2` in the location where you installed the game. Now you must decide which animal you want the variant to be for. If it is for an ES animal, open the file called `x100_000` using the extracting program (WinRar or WinZip). If the animal is from original ZT2 then open the file called `entities` in the same way.

In either of these files go to: `entities/units/animals`. Inside that folder you will see many other folders, each with an animal related to it. The folder name will often be the animal's name backwards, such as `BearPolar` or `WolfGray`. It will be easy to locate the folder of your animal.

Inside that folder find the `_Adult.dds` file, the `Adult_Sick.dds` file, the `Adult_Dirty.dds` file and the `Adult_Sick_Dirty.dds` file. The names will vary between animals but it generally has something similar to that. It may contain an `F` or `M` in it as well. Copy and paste those into your `entities/units/animals/codename` file (the one included with this tutorial).

Now in your entities file, included with the tutorial, go to `entities/units/animals` and rename the folder called `codename` to match the name of the folder for your animal exactly as the original, such as `BearPolar` or `WolfGray`.

## Part 2: Re-coloring

Next open DxtBmp. Go to **File > Open** and then browse until you find the first .dds file in your entities folder.

Now go to "Prefs" and choose what editor you want to use (such as PSP, Adobe, or MS Paint) to recolor with. Now double click on the image in the center. DO NOT CLOSE DXTBMP

Now edit (color) the skin in your editor of choice and save it in that editor, but DO NOT use Save As. Now exit the file and close the editor.

Go back to DXTBMP and click on the "Refresh After Edit" button on the bottom. The new and edited skin should appear.

Now click **File > Save As**, and select .dds texture. In the save menu at the bottom there is a drop down menu. Select DXT1 in the drop down menu and then save the file.

In order to name the file, you must select a number and add an underscore plus a number to the end of each of the 4 .dds files. If the game already uses _1 for a variant, then you should use another number such as `_2`, `_3`, or `_4`. You can only use numbers up to 5. The re-named files will be something like: `WolfGray_Adult_F_4`, `WolfGray_Adult_Sick_4`, `WolfGray_Adult_Dirty_4` and `WolfGray_Adult_Sick_Dirty_4` depending on what your animal is.

## Part 3: Making it work

Now right click on the entities folder and select **Add To Archive**. If using WinRar make sure that .zip is selected and not .rar. Then name it in the renaming box, making sure it ends with .z2f instead of .zip. Then select ok and you are done!