#!/bin/bash

sudo apt-get update

for i in django pandas numpy sklearn numpy scipy; do
  sudo pip install $i
done


chmod u+x installPackages.sh