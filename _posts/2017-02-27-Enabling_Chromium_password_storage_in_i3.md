---
layout: post
title: Enabling Chromium password storage in i3
tags: chromium i3 linux
categories: linux
---

Chroium may not use the correct password storage under linux if it fails to detect the desktop enviroment. In my case, when using i3 as my WM witout a desktop enviroment, Chromium was failing to unlock the keychain and a result all my creds would have been stored in plain text. To solve this problem you can use the `--password-store=<basic|gnome|kwallet>` paramenter. Since I use gnome-keyring, I will use --password-storage=gnome, to ensure Chromium stores all the creds in the gnome-keyring.

Couple things that help me debug this issue was the information at [chrome://signin-internals]() and the flags `--enable-logging=stderr --v=1` to enable logging in Chromium.
Also if you want to make the `--password-store` a permanent flag in Arch Linux, you can store it in chromium-flags.conf under $HOME/.config/.

Sources:
> - chromium --help
> - https://wiki.archlinux.org/index.php/Chromium/Tips_and_tricks
> - https://www.chromium.org/for-testers/enable-logging
> - https://productforums.google.com/forum/#!topic/chrome/POKH5enbwgU
