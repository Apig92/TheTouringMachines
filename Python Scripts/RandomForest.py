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
import sys

'''Creates dataframe with the information needed'''
def read(filename):
    df = pd.read_csv(filename, low_memory=False)
    df['Date'] = pd.to_datetime(df['Timestamp'], unit='us')
    df['Hour'] = df.Date.dt.hour
    df['JourneyPatternID'] = df['JourneyPatternID'].astype('category')
    df['Pattern'] = df.JourneyPatternID.cat.codes

    return df

'''Trains model and creates pickle file'''
def RandomForest(df,path,filename,output):
    features = ['Hour', 'Day', 'StopID', 'LineID','Pattern','rain','wdsp','temp']
    X = pd.concat([df[features]], axis=1)
    y = df.Seconds
    rfc = RandomForestRegressor(n_estimators=100, oob_score=True, random_state=1,)
    rfc.fit(X, y)
    print("R Squared: ", metrics.r2_score(y, rfc.predict(X)))
    print("neg_mean_absolute_error: ", metrics.mean_absolute_error(y,rfc.predict(X)))
    print("mean_squared_error: ", metrics.mean_squared_error(y, rfc.predict(X)))
    print("median_absolute_error: ", metrics.median_absolute_error(y, rfc.predict(X)))
    pickle.dump(rfc, open(path+'/'+filename[:-4]+".sav", 'wb'))


if __name__ == "__main__":
    newpath = '/home/csstudent/DublinBus/TTM/static/TTM/pickles'          #Destination folder
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    directory = '/home/csstudent/MergedWeather'  #Folder where all the CSV files are contained
    f = open('RandomForestResults.txt', 'w')     #Creates .txt file where all the model information and stats are contained
    orig_stdout = sys.stdout                     #Original output, the terminal
    sys.stdout = f                               #Change output to the file
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            x = "" + filename + ""
            df = read(x)
            print("Stats for Line",filename)
            RandomForest(df, newpath, x, f)
            print('--------------------------------------------------')
        else:
            continue
    sys.stdout = orig_stdout                     #Change output back to terminal
    f.close()








