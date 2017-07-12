#This scripts creates a separate csv file for every route, run in the server from the home folder

import pandas as pd
import csv
import numpy as np
import glob
import time
import numpy




#This is the path where the CSVs are: do not put anything else in here, as the program loads all the content.
path =r'./AllDays'      #path in the server

#This is the path where you want to save the new CSVs: change it to whatever you want
path2="./AllRoutes"   #path in the server
allFiles = glob.glob(path + "/*.csv")

#get lines by reading one of the CSVs
df = pd.read_csv(path+"/siri.20121106.csv",index_col=None, header=0, low_memory=False)  #Use whatever file you wish
df.columns=["Timestamp","LineId","Direction","JourneyPattern","Timeframe","VehicleJourney","Operator","Congestion","Longitude","Latitude","Delay","BlockId","VehicleId","StopId","AtStop"]

#Save the routes in an array
lines=df['JourneyPattern'].unique()
lines = lines[~pd.isnull(lines)]
print(lines)


#This creates a new CSV for each route

for line in lines:
    frame = pd.DataFrame()
    list_ = []
    print("Creating Route:", line)
    for file_ in allFiles:
        df = pd.read_csv(file_,index_col=None, header=0, low_memory=False)
        df.columns=["Timestamp","LineId","Direction","JourneyPattern","Timeframe","VehicleJourney","Operator","Congestion","Longitude","Latitude","Delay","BlockId","VehicleId","StopId","AtStop"]
        df1 = df[ df['JourneyPattern'] == line]
        list_.append(df1)
    frame = pd.concat(list_)
    frame = frame.reset_index(drop=True)
    frame['Date'] = pd.to_datetime(frame['Timestamp'], unit='us')
    #Get rid of the night busses
    daytime = frame[(frame.Date.dt.hour != 1) &(frame.Date.dt.hour !=2) & (frame.Date.dt.hour !=3) &(frame.Date.dt.hour !=4) & (frame.Date.dt.hour !=5)  ]
    print('Working on: '+'route'+str(line)+'CLEAN.csv')
    daytime.to_csv(path2+'/route'+str(line)+'CLEAN.csv', index=False)
    print('Finished: '+ 'route' + str(line) + 'CLEAN.csv')



    

