import pandas as pd
import json
import os


def read(filename):
    df = pd.read_csv(filename, low_memory=False)
    df['JourneyPatternID'] = df['JourneyPatternID'].astype('category')
    df['Pattern'] = df.JourneyPatternID.cat.codes
    return df


def PatternJson(df,dictionary):
    patterns = df.JourneyPatternID.unique()
    indexes = df.Pattern.unique()
    for i in range (len(patterns)):
        dictionary[patterns[i]]= int(indexes[i])
        print(patterns[i]," index: ",indexes[i])


def main():
    directory = '/home/csstudent/AllLines'
    dictionary={}
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            x = "" + filename + ""
            df = read(x)
            PatternJson(df,dictionary)

    with open('indexes.json', 'w') as outfile:
        json.dump(dictionary, outfile)

main()






