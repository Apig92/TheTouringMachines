import pandas as pd
import numpy as np
import os
from sklearn.ensemble import RandomForestRegressor
import pickle
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoSite.settings'
django.setup()
from DublinBus.settings import BASE_DIR

from django.conf import settings
#from .models import routes, stops

def predictions(dict):
    hour = int(dict['time'])
    day = int(dict['date'])
    start = int(dict['start'])
    end = int(dict['stop'])
    temp = float(dict['temp'])
    rain = float(dict['rain'])
    pattern = dict['route']
    line = dict['nameroute']
    wind = dict['wind']
    #return (dict)
    filename = os.path.join(BASE_DIR, 'TTM\static\TTM\pickles\\'+line+'.sav')
    # return dict
    if os.path.isfile(filename):
        print ('filefound')
    else:
        return ('Pickle not found')
    #return (dict)
    TrainedModel = pickle.load(open(filename, 'rb'))
    StartInformation = [hour, day, start, line, pattern, rain, wind, temp] #pattern might need to be a string
    EndInformation = [hour, day, end, line, pattern, rain, wind, temp]
    StartPrediction = TrainedModel.predict(StartInformation)
    EndPrediction= TrainedModel.predict(EndInformation)

    return (EndPrediction[0] - StartPrediction[0])/60



