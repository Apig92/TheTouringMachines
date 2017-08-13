import pandas as pd
import csv
import numpy as np
import glob
import time
import numpy
import os

'''Creates a dataframe with the weather information'''
def ReadWeather(weatherfile):
    df= pd.read_csv(weatherfile)
    df= df.reset_index(drop=True)
    clean=df.drop(['ind', 'ind.1', 'igmin', 'gmin', 'ind.2', 'cbl','ind.3','hm','ind.4','ddhm','ind.5','hg','sun','dos','soil','pe','evap','smd_wd','smd_md','smd_pd'], axis=1)
    clean['date'] = clean['date'].astype('datetime64[ns]')
    clean['temp'] = (clean['mintp'] + clean['maxtp'])/2
    return clean

'''Creates a dataframe with the bus information'''
def ReadBusline(busfile):
    df=pd.read_csv(busfile)
    df['date'] = df['Date']
    df['date'] = df['date'].astype('datetime64[ns]')
    df['date'] = df['date'].dt.date
    df['date'] = df['date'].astype('datetime64[ns]')
    return df

'''Merges the two datframes, using the date as the merging condition'''
def merge(weather,bus,filename):
    df = pd.merge(bus, weather, how='left', left_on=['date'], right_on=['date'])
    df.to_csv(filename[:-4] + 'weather.csv', index=False)
    return df

if __name__ == "__main__":
    directory = '/home/csstudent/Routes'         #Directory where all CSVs should be stored, both bus and weather
    weather= ReadWeather("daily_weather.csv")
    newpath = '/home/csstudent/MergedWeather/'   #Destination path
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    for filename in os.listdir(directory):
        if filename.endswith("route.csv"):
            x = "" + filename + ""
            bus=ReadBusline(x)
            merge(weather,bus,newpath+x)
            print("Merging:",x)
        else:
            print(filename, "is not a.csv")

