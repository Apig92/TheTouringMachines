#!/bin/bash

for filename in *;
 do mongoimport --db DublinBus --collection Stops --file $filename;
done

chmod u+x mongoimport.sh
