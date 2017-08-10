import pandas as pd
import csv
import numpy as np
import glob
import time
import numpy
import datetime
import os

'''This function creates a list with all the unique bus lines'''
def getRoutes(path):
    routes = set()
    for filename in os.listdir(path):
        if filename.endswith(".csv"):
            x = "" + filename + ""
            df = pd.read_csv(x, index_col=None, header=0, low_memory=False, keep_default_na=False)
            df.columns = ["Timestamp", "LineId", "Direction", "JourneyPattern", "Timeframe", "VehicleJourney",
                          "Operator",
                          "Congestion", "Longitude", "Latitude", "Delay", "BlockId", "VehicleId", "StopId", "AtStop"]
            df['LineId'] = df['LineId'].astype('str')
            lines = df['LineId'].unique()
            lines1 = lines[~pd.isnull(lines)]
            routes = routes.union(set(lines1))
        else:
            continue
    routes=list(routes)
    print('There are this many unique routes',len(routes),'\n final routes')
    print(routes)
    return routes


'''This function gets all the original CSVs, and divides them by bus line (one new CSV per bus line). It also gets rid of the buses running at night.'''
def separateLines(routes,allFiles,path2):
    for line in routes:
        if not os.path.exists(path2 + '/line' + str(line) + 'CLEAN.csv'):
            frame = pd.DataFrame()
            list_ = []
            print("Creating line:", line)
            for file_ in allFiles:
                df = pd.read_csv(file_, index_col=None, header=0, low_memory=False)
                print("working on", file_)
                df.columns=["Timestamp", "LineId", "Direction", "JourneyPattern", "Timeframe", "VehicleJourney",
                          "Operator",
                          "Congestion", "Longitude", "Latitude", "Delay", "BlockId", "VehicleId", "StopId", "AtStop"]
                clean = df.drop(['Direction', 'Operator', 'Congestion', 'Delay', 'BlockId', 'VehicleId'], axis=1)

                clean['LineId'] = clean['LineId'].astype('str')
                df1 = clean[clean['LineId'] == line]
                list_.append(df1)
            frame = pd.concat(list_)
            frame = frame.reset_index(drop=True)
            frame['Date'] = pd.to_datetime(frame['Timestamp'], unit='us')
            #get rid of the night buses
            daytime = frame[(frame.Date.dt.hour != 1) & (frame.Date.dt.hour != 2) & (frame.Date.dt.hour != 3) & (
            frame.Date.dt.hour != 4) & (frame.Date.dt.hour != 5)]
            print('Working on: ' + 'line' + str(line) + 'CLEAN.csv')
            daytime.to_csv(path2 + '/line' + str(line) + 'CLEAN.csv', index=False)
            print('Finished: ' + 'line' + str(line) + 'CLEAN.csv')
        else:
            print(line,'alredy exists')

if __name__ == "__main__":
    #run script in the server (path directory), and obtain a csv for each line
    path = '/home/csstudent/AllDays/'  # Folder where all CSVs are contained
    # This is the path where you want to save the new CSVs: change it to whatever you want
    path2 = "/home/csstudent/AllLines"  # Destination folder
    allFiles = glob.glob(path+"/*.csv")
    routes=getRoutes(path)
    separateLines(routes,allFiles,path2)




