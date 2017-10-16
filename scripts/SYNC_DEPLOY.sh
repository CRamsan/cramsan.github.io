#!/bin/bash
git reset --hard
git pull origin master
./scripts/DEPLOY_PROD.sh
git push mirror master
