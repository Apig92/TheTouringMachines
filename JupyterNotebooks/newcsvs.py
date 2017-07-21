import pandas as pd
import os
import numpy as np

newpath ='/home/csstudent/Routes'
if not os.path.exists(newpath):
    os.makedirs(newpath)

directory = '/home/csstudent/CleanCSV'
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        x= ""+filename+""

    df = pd.read_csv(x) # change for route (possibly programm to run all
    df.columns = ['Timestamp', 'LineID', 'Direction', 'JourneyPatternID', 'TimeFrame', 'VehicleJourneyID', 'Operator', 'Congestion', 'Longitude', 'Latitude', 'Delay', 'BlockID', 'VehicleID', 'StopID', 'AtStop', 'Date']
    df1 = df[['Timestamp', 'LineID', 'JourneyPatternID', 'VehicleJourneyID',  'Congestion', 'Delay', 'StopID', 'AtStop', 'Date']].copy()
    df1=df1[df1.JourneyPatternID != 'null']
    df1=df1[df1.StopID != 'null']
    df1 = df1[df1['AtStop'] == 1]
    df1= df1.dropna( how='any', subset = ['JourneyPatternID', 'StopID'])
    jpid = df1['JourneyPatternID'].unique()
    #need to change type of date
    df1['Date'] = pd.to_datetime(df['Date'])
    df1['Seconds'] = np.nan # new column that will be filled in
    routeID = df1.iloc[1]['LineID']
    # for day in range (7): single file for LineID now
    #     df_day = df1[df1['Date'].dt.dayofweek == day]
    for journey in jpid:
        df2 = df1[df1['JourneyPatternID'] == journey ]
        jid = df2['VehicleJourneyID'].unique()
        count = 0
        for j in jid: # loop through journey id
            df_temp = df2[df2['VehicleJourneyID'] == j ] # temporary df for every journey id
            temp1 = df_temp.head(1)
            if temp1.empty:
                print ('empty df')
                pass
            else:
                c = int(temp1['Timestamp']) # the time for the first stop is 0
                stops = df_temp.StopID.unique() # loop through the individual stops
                data = []
                for i in stops:
                    count += 1
                    temp = df_temp[df_temp['StopID'] == i ].head(1) # the first time the stop appears on the busses radar seems to be most accurate
                    StopID = int(temp['StopID'])
                    #print (temp.index)
                    b = int(temp['Timestamp'])
                    seconds = (b-c)/1000000 # timestamp - the time of the first stop / 1000000 (microseconds) = time from first stop, per route
                    if seconds >=0 and seconds <= 10800: #just catch one trip - 3hr range
                        pass
                    else:
                        seconds = 0
                        c = b
                        print(c, b, seconds)
                    df2.set_value(temp.index, 'Seconds', seconds)
                    print (count)

            print ('done day', count)
            df2 = df2.dropna( how='any', subset = ['Seconds'])
            df2['Day'] = df2.Date.dt.dayofweek
            df2.to_csv("/home/csstudent/Routes/"+str(routeID)+"route.csv") # works for every route
