#!/bin/bash
# This script is used mostly during deployment. Reset the current repo to a
# clean state, then pull the latest content and start the deployment to PROD.
# Once the deployment is ready push the content to the mirror.
git reset --hard
git pull origin master
./scripts/deploy_prod.sh
git push mirror master
