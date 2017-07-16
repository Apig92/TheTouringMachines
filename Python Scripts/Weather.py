import pandas as pd
import csv
import numpy as np
import glob
import time
import numpy
import os


def ReadWeather(weatherfile):
    df=pd.read_csv(weatherfile)
    df['date'] = df['date'].astype('datetime64[ns]')
    return df


def ReadBusline(busfile):
    df=pd.read_csv(busfile)
    df = df.rename(columns={'Timeframe': 'date'})
    df['date'] = df['date'].astype('datetime64[ns]')
    return df

def merge(weather,bus,filename):
    df = pd.merge(bus, weather, how='left', left_on=['date'], right_on=['date'])
    df.to_csv(filename + 'weather.csv', index=False)
    return df

def main():
    weather= ReadWeather("weather.csv")
    newpath = '/home/csstudent/MergedWeather'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    directory = '/home/csstudent/Routes'
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            x = "" + filename + ""
            bus=ReadBusline(x)
            merge=merge(weather,bus,x)
            print("Merging:",x)
        else:
            print(filename, "is not a.csv")

main()