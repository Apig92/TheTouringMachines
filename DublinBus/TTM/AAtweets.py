from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json
import time

# my_url = 'https://twitter.com/aaroadwatch?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
#
# uClient = uReq(my_url)
# page_html = uClient.read()
# uClient.close()
#
# page_soup = soup(page_html, "html.parser")
# content = page_soup.body.div
# containers = page_soup.findAll("div", {"class": "js-tweet-text-container"})
# tweet = containers[0].p.text
# print(containers)

def dublinornot(tweet):
    tweet_loca = tweet[:6]
    if tweet_loca == "DUBLIN":
        return True
    else:
        return False

def write_to_json(file):
    my_url = 'https://twitter.com/aaroadwatch?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    # content = page_soup.body.div
    containers = page_soup.findAll("div", {"class": "js-tweet-text-container"})
    tweet = containers[0].p.text

    with open(file) as f:
        data = json.load(f)
        if data["tweets"][-1] != tweet and dublinornot(tweet) is True:
            (data["tweets"]).append(tweet)
            with open(file, 'w') as outfile:
                json.dump(data, outfile)
    return
file = "static/TTM/JSON/AAtweets.json"
#write_to_json(file)



while (True):
    write_to_json(file)

    with open(file) as f2:
        data = json.load(f2)
        print("\n" + data["tweets"][-2])
        print(data["tweets"][-1])
    now = time.time()
    print("now is:", now)
    future = now + 60
    print("future is:", future)
    while time.time() < future:
        continue

