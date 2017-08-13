import pandas as pd
import json
import os
import sys

def read(filename):
    dtype_dic = {'JourneyPatternID': str}
    df = pd.read_csv(filename, low_memory=False, dtype=dtype_dic)
    df['JourneyPatternID'] = df['JourneyPatternID'].astype('category')
    df['Pattern'] = df.JourneyPatternID.cat.codes
    df['JourneyPatternID'] = df['JourneyPatternID'].astype('str')
    return df


def PatternJson(df,dictionary):
    patterns = df.JourneyPatternID.unique()
    indexes = df.Pattern.unique()
    print('Number of patterns',len(patterns))
    print('Number of indexes', len(indexes))

    for i in range (len(patterns)):
        if len(patterns[i])==8:
            dictionary[str(patterns[i])]= int(indexes[i])
            print(patterns[i]," index: ",indexes[i])
        elif len(patterns[i])==7:
            patterns[i]='0'+patterns[i]
            dictionary[str(patterns[i])] = int(indexes[i])
            print(patterns[i], " index: ", indexes[i])
        elif len(patterns[i])==6:
            patterns[i]='00'+patterns[i]
            dictionary[str(patterns[i])] = int(indexes[i])
            print(patterns[i], " index: ", indexes[i])


if __name__ == "__main__":
    directory = '/home/csstudent/MergedWeather'
    dictionary={}
    f = open('patternResults.txt', 'w')     #Creates .txt file where all the model information and stats are contained
    orig_stdout = sys.stdout  # Original output, the terminal
    sys.stdout = f
    for filename in os.listdir(directory):
        if filename.endswith("weather.csv"):
            x = "" + filename + ""
            df = read(x)
            print('_______________________________________________________')
            print("Working on",x)
            PatternJson(df,dictionary)

    with open('indexes.json', 'w') as outfile:
        json.dump(dictionary, outfile)
    sys.stdout = orig_stdout  # Change output back to terminal
    f.close()








