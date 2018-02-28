#!/bin/bash
# This script will install the required components to run jekyll.
# It is assumed that gem and pip are already installed.
# 1. Install all the required gems and install jekyll and bundler.
# 2. Use pip to install the flickerapi.
export PATH=~/.gem/ruby/2.3.0/bin:~/.gem/ruby/2.4.0/bin:~/.gem/ruby/2.5.0/bin:$PATH
gem update
gem install jekyll bundler
pip install flickrapi  