import pandas as pd
import numpy as np
import os
from sklearn.ensemble import RandomForestRegressor
import pickle

def predictions(hour, day, start, end, line,pattern,rain,wind,temp):
    filename = os.path.join(settings.DATA_PATH, 'pickles/'+line+'.sav')
    TrainedModel = pickle.load(open(filename, 'rb'))
    StartInformation = [hour, day, start, line, pattern, rain, wind, temp] #pattern might need to be a string
    EndInformation = [hour, day, end, line, pattern, rain, wind, temp]
    StartPrediction = TrainedModel.predict(StartInformation)
    EndPrediction= TrainedModel.predict(EndInformation)

    return (EndPrediction[0] - StartPrediction[0])/60

