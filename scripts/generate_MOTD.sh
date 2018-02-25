#!/bin/bash
# Generate a new cookie string and store it in 
# _includes/motd.html. The fortune program needs
# to be installed.

fortune -n 30 -s | tee _includes/motd.html
