import pandas as pd
import os



import json
newpath ='/home/csstudent/routes_json'
if not os.path.exists(newpath):
    os.makedirs(newpath)

directory = '/home/csstudent/CleanCSV'
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        x= ""+filename+""
    df = pd.read_csv(x) # change for route (possibly programm to run all)
    df.columns = ['Timestamp', 'LineID', 'Direction', 'JourneyPatternID', 'TimeFrame', 'VehicleJourneyID', 'Operator', 'Congestion', 'Longitude', 'Latitude', 'Delay', 'BlockID', 'VehicleID', 'StopID', 'AtStop', 'Date']

    #drop nulls
    df=df[df.JourneyPatternID != 'null']


    df=df[df.StopID != 'null']


    df['Date'] = pd.to_datetime(df['Date']) # change types


    df['StopID'] = pd.to_numeric(df['StopID']) #change types (for JSON)

    df= df.dropna( how='any', subset = ['JourneyPatternID', 'StopID'])
    pattern = df['JourneyPatternID'].unique()

    df1 = df[df['AtStop'] == 1]
    #Only at stop to get Lat long

    for p in pattern:
        df2 = df1[df1['JourneyPatternID'] == p ]
        df_longlat = df2[['JourneyPatternID', 'Longitude', 'Latitude', 'StopID']].copy() #drop unnecessary columns
        df_longlat['Key']= (df_longlat['Longitude'] + df_longlat['Latitude'])# one value for latlng as identifier
        newdf = pd.DataFrame(columns=['JourneyPatternID', 'Longitude', 'Latitude', 'StopID'])
        stops = df_longlat['StopID'].unique()
        datalist = []
        for i in stops:
            #print (i)
            dftemp=df_longlat[df_longlat['StopID']== i]
            #print (dftemp)
            key = dftemp['Key'].value_counts().idxmax()  # Get the highest value count per stop id
            dftemp=df_longlat[df_longlat['Key']== key].head(1) # Get the first row as all rows are the same
            datalist.append(dftemp)
            routedf = newdf.append(datalist)
        routedf = routedf[['StopID', 'Longitude', 'Latitude']].copy()
        data = json.dumps(json.loads(routedf.to_json(orient='records')), indent=2) # make a JSON File
        with open("/home/csstudent/routes_json/"+p+".json", 'w') as outfile:
           outfile.write(data)
