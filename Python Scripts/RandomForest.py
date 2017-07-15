import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import datetime
import pickle
import joblib
import os


def read(filename):
    df = pd.read_csv(filename, low_memory=False)
    df['Hour'] = df['Date']
    df['Date'] = pd.to_datetime(df['Timestamp'], unit='us')
    for iter in range (len(df)):
        df.iloc[iter,12]=df.iloc[iter, 9].hour
    df['Hour'] = df['Hour'].astype('category')
    df['Day'] = df['Day'].astype('category')
    df['LineID'] = df['LineID'].astype('category')
    df['JourneyPatternID'] = df['JourneyPatternID'].astype('category')
    df['StopIDID'] = df['StopID'].astype('category')

    return df

def RandomForest(df,path,filename):
    features = ['Hour', 'Day', 'StopID', 'LineID']
    X = pd.concat([df[features]], axis=1)
    y = df.Seconds
    rfc = RandomForestRegressor(n_estimators=130, oob_score=True, random_state=1,)
    rfc.fit(X, y)
    pickle.dump(rfc, open(path+'/'+filename+".sav", 'wb'))


def main():
    newpath = '/home/csstudent/Pickles'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    directory = '/home/csstudent/Routes'
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            x = "" + filename + ""
        else:
            print("There are no files")
            break

        df=read(x)
        RandomForest(df,newpath,x)


main()




