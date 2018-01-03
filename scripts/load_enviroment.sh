#!/bin/bash
# Use this script to load everything scripts and variables
# This script assumes that is run from the root of the repo.

if [ ! -d "scripts" ]; then
	echo "Folder \"scripts\" does not exist."
	return
fi

if [ ! -d ".git" ]; then
	echo "Are you on the root of the repository? Folder .git seems to be missing"
	return
fi

CURRENT_DIR=$(pwd)
export PATH=$CURRENT_DIR/scripts:/home/cramsan/.gem/ruby/2.4.0/bin/:$PATH
