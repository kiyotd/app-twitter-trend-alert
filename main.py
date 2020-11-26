import datetime
import time

import tweepy
from plyer import notification
from tweepy import OAuthHandler

import settings

# 監視したいキーワードのリスト
words = ["GitHub", "AWS", "Slack", "Gmail", "障害"]

auth = OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_SECRET)

api = tweepy.API(auth)

lower_words = list(map(str.lower, words))

print("Start monitoring trends")
print(words)

hit_words = []

while True:

    now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")

    trends = api.trends_place(23424856)[0]["trends"]

    for i, trend in enumerate(trends):

        rank = i + 1
        lower_name = str.lower(trend["name"])

        for _ in lower_words:
            if _ in lower_name:
                if trend['name'] not in hit_words:
                    hit_words.append(trend['name'])
                    print(f"{now} [{rank}位] {trend['name']}")

                    notification.notify(
                        title=f"{trend['name']}",
                        message=f"{rank}位",
                    )
        hit_words = []

    time.sleep(60)
