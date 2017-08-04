import urllib.request
import json
import time

api_request = "http://api.openweathermap.org/data/2.5/forecast/daily?id=2964574&APPID=e9da13ccf40ebb756a8680b64650d626"
#this can only be called every 10 mins or will get blocked, so will call every 3 hours and save as json

def getjson(api_request):
    url = urllib.request.urlopen(api_request)
    print ('request made')
    output = url.read().decode('utf-8')
    weatherjson = json.loads(output)
    url.close()
    # with open('C:/Users/Daniel/PycharmProjects/TheTouringMachines/DublinBus/TTM/static/TTM/JSON/weather.json', 'w') as outfile:
    #     json.dump(weatherjson, outfile)
    with open('/home/csstudent/DublinBus/TTM/static/TTM/JSON/weather.json', 'w') as outfile:
        json.dump(weatherjson, outfile)
    print('done')
    time.sleep(10800)


if __name__ == "__main__":
    getjson(api_request)




