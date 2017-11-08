﻿# GPU-Viewer
A front-end to glxinfo and Vulkaninfo. 

This project aims to capture all the required/important details of glxinfo and vulkaninfo in a GUI. The project is being developed using python 3 PyGObjects with GTK3. All the required/Important details were extracted using glxinfo/vulkaninfo with the combination of grep, CAT , AWK commands and displayed in the front-end. There is no hard OpenGL Programming involved, until glxinfo and vulkaninfo works the GPU-viewer will also work

![screenshot from 2017-11-07 18-43-41](https://user-images.githubusercontent.com/30646692/32495479-c813ca20-c3eb-11e7-979b-915954c6ad05.png)

![screenshot from 2017-11-07 18-43-57](https://user-images.githubusercontent.com/30646692/32495490-dc8d4c56-c3eb-11e7-92ee-2c1c0ed13739.png)

![screenshot from 2017-11-07 18-44-13](https://user-images.githubusercontent.com/30646692/32495519-f4c7fc58-c3eb-11e7-8338-23869a7080e1.png)

* Please note that the above images solely depends on the Theme being used on the system.

## INSTALLATION STEPS

1. Before Downloading the files please see the Known issues mentioned below
2. Ensure python is installed
3. Download the file and Extract to a folder
4. Navigate to extracted folder, open terminal and enter ./install
5. Choose the theme between Adapta and Numix that you want to apply to the Application. If you install both the themes Adapta will be taken as default.
If the user chooses not install both the themes, the application will take the current system theme. 
5. Once completed,Application can be accessed at menu->System/Administration/System tools->GPU Viewer
6. For Vulkan Tab to work Install Vulkan-Utils (Sudo apt-get install vulkan-utils) in Ubuntu, Vulkan-extra-layers in Arch, Vulkan in Solus, also Vulkan enabled drivers should be installed.
The installer should be able to take care of this dependency in Debian based distro and Solus.
7. Incase of issues launching the application please see the FAQ in Wiki section

## UNINSTALL STEPS

1. Open menu->System/Administration/System tools->GPU Viewer right click and uninstall, click yes on the pop up
2. Remove gpu-viewer directory in \usr\share\  or run sudo rm \usr\share\gpu-viewer -r to remove

## What's developed and available?

1. OpenGL Tab - OpenGL Information, OpenGL ES Information, OpenGL hardware limits and Extensions displayed as per different Vendors, View GLX Frame Buffer Configuration
2. Vulkan Tab - Device Features, Device Limits, Device Extensions,Formats,Memory Types & Heaps, Partial Queue Families implemented, Instance and Layers,Surface Tab
3. About Tab - About GPU Viewer Application, ability to report a bug,view license,view change log, Donate via paypal, GPU Viewer Github main page.


## UNDERDEVELOPMENT

1. OpenGL - OpenGL SPIRV support (low priority - this feature is not available in glxinfo yet,it will be done once implemented by MESA team)
2. General - Bug fixes, Code Optimizations (High Priority)

## IMPORTANT

1. Requires Python to run this Application, works only on linux Operating system
2. For Vulkaninfo to work, nvidia, Mesa and AMD vulkan enabled drivers should be installed along with vulkan-utils

## KNOWN ISSUES

1. Minor UI issues.
2. The Extensions drop down menu in OpenGL tab will not render well if there are too many items, users may see a big empty space at the start. This is a GTK issue (https://github.com/arunsivaramanneo/GPU-Viewer/issues/9)
3. The Application will not render well under dark themes, provided when the user does not select Adapta or Numix during installation

## DEVELOPMENT ENVIRONMENT

1. Operating System : Linux Mint 18.2 (Sonya)/Solus 3
2. Desktop : Cinnamon 3.4.6/Budgie
3. Kernel : 4.13.11-31
4. IDE : SublimeText 3.0,IntelliJ IDEA Community Edition


## SYSTEM SETUP

1. ASUS G551JK ROG Laptop
2. Quad Core Intel Core i7-4710HQ
3. Nvidia Geforce GTX 850m (Discrete GPU) , Drivers - Nvidia (proprietary)
4. Intel Haswel Mobile (Integrated GPU) , Drivers - MESA (Open Source)
5. 8 GB RAM

If you like/use this Application and think i deserve a cup of chai, do a Paypal donation: https://www.paypal.me/ArunSivaraman
