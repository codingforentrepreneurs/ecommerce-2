#!/bin/bash
echo -e "*************************************************************"
echo -e "************ Installing required system modules *************"
echo -e "*************************************************************"
sudo apt-get -y update
sudo apt-get -y upgrade

echo -e "************     Installing Python3 and pip     *************"
sudo apt-get -y install python-pip python-dev build-essential
sudo apt-get -y install libssl-dev libffi-dev
pip3 install --upgrade pip

echo -e "************     Installing Dependencies     *************"
cd /vagrant
sudo -H pip install -r src/requirements.txt
