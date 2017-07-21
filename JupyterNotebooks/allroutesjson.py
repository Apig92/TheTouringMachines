import pandas as pd
import os



import json
newpath ='/home/csstudent/allroutes_json'
if not os.path.exists(newpath):
    os.makedirs(newpath)

directory = '/home/csstudent/AllLines'
results = {}
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        x= ""+filename+""
    df = pd.read_csv(x) # change for route (possibly programm to run all)
    df.columns = ['Timestamp', 'LineID', 'Direction', 'JourneyPatternID', 'TimeFrame', 'VehicleJourneyID', 'Operator', 'Congestion', 'Longitude', 'Latitude', 'Delay', 'BlockID', 'VehicleID', 'StopID', 'AtStop', 'Date']

    #drop nulls
    df=df[df.JourneyPatternID != 'null']

    df = df.StopID.apply(str)

    #df=df[df.StopID != 'null']




    #df['Date'] = pd.to_datetime(df['Date']) # change types


    #df['StopID'] = pd.to_numeric(df['StopID']) #change types (for JSON)

    df= df.dropna( how='any', subset = ['JourneyPatternID', 'StopID'])
    pattern = df['JourneyPatternID'].unique()

    df1 = df[df['AtStop'] == 1]
    #Only at stop to get Lat long

    for p in pattern:
        df3 = df[df['JourneyPatternID'] == p]
        data = []
        alldata = []
        datalist = []
        newdf = pd.DataFrame(columns=['JourneyPatternID', 'Longitude', 'Latitude', 'StopID'])
        for j in df3['VehicleJourneyID'].unique():
            tempdf = df3[df3['VehicleJourneyID'] == j]
            stops1 = tempdf['StopID'].unique()
            data = stops1
            alldata.append(data)
        maxstops = max(alldata, key=len)
        df_longlat = df3[['JourneyPatternID', 'Longitude', 'Latitude', 'StopID']].copy()  # drop unnecessary columns
        df_longlat['Key'] = (df_longlat['Longitude'] + df_longlat['Latitude'])  # one value for latlng as identifier
        for s in maxstops:
            dfstops = df_longlat[df_longlat['StopID'] == s]
            key = dfstops['Key'].value_counts().idxmax()  # Get the highest value count per stop id
            dfstops = dfstops[dfstops['Key'] == key].head(1)  # Get the first row as rows are ordered
            datalist.append(dfstops)
            routedf = newdf.append(datalist)
        routedf = routedf[['StopID', 'Longitude', 'Latitude']].copy()
        data = json.loads(routedf.to_json(orient='records'))
        print("It's working, It's working!!!!")
        results[p] = data
        print('route finished')
with open("/home/csstudent/allroutes_json/routeinfo.json", 'w') as outfile:
        # outfile.write(data)
        json.dump(results, outfile)
print('done!')
