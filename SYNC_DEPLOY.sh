#!/bin/bash -x
git pull origin master
./DEPLOY_PROD.sh
git push
