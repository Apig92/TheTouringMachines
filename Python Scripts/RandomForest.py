import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import preprocessing
import datetime
import pickle
import joblib
import os


def read(filename):
    df = pd.read_csv(filename, low_memory=False)
    df['Date'] = pd.to_datetime(df['Timestamp'], unit='us')
    df['Hour'] = df.Date.dt.hour
    df['JourneyPatternID'] = df['JourneyPatternID'].astype('category')
    df['Pattern'] = df.JourneyPatternID.cat.codes

    return df

def RandomForest(df,path,filename):
    features = ['Hour', 'Day', 'StopID', 'LineID','Pattern','rain','wdsp','mintp']
    X = pd.concat([df[features]], axis=1)
    y = df.Seconds
    rfc = RandomForestRegressor(n_estimators=100, oob_score=True, random_state=1,)
    rfc.fit(X, y)
    pickle.dump(rfc, open(path+'/'+filename[:-4]+".sav", 'wb'))


def main():
    newpath = '/home/csstudent/Pickles'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    directory = '/home/csstudent/MergedWeather'
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            x = "" + filename + ""
            df = read(x)
            print("Working on",filename)
            RandomForest(df, newpath, x)
        else:
            print(filename,"is not a.csv")





main()




