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
    pattern = int(dict['routeindex'])
    line = dict['line']
    wind = float(dict['wind'])
    temp = float(dict['temp'])
    rain= float(dict['rain'])
    filename = '/home/csstudent/DublinBus/TTM/static/TTM/pickles/'+line+'.sav'
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
    seconds = (EndPrediction[0] - StartPrediction[0])
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return ("%d hrs %02d mins %02d secs" % (h, m, s))
