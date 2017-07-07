
# coding: utf-8

# Getting routes
# 

# In[ ]:

import pandas as pd
from collections import OrderedDict
import os


# In[ ]:

newpath ='/home/csstudent/Routesbyday'
if not os.path.exists(newpath):
    os.makedirs(newpath)


# In[ ]:
directory = '/home/csstudent/CleanCSV'
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        x= "'"+filename+"'"

    df = pd.read_csv(x) # change for route (possibly programm to run all
    df.columns = ['Timestamp', 'LineID', 'Direction', 'JourneyPatternID', 'TimeFrame', 'VehicleJourneyID', 'Operator', 'Congestion', 'Longitude', 'Latitude', 'Delay', 'BlockID', 'VehicleID', 'StopID', 'AtStop', 'Date']


    # In[ ]:

    df1 = df[['Timestamp', 'LineID', 'JourneyPatternID', 'VehicleJourneyID',  'Congestion', 'Delay', 'StopID', 'AtStop', 'Date']].copy()


    # In[ ]:

    #df= df.dropna( how='any', subset = ['JourneyPatternID', 'StopID'])
    df1=df1[df1.JourneyPatternID != 'null']


    # In[ ]:

    df1=df1[df1.StopID != 'null']


    # In[ ]:

    df1 = df1[df1['AtStop'] == 1]


    # In[ ]:

    df1= df1.dropna( how='any', subset = ['JourneyPatternID', 'StopID'])


    # In[ ]:

    jpid = df1['JourneyPatternID'].unique()


    # In[ ]:

    #need to change type of date
    df1['Date'] = pd.to_datetime(df['Date'])


    # In[ ]:

    df1['Seconds'] = np.nan # new column that will be filled in


    # In[ ]:

    routeID = df1.iloc[1]['LineID']


    # In[ ]:


    for day in range (7):
        df_day = df1[df1['Date'].dt.dayofweek == day]
        for journey in jpid:
            df2 = df1[df1['JourneyPatternID'] == journey ]
            jid = df_day['VehicleJourneyID'].unique()
            count = 0
            for j in jid: # loop through journey id
                df_temp = df_day[df_day['VehicleJourneyID'] == j ] # temporary df for every journey id
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
                        df_day.set_value(temp.index, 'Seconds', seconds)
                        print (count)

            print ('done day', count)
            df_day = df_day.dropna( how='any', subset = ['Seconds'])
            df_day['Day'] = day
            df_day.to_csv("/home/csstudent/Routesbyday/"+day+routeID+"route.csv") # works for every route


    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:



