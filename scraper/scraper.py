import snscrape.modules.twitter as sntwitter
import pandas as pd

query = 'Arima Kana'

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    print(tweet)
    break
