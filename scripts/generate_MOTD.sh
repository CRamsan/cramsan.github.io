#!/bin/bash
# Generate a new cookie
fortune -n 30 -s | tee _includes/motd.html
