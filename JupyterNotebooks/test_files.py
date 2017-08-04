import pandas as pd
import os
import numpy as np

newpath ='/home/csstudent/Routes'
if not os.path.exists(newpath):
    os.makedirs(newpath)
count = 0
directory = '/home/csstudent/AllLines'
for filename in os.listdir(directory):
    count += 1
    filename = str(filename)
    #print(filename)
    print (count)
    if filename.endswith('py'):
        print ('skip')
    else:
        print (filename)
