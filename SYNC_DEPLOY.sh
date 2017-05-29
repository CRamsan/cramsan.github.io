#!/bin/bash
git reset --hard
git pull origin master
./DEPLOY_PROD.sh
# git push
