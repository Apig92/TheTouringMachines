import pandas as pd
import os




import json
newpath ='/home/csstudent/allroutes_json'
if not os.path.exists(newpath):
    os.makedirs(newpath)

directory = '/home/csstudent/AllLines'
results = {}
for filename in os.listdir(directory):
    if filename.startswith("line"):
        x= ""+filename+""
    df = pd.read_csv(x, encoding='Latin1') # change for route (possibly programm to run all)
    df.columns = ['Timestamp', 'LineID', 'JourneyPatternID', 'TimeFrame', 'VehicleJourneyID',
                 'Longitude', 'Latitude', 'StopID', 'AtStop', 'Date']
    newdf = pd.read_csv('route_seq.csv', encoding='Latin1') # new info available
    newdf = newdf.rename(columns={'Stop_ID': 'StopID'}) #must be the same name to merge
    df = df.dropna(how='any', subset=['JourneyPatternID', 'StopID'])
    newdf['StopID'] = pd.to_numeric(newdf['StopID']) #must be same dtype
    df['StopID'] = df.StopID.apply(str)
    df = df[df.StopID != 'null']
    df = df[df.StopID != 'nan'] #fixing errors that occur infrequently
    df['StopID'] = pd.to_numeric(df['StopID'])
    df['LineID'] = df['LineID'].astype(str)
    newdf['LineID'] = newdf['LineID'].astype(str)
    #merge them
    df4 = pd.merge(df, newdf, how='inner', on=['LineID', 'StopID'])
    df4 = df4.dropna(how='any', subset=['JourneyPatternID', 'StopID'])
    df4=df4[df4.JourneyPatternID != 'null']

    pattern = df4['JourneyPatternID'].unique()


    df4['Date'] = pd.to_datetime(df4['Date']) # change types


    df4['StopID'] = pd.to_numeric(df4['StopID']) #change types (for JSON)


    df1 = df4[df4['AtStop'] == 1]
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
        if routedf.empty:
            print('empty df')
        else:
            data = json.loads(routedf.to_json(orient='records'))
            print(p)
            results[p] = data
        print('route finished')
with open("/home/csstudent/allroutes_json/routeinfo.json", 'w') as outfile:
        # outfile.write(data)
        json.dump(results, outfile)
print('done!')
