---
layout: post
categories: social
tags: buffer
buffer: true
title: "Configuring Wii to load games from USB media"
date: 2017-06-05 19:44:56
services: 
  - facebook
---
Configuring Wii to load games from USB media<br />
<br />
This guide was developed based on my very limited knowledge and the most up to date information that I could find.<br />
<br />
In order to reduce the wear and tear in my GameCube and Wii, I have decided to configure one of my Wiis to load all the games from an external media. It took me longer than it should have so I am documenting the process I went through so other people dont have to go through the same thing.<br />
<br />
Install the HomeBrew channel<br />
<br />
Starting from a vanilla Wii, you first need to install the Homebrew channel, which will be your door to load almost all homebrew software. Head over to Wiibrew and select the exploit that best matches your system, the main factor here is the OS version of the Wii. My favorite method is LetterBomb because of how easy it is to execute and it does not even need a game.<br />
<br />
Requirements<br />
<br />
SD or SDHC formatted as FAT16 or FAT32.<br />
<br />
System Menu 4.3 (anything lower will not work).<br />
<br />
Your Wiis WiFi MAC Address (available from your Wiis system settings). This is needed because the Wii will only accept messages addressed to its specific MAC address.<br />
<br />
A way to copy the files from your PC to the SD card (card reader, printer, etc.)<br />
<br />
Some homebrew software to load. Although this isnt necessary, its highly recommended. The exploit will attempt to load boot.elf (or boot.dol if it cant be found) from the SD card root directory. For this example we will load the homebrew channel.<br />
<br />
Instructions<br />
<br />
On your computer<br />
<br />
Go to BootMii and download the latest HackMii installer.<br />
<br />
Extract the content of the installer and find the boot.elf file.<br />
<br />
Copy the bool.elf file to the root of your sd card.<br />
<br />
Go to the LetterBomb page and enter the Mac address of your Wii, now a file will be downloaded.<br />
<br />
If there is a folder titled private on your SD card, rename it to privateold<br />
<br />
Copy the private directory from the LetterBomb download to the root of your SD card.<br />
<br />
On your Wii<br />
<br />
Put your SD card in your Wii and turn it on.<br />
<br />
Go into the Wii Message Board and navigate to Today, Yesterday or Two days ago.<br />
<br />
Click on the appropriate envelope, sit back and prepare for the hacking glory.<br />
<br />
Wait for the Hackmii Installer to run tests on your Wii<br />
<br />
Press Wiimote 1 Button when told to continue installing HBC and BootMii.<br />
<br />
The installation should be automatic from this point on, and your Wii will reboot.<br />
<br />
At this point you should have the Homebrew channel installed and accesible from the Wii main menu. Now that the Homebrew channel is installed you have the power to load homebrew software directly from the SD card.<br />
<br />
Install a WAD manager<br />
<br />
You will also need a tool called a WAD manager. I suggest this page for detailed instructions.<br />
<br />
Install the loader<br />
<br />
Now that we have access to loading homebrew from the SD card, the next step is to load something to read data from USB storage. For this we are going to use a USB loader, which does pretty much what its name say, it loads stuff from USB storage. The USB loader is the equivalent of user-space drivers to read and write from a device. It will handle accessing the storage device connected through USB as well as manage the filesystem. You can find the list of loaders [6][here]. Most loaders will work with the Wii in Wii mode, so they will be able to read Wii discs as well as load games from the disc tray. To been able to load gamecube games you will also need a Gamecube loader.<br />
<br />
We will use USBLoaderGX as our USB loader and Nintendont as our Gamecube loader. When I started looking into using a Gamecube loader I wanted to user Devolution because it supports network connectivity for GC games, but sadly I was not able to get it to work.<br />
<br />
Install USBLoaderGX<br />
<br />
Requirements<br />
<br />
You will need the SD card previously configured<br />
<br />
A thumbdrive or USB hard-drive formatted as FAT32 to store games.<br />
<br />
Instructions<br />
<br />
This is very important. You need to ensure you are using the latest files, otherwise things will not work as expected. Double check the version of everything.<br />
<br />
Go to the USBLoaderGX download page and download the latest file. As of now that is / Releases/New revisions (3.0+)/USBLoaderGX r1262.7z<br />
<br />
Extract the file and place it its content in the SD card. Now the folder called usbloader_gx should be inside sd:/apps/.<br />
<br />
Now you can load USBLoaderGX from the Homebrew channel. Give it a try to make sure everything is working as expected.<br />
<br />
At this point you have USBLoaderGX working and you are ready to install Nintendont and rip some games.<br />
<br />
To install Nintendont follow the instructions from here. If you dont see the settings to configure Nintendont in USBLoaderGX it may mean you have an old version of the USB loader. Please verify you have the latest version installed.<br />
<br />
Connect the USB media you want to rip your games to. On the USBLoaderGX settings, go to the Custom path settings and then change the default path for save and write games to, from the SD card to the USB drive. Now if you insert a gamecube disc, you will have the 
