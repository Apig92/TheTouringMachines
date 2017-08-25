from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json
import time
from datetime import datetime, timedelta

# function that check if the tweet is about Dublin or not
def dublinornot(tweet):
    tweet_loca = tweet[:7]
    if tweet_loca == "#DUBLIN":
        return True
    else:
        return False

# function that convert the US time to Ireland time
def timeconvert(time_was):
    time_format = '%I:%M %p - %d %b %Y'
    my_date = datetime.strptime(time_was, time_format)
    time_now = my_date + timedelta(hours=8)
    time_now = time_now.strftime(time_format)
    return time_now

# function that get the latest tweet and write it to AAtweets.json
def write_to_AAjson(file):
    my_url = 'https://twitter.com/aaroadwatch?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class": "js-tweet-text-container"})
    times = page_soup.findAll("a", {"class": "tweet-timestamp js-permalink js-nav js-tooltip"})

    for i in range(len(containers) - 1, -1, -1):
        timestamp = timeconvert(times[i]['title'])
        text = containers[i].p.text
        tweet = timestamp + ", " + text
        with open(file) as f:
            data = json.load(f)
            if tweet not in data["tweets"] and dublinornot(text) is True:
                print("found one: ", tweet)
                (data["tweets"]).append(tweet)
                with open(file, 'w') as outfile:
                    json.dump(data, outfile)
    return

# function that get the latest tweet and write it to DublinBus tweets json
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
        with open(file) as f:
            data = json.load(f)
            if tweet not in data["tweets"]:
                print("found one: ", tweet)
                (data["tweets"]).append(tweet)
                with open(file, 'w') as outfile:
                    json.dump(data, outfile)
    return

# to re-scraped AA tweets and DB tweets every minute, and print the last two tweets.
while (True):
    write_to_AAjson("/home/csstudent/DublinBus/TTM/static/TTM/JSON/AAtweets.json")
    write_to_DBjson("/home/csstudent/DublinBus/TTM/static/TTM/JSON/DBtweets.json")

    with open("/home/csstudent/DublinBus/TTM/static/TTM/JSON/AAtweets.json") as f1:
        data1 = json.load(f1)
        print("\nAA: \n" + data1["tweets"][-2])
        print(data1["tweets"][-1])
    with open("/home/csstudent/DublinBus/TTM/static/TTM/JSON/DBtweets.json") as f2:
        data2 = json.load(f2)
        print("DB: \n" + data2["tweets"][-2])
        print(data2["tweets"][-1])
    now = time.time()
    print("now is:", now)
    future = now + 600
    print("future is:", future)
    while time.time() < future:
        continue