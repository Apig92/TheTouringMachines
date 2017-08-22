from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json
import time
from datetime import datetime, timedelta

def dublinornot(tweet):
    tweet_loca = tweet[:6]
    if tweet_loca == "DUBLIN":
        return True
    else:
        return False

def timeconvert(time_was):
    time_format = '%I:%M %p - %d %b %Y'
    my_date = datetime.strptime(time_was, time_format)
    time_now = my_date + timedelta(hours=8)
    time_now = time_now.strftime(time_format)
    return time_now

my_url = 'https://twitter.com/aaroadwatch?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
content = page_soup.body.div
containers = page_soup.findAll("div", {"class": "js-tweet-text-container"})
times = page_soup.findAll("a", {"class": "tweet-timestamp js-permalink js-nav js-tooltip"})

for i in range(len(containers)-1, -1, -1):
    timestamp = timeconvert(times[i]['title'])
    text = containers[i].p.text
    tweet = timestamp + ", " + text
    with open("static/TTM/JSON/AAtweets.json") as f:
        data = json.load(f)
        if tweet not in data["tweets"] and dublinornot(text) is True:
            print("found one: ", tweet)
            (data["tweets"]).append(tweet)
            with open("static/TTM/JSON/AAtweets.json", 'w') as outfile:
                json.dump(data, outfile)

def write_to_AAjson(file):
    my_url = 'https://twitter.com/aaroadwatch?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class": "js-tweet-text-container"})
    timestamp = timeconvert(times[0]['title'])
    text = containers[0].p.text
    tweet = timestamp + ", " + text

    with open(file) as f:
        data = json.load(f)
        if data["tweets"][-1] != tweet and dublinornot(text) is True:
            (data["tweets"]).append(tweet)
            with open(file, 'w') as outfile:
                json.dump(data, outfile)
    return

def write_to_DBjson(file):
    my_url = 'https://twitter.com/dublinbusnews?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class": "js-tweet-text-container"})
    people = page_soup.findAll("span", {"class": "FullNameGroup"})
    times = page_soup.findAll("a", {"class": "tweet-timestamp js-permalink js-nav js-tooltip"})

    for i in range(len(containers)-1, 0, -1):
        timestamp = timeconvert(times[i]['title'])
        person = people[i].strong.text
        text = containers[i].p.text
        tweet = timestamp + ", " + person + ": " + text
        with open("static/TTM/JSON/DBtweets.json") as f:
            data = json.load(f)
            if tweet not in data["tweets"]:
                print("found one: ", tweet)
                (data["tweets"]).append(tweet)
                with open("static/TTM/JSON/DBtweets.json", 'w') as outfile:
                    json.dump(data, outfile)
    return


while (True):
    write_to_AAjson("static/TTM/JSON/AAtweets.json")
    write_to_DBjson("static/TTM/JSON/DBtweets.json")

    with open("static/TTM/JSON/AAtweets.json") as f1:
        data1 = json.load(f1)
        print("\nAA: \n" + data1["tweets"][-2])
        print(data1["tweets"][-1])
    with open("static/TTM/JSON/DBtweets.json") as f2:
        data2 = json.load(f2)
        print("DB: \n" + data2["tweets"][-2])
        print(data2["tweets"][-1])
    now = time.time()
    print("now is:", now)
    future = now + 60
    print("future is:", future)
    while time.time() < future:
        continue

