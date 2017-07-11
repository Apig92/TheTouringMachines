#run script in the server (home directory), and obtain a csv for each line

import pandas as pd
import csv
import numpy as np
import glob
import time
import numpy


# This is the path where the CSVs are: do not put anything else in here, as the program loads all the content.
path = r'./AllDays'  # CHANGE ME

# This is the path where you want to save the new CSVs: change it to whatever you want
path2 = "./AllLines"  # CHANGE ME
allFiles = glob.glob("/*.csv")

# get lines by reading one of the CSVs
df = pd.read_csv(path+ "/siri.20121106.csv", index_col=None, header=0, low_memory=False)  # Use whatever file you wish
df.columns = ["Timestamp", "LineId", "Direction", "JourneyPattern", "Timeframe", "VehicleJourney", "Operator",
              "Congestion", "Longitude", "Latitude", "Delay", "BlockId", "VehicleId", "StopId", "AtStop"]

# Save the lines in an array
lines = df['LineId'].unique()
lines = lines[~pd.isnull(lines)]

print(lines)
# This creates a new CSV for each route

for line in lines:
    frame = pd.DataFrame()
    list_ = []
    print("Creating line:", line)
    for file_ in allFiles:
        df = pd.read_csv(file_, index_col=None, header=0, low_memory=False)
        df.columns = ["Timestamp", "LineId", "Direction", "JourneyPattern", "Timeframe", "VehicleJourney", "Operator",
                      "Congestion", "Longitude", "Latitude", "Delay", "BlockId", "VehicleId", "StopId", "AtStop"]
        df= df.LineId.apply(str)
        df1 = df[df['LineId'] == line]
        list_.append(df1)
    frame = pd.concat(list_)
    frame = frame.reset_index(drop=True)
    frame['Date'] = pd.to_datetime(frame['Timestamp'], unit='us')
    #get rid of the night busses
    daytime = frame[(frame.Date.dt.hour != 1) & (frame.Date.dt.hour != 2) & (frame.Date.dt.hour != 3) & (
    frame.Date.dt.hour != 4) & (frame.Date.dt.hour != 5)]
    print('Working on: ' + 'line' + str(line) + 'CLEAN.csv')
    daytime.to_csv(path2 + '/line' + str(line) + 'CLEAN.csv', index=False)
    print('Finished: ' + 'line' + str(line) + 'CLEAN.csv')




