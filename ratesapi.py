import requests
from datetime import datetime
import tweepy
import time

url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/convert"

querystring = {"from":"USD","to":"KES","amount":"1"}

headers = {
	"X-RapidAPI-Key": "be623b818cmsh7d25d2e33a15fccp15ee38jsne2bef3c5c029",
	"X-RapidAPI-Host": "currency-conversion-and-exchange-rates.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data=response.json()

status=data['success']
converted=data['query']['from']
dollar_information=data['info']['rate']
date=data['date']
time=datetime.now()
formatted_time = time.strftime("%H:%M:%S")

querystring = {"from":"EUR","to":"KES","amount":"1"}

headers = {
	"X-RapidAPI-Key": "be623b818cmsh7d25d2e33a15fccp15ee38jsne2bef3c5c029",
	"X-RapidAPI-Host": "currency-conversion-and-exchange-rates.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data=response.json()
eur_information=data['info']['rate']


querystring = {"from":"BTC","to":"USD","amount":"1"}

headers = {
	"X-RapidAPI-Key": "be623b818cmsh7d25d2e33a15fccp15ee38jsne2bef3c5c029",
	"X-RapidAPI-Host": "currency-conversion-and-exchange-rates.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data=response.json()
btc_information=data['info']['rate']


querystring = {"from":"JPY","to":"KES","amount":"1"}

headers = {
	"X-RapidAPI-Key": "be623b818cmsh7d25d2e33a15fccp15ee38jsne2bef3c5c029",
	"X-RapidAPI-Host": "currency-conversion-and-exchange-rates.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data=response.json()
yen_information=data['info']['rate']


tweet=f"Forex Rates {date}, {formatted_time}\n 1 USD = {dollar_information} KES\n 1 EUR = {eur_information} KES\n 1 JP YEN = {yen_information} KES\n 1 BTC = {btc_information} USD"
print (tweet)
with open('forex_rates.txt', 'a') as f:
    f.write(tweet)
    f.write('\n')
    print("Data updated for Forex Rates")

consumer_key = "3dBuNo5M9bgpevzDk9hMUylYN"
consumer_secret = "bvLCHFMYdPxNz6gktv7gDNjntJXoc2x2fcwLM45nbaOTSkfgzG"
access_token = "1730822173055393792-i1fs681VlgMA2RdPz873CAyaEYTrgN"
access_token_secret = "nbnAve0khOUKX2466KK48kICRANej26vlXSmA4WFqjrBA"


client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

tweet_file_path = "forex_rates.txt"


def read_tweets_without_blanks():
  """
  Reads tweets from the file, removes blank lines, and returns a list.
  """
  with open(tweet_file_path, "r") as file:
    tweets = file.readlines()
  return [tweet.strip() for tweet in tweets if tweet.strip()]  # Filter blank lines

tweet=read_tweets_without_blanks()

for i in range(0, len(tweet), 5):
  try:
   
    tweet_text = "\n".join(tweet[i:i+5])

    
    response = client.create_tweet(text=tweet_text)
    print(f"Tweet posted: {tweet_text}")
  except tweepy.TweepError as e:
    print(f"Error posting tweet: {e}") 


with open(tweet_file_path, "w") as file:
  file.write("") 

print("All is well. Voila!")