#!/bin/bash
#
# Script for staring jupyter notebook on EC2.
# Run it like this:
#
#   $ bash start.sh
#

# standard directory for notebooks
BOOK=${HOME}/notebook

# kill jupyter if it was already running
sudo pkill jupyter

# make sure notebook directory exists and change into it
mkdir -p ${BOOK}
cd ${BOOK}

# clean up log file in case this script has already been run
sudo rm -rf jupyter-logs.txt

# get public IP to this machine
DNS=`curl -s http://169.254.169.254/latest/meta-data/public-hostname`

# wait three seconds before actually start
sleep 3

# report URL for notebook we are about to start
echo "Starting jupyter notebook, available here in a moment:"
echo "  https://${DNS}:8888"

# start jupyter notebook
nohup jupyter notebook > jupyter-logs.txt &

echo "To kill it later type:"
echo "  pkill jupyter"

