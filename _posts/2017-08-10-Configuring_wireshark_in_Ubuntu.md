---
title: Configuring wireshark in Ubuntu
date: 2017-08-10 00:00:00 Z
categories:
- development
tags:
- linux
- networking
layout: post
---

Since my job requires me to spend a lot of time looking at network traffic, I decided that it would be neat to have a way to capture traffic while at home as well.
The idea is that if at any point I want to look at traffic(either wireless or wired) I have a quick way to do it.

To achieve this I am using a box with Ubuntu with two network cards and Wireshark. I configured one of the network cards(internal network) to works a gateway to the other card(internet). Then Wireshark will listen to the packets send across the network card in the internal network and it will be able to see everything going through it. Finally I will add a wifi router with 4 ethernet ports to the internal network, this way I will be able to capture both wireless and wired connections.

In this setup the eth0 is the interface to the internal network and eth1 is the interface to the external network.

## Configure the interfaces to do the routing

    # Set some variables
    ETH_INT="enp4s1"
    ETH_EXT="eth1"
    # Set the IP for the internal interface
    sudo ip addr add 192.168.2.1/24 dev $ETH_INT
    
    # The first rule allows forwarded packets (initial ones). 
    # The second rule allows forwarding of established connection packets (and those related to ones that started). 
    # The third rule does the NAT. 
    sudo iptables -A FORWARD -o $ETH_EXT -i $ETH_INT -s 192.168.2.0/24 -m conntrack --ctstate NEW -j ACCEPT
    sudo iptables -A FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
    sudo iptables -t nat -F POSTROUTING
    sudo iptables -t nat -A POSTROUTING -o $ETH_EXT -j MASQUERADE
    
    # Save iptables so we can load them on boot
    sudo iptables-save | sudo tee /etc/iptables.sav
    
    # Now edit rc.local to load the iptables
    # Since I don't need this configuration to persist, I will not do this step.
    echo "Add the following to your rc.local"
    echo "iptables-restore < /etc/iptables.sav"
    
    # Enable te routing between the two interfaces
    sudo sh -c "echo 1 > /proc/sys/net/ipv4/ip_forward"
    
    # Enable settings in sysctl.conf
    echo "Enable the following settings in /etc/sysctl.conf"
    echo "net.ipv4.ip_forward=1
    
At this point you can configure a device to the internal network and if you configure a static IP and DNS, you should have access to the external network/internel.

## Configuring DHCP and DNS

This step is even easier than the first one.

    ETH_INT="enp4s1"
    
    # Install dnsmasq
    sudo apt-get install dnsmasq
    
    # Stop dnsmasq since we are going to change some settings
    sudo /etc/init.d/dnsmasq stop
    
    # Make a backup of the dnsmasq configuration
    sudo cp /etc/dnsmasq.conf /etc/dnsmasq.conf-backup
    
    # Configure dnsmasq
    echo "Modify /etc/dnsmasq.conf and add the following lines: "
    echo "interface=$ETH_INT"
    echo "dhcp-range=192.168.2.100,192.168.2.250,72h"
    
    # Restart dnsmasq
    echo "Restart dnsmasq"
    echo "sudo /etc/init.d/dnsmasq start"
    sudo /etc/init.d/dnsmasq start
	
At this point you should have dns and DHCP working in the internal network. One caveat that I found was that NetworkManager was trying to manage the internal interface. As a result, my changes were getting overwritten after a period of time. Since I don't need this configuration to be permanent, I disable NetworkManager while the routing of the internal interface is set.

    sudo service NetworkManager stop

## Now Wireshark

You though that configuring dnsmaq was easy? Wireshark cannot be any simple:
	
    # When installing wireshark, you will be asked if you want to configure
    # access to non-root users, select YES
    sudo apt-get install wireshark
    sudo useradd $USER wireshark

You will need to log out and log back in for the group permission  to take effect. But now you can run Wireshark and select your internal network to listen to anything going through it.

## Router

I decided to use a wifi router with DD-WRT to extend the network with 3 more ports + wifi. Now any device connected through the wired or wireless connections will be captured by Wireshark.

## Sources
 - https://help.ubuntu.com/community/Internet/ConnectionSharing

