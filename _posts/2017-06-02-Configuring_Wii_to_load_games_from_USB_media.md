---
layout: post
title: Configuring Wii to load games from USB media
tags: wii gamecube backup mods
categories: gaming
---

**This guide was developed based on my very limited knowledge and the most up to date information that I could find.**

In order to reduce the wear and tear in my GameCube and Wii, I have decided to configure one of my Wiis to load all the games from an external media. It took me longer than it should have so I am documenting the process I went through so other people don't have to go through the same thing.

## Install the HomeBrew channel

Starting from a vanilla Wii, you first need to install the Homebrew channel, which will be your door to load almost all homebrew software. Head over to [Wiibrew][1] and select the exploit that best matches your system, the main factor here is the OS version of the Wii. My favorite method is [LetterBomb][2] because of how easy it is to execute and it does not even need a game. 

### Requirements
 - SD or SDHC formatted as FAT16 or FAT32.
 - **System Menu 4.3** (anything lower will not work).
 - Your Wii’s WiFi MAC Address (available from your Wii's system settings). This is needed because the Wii will only accept messages addressed to its specific MAC address.
 - A way to copy the files from your PC to the SD card (card reader, printer, etc.)
 - Some homebrew software to load. Although this isn't necessary, it's highly recommended. The exploit will attempt to load "boot.elf" (or "boot.dol" if it can't be found) from the SD card root directory. For this example we will load the homebrew channel.

### Instructions
#### On your computer
 - Go to [BootMii][4] and download the latest HackMii installer.
 - Extract the content of the installer and find the boot.elf file. 
 - Copy the bool.elf file to the root of your sd card.
 - Go to the [LetterBomb][5] page and enter the Mac address of your Wii, now a file will be downloaded.
 - If there is a folder titled "private" on your SD card, rename it to "privateold"
 - Copy the "private" directory from the LetterBomb download to the root of your SD card.

### On your Wii
 - Put your SD card in your Wii and turn it on.
 - Go into the Wii Message Board and navigate to "Today", "Yesterday" or "Two days ago".
 - Click on the appropriate envelope, sit back and prepare for the hacking glory.
 - Wait for the Hackmii Installer to run tests on your Wii
 - Press Wiimote 1 Button when told to continue installing HBC and BootMii. 
 - The installation should be automatic from this point on, and your Wii will reboot.

At this point you should have the Homebrew channel installed and accesible from the Wii main menu. Now that the Homebrew channel is installed you have the power to load homebrew software directly from the SD card.

### Install a WAD manager
You will also need a tool called a WAD manager. I suggest [this][7] page for detailed instructions. 

## Install the loader
Now that we have access to loading homebrew from the SD card, the next step is to load 'something' to read data from USB storage. For this we are going to use a USB loader, which does pretty much what it's name say, it loads stuff from USB storage. The USB loader is the equivalent of user-space drivers to read and write from a device. It will handle accessing the storage device connected through USB as well as manage the filesystem. You can find the list of loaders [6][here]. Most loaders will work with the Wii in 'Wii' mode, so they will be able to read Wii discs as well as load games from the disc tray. To been able to load gamecube games you will also need a 'Gamecube' loader.

We will use USBLoaderGX as our USB loader and Nintendont as our Gamecube loader. When I started looking into using a Gamecube loader I wanted to user Devolution because it supports network connectivity for GC games, but sadly I was not able to get it to work.

### Install USBLoaderGX
### Requirements
 - You will need the SD card previously configured
 - A thumbdrive or USB hard-drive formatted as FAT32 to store games.

### Instructions
***This is very important. You need to ensure you are using the latest files, otherwise things will not work as expected. Double check the version of everything.***

 - Go to the [USBLoaderGX][8] download page and download the latest file. As of now that is '/ Releases/New revisions (3.0+)/USBLoaderGX r1262.7z'
 - Extract the file and place it it's content in the SD card. Now the folder called 'usbloader_gx' should be inside sd:/apps/.
 - Now you can load USBLoaderGX from the Homebrew channel. Give it a try to make sure everything is working as expected.

At this point you have USBLoaderGX working and you are ready to install Nintendont and rip some games. 

To install Nintendont follow the instructions from [here][9]. **If you don't see the settings to configure Nintendont in USBLoaderGX it may mean you have an old version of the USB loader. Please verify you have the latest version installed.**

Connect the USB media you want to rip your games to. On the USBLoaderGX settings, go to the Custom path settings and then change the default path for save and write games to, from the SD card to the USB drive. Now if you insert a gamecube disc, you will have the option to install it to the USB drive. Once the game is saved, you can remove it and now you will be able to load the game directly from the USB media.

[1]: http://wiibrew.org/wiki/Homebrew_Channel
[2]: http://wiibrew.org/wiki/LetterBomb
[4]: https://bootmii.org/download/
[5]: https://please.hackmii.com
[6]: https://sites.google.com/site/completesg/backup-launchers/usb
[7]: https://sites.google.com/site/completesg/how-to-use/wad-manager
[8]: https://sourceforge.net/projects/usbloadergx/files/Releases/
[9]: https://sites.google.com/site/completesg/backup-launchers/gamecube/nintendont