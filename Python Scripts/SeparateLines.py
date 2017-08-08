#run script in the server, and obtain a csv for each line

import pandas as pd
import csv
import numpy as np
import glob
import time
import numpy
import datetime
import os


def getRoutes(path):
    routes= set()
    for filename in os.listdir(path):
        if filename.endswith(".csv"):
            x = "" + filename + ""
            df = pd.read_csv(x, index_col=None, header=0, low_memory=False)
            df.columns = ["Timestamp", "LineId", "Direction", "JourneyPattern", "Timeframe", "VehicleJourney",
                          "Operator",
                          "Congestion", "Longitude", "Latitude", "Delay", "BlockId", "VehicleId", "StopId", "AtStop"]
            print("Working on day", x)
            #df1 = df.LineId.apply(str)
            # df['LineId'] = df['LineId'].astype(str)

            lines = df['LineId'].unique()
            lines1 = lines[~pd.isnull(lines)]
            routes = routes.union(set(lines1))


        else:
            print(filename, "is not a.csv")

    routes=list(routes)

    return routes


def separateLines(path,routes):
    path2 = "/home/csstudent/AllLines"  # CHANGE ME
    for line in routes:
        frame = pd.DataFrame()
        list_ = []
        print("Creating line:", line)
        for file in os.listdir(path):
            if file.endswith(".csv"):
                x = "" + file + ""
                df = pd.read_csv(x, index_col=None, header=0, low_memory=False)
                df.columns = ["Timestamp", "LineId", "Direction", "JourneyPattern", "Timeframe", "VehicleJourney",
                              "Operator",
                              "Congestion", "Longitude", "Latitude", "Delay", "BlockId", "VehicleId", "StopId",
                              "AtStop"]
                df['LineId'] = df['LineId'].astype(str)
                df1 = df[df['LineId'] == line]
                list_.append(df1)
            else:
                print(file, "is not a.csv")
        frame = pd.concat(list_)
        frame = frame.reset_index(drop=True)
        frame['Date'] = pd.to_datetime(frame['Timestamp'], unit='us')
        # get rid of the night busses
        daytime = frame[(frame.Date.dt.hour != 1) & (frame.Date.dt.hour != 2) & (frame.Date.dt.hour != 3) & (
            frame.Date.dt.hour != 4) & (frame.Date.dt.hour != 5)]
        print('Working on: ' + 'line' + str(line) + 'CLEAN.csv')
        daytime.to_csv(path2 + '/line' + str(line) + 'CLEAN.csv', index=False)
        print('Finished: ' + 'line' + str(line) + 'CLEAN.csv')



def main():
    path = '/home/csstudent/AllDays'  # CHANGE ME
    routes= getRoutes(path)
    print(routes)
    #separateLines(path,routes)


#run script in the server (home directory), and obtain a csv for each line



# This is the path where the CSVs are: do not put anything else in here, as the program loads all the content.
path = '/home/csstudent/AllDays'  # CHANGE ME

# This is the path where you want to save the new CSVs: change it to whatever you want
path2 = "/home/csstudent/AllLines"  # CHANGE ME
allFiles = glob.glob(path+"/*.csv")

#routes = getRoutes(path)

routes= set()
for filename in os.listdir(path):
    if filename.endswith(".csv"):
        x = "" + filename + ""
        df = pd.read_csv(x, index_col=None, header=0, low_memory=False)
        df.columns=["Timestamp","LineId","Direction","JourneyPattern","Timeframe","VehicleJourney","Operator","Congestion","Longitude","Latitude","Delay","BlockId","VehicleId","StopId","AtStop"]

        #print("Working on day", x)
            #df1 = df.LineId.apply(str)
        #df['LineId'] = df['LineId'].astype(str)
        df['LineId'] = df['LineId'].astype('str')

        lines = df['LineId'].unique()
        lines1 = lines[~pd.isnull(lines)]
        routes = routes.union(set(lines1))
    else:
        continue

routes=list(routes)
print(routes)


# This creates a new CSV for each route

for line in routes:
    if not os.path.exists(path2 + '/line' + str(line) + 'CLEAN.csv'):
        frame = pd.DataFrame()
        list_ = []
        print("Creating line:", line)
        for file_ in allFiles:
            df = pd.read_csv(file_, index_col=None, header=0, low_memory=False)
            print("working on", file_)
            df.columns=["Timestamp","LineId","Direction","JourneyPattern","Timeframe","VehicleJourney","Operator","Congestion","Longitude","Latitude","Delay","BlockId","VehicleId","StopId","AtStop"]
            #df= df.LineId.apply(str)
            df['LineId'] = df['LineId'].astype('str')

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
    else:
        print(line,'alredy exists')












