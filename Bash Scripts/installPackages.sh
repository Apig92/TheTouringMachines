#!/bin/bash

for i in django pandas pickle numpy sklearn numpy scipy; do
  sudo pip install -y $i
done

chmod u+x