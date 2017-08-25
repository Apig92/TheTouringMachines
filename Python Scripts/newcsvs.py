# Program to write seconds day ad hors to new csvs per line + clean data
import pandas as pd
import os
import numpy as np

newpath ='/home/csstudent/Routes'
#make a folder if none exists
if not os.path.exists(newpath):
    os.makedirs(newpath)

directory = '/home/csstudent/AllLines'   #denotes the location of all the files

for filename in os.listdir(directory):
#loop through all cleaned data
    filename = str(filename)
    print(filename)   #visual cues for when running
    if filename.startswith("line"):
        print("starting" + filename)
        filename = str(filename)
        x= ""+filename+""
        if filename[3] == 'e':
            routeID = filename[4:-4]
        else:
            routeID = filename[3:-4]
        #extracts the name of the new file
        df = pd.read_csv(x, converters={'LineID':'str'})   # convert LineID to string
        df.columns = ['Timestamp', 'LineID', 'JourneyPatternID', 'TimeFrame', 'VehicleJourneyID', 'Longitude', 'Latitude', 'StopID', 'AtStop', 'Date']
        df1 = df[['Timestamp', 'LineID', 'JourneyPatternID', 'VehicleJourneyID', 'StopID', 'AtStop', 'Date']].copy()

        df1['StopID'] = df1['StopID'].astype(str)   #get rid of nulls, ns's. 'null' and 'nan'.
        df1=df1[df1.JourneyPatternID != 'null']
        df1=df1[df1.StopID != 'null']

        df1['StopID'] = pd.to_numeric(df1['StopID'])  # change types (for JSON)
        df1 = df1.dropna(how='any', subset=['JourneyPatternID', 'StopID'])
        df1 = df1[df1['AtStop'] == 1]
        df1= df1.dropna( how='any', subset = ['JourneyPatternID', 'StopID'])
        jpid = df1['JourneyPatternID'].unique()
        df1['Date'] = pd.to_datetime(df['Date'])  #change type of date
        df1['Seconds'] = np.nan  # new column that will be filled in
        for journey in jpid:
            df2 = df1[df1['JourneyPatternID'] == journey ]
            jid = df2['VehicleJourneyID'].unique()
            for j in jid:  # loop through journey id
                df_temp = df2[df2['VehicleJourneyID'] == j ]  # temporary df for every journey id
                temp1 = df_temp.head(1)
                if temp1.empty:
                    print ('empty df')
                    pass
                else:
                    c = int(temp1['Timestamp'])  # the time for the first stop is 0
                    stops = df_temp.StopID.unique()  # loop through the individual stops
                    data = []
                    for i in stops:
                        temp = df_temp[df_temp['StopID'] == i ].head(1)  # the first time the stop appears on the busses radar seems to be most accurate
                        StopID = int(temp['StopID'])
                        b = int(temp['Timestamp'])
                        seconds = (b-c)/1000000  # timestamp - the time of the first stop / 1000000 (microseconds) = time from first stop, per route
                        if seconds >=0 and seconds <= 10800:  #just catch one trip - 3hr range
                            pass
                        else:
                            seconds = 0
                            c = b
                        df1.set_value(temp.index, 'Seconds', seconds)

        df1 = df1.dropna( how='any', subset = ['Seconds'])  # drop any empties
        df1['Day'] = df1.Date.dt.dayofweek  # add a column for day of the week
        df1.to_csv("/home/csstudent/Routes/"+str(routeID)+"route.csv")  # works for every route
        print ("done Line"+ routeID)
print ('Finished')
