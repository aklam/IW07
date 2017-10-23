#!/bin/bash
#
# Setup script for getting jupyter notebook set up for secure connection on EC2
# Run it like this:
#
#   $ bash setup.sh
#

# some standard directories we will use
SETUP=${HOME}/ec2setup
JUP=${HOME}/.jupyter
CERT=${JUP}/cert

# clean up in case this script has already been run or there was already a configuration
sudo rm -rf ${JUP} 

# setup config and SSL cert for jupyter
mkdir -p ${CERT}
cd ${CERT}
sudo openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout cert.key -out cert.pem -batch > logs.txt 2>&1
cp ${SETUP}/jupyter_notebook_config.py ${JUP}

