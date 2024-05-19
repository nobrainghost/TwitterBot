import tweepy
import time
import requests


# List of URLs to fetch data from
urls = [
    "https://nairobi-stock-exchange-nse.p.rapidapi.com/stocks/Absa Bank Kenya Plc",
    "https://nairobi-stock-exchange-nse.p.rapidapi.com/stocks/Safaricom",
    "https://nairobi-stock-exchange-nse.p.rapidapi.com/stocks/KCB Group Limited",
    "https://nairobi-stock-exchange-nse.p.rapidapi.com/stocks/Equity Group Holdings Limited",
    "https://nairobi-stock-exchange-nse.p.rapidapi.com/stocks/Co-operative Bank of Kenya Limited",
    "https://nairobi-stock-exchange-nse.p.rapidapi.com/stocks/Kenya Power & Lighting Company",
    # Add more URLs here as needed
]

# Common headers for all requests
headers = {
    "X-RapidAPI-Key": "be623b818cmsh7d25d2e33a15fccp15ee38jsne2bef3c5c029",
    "X-RapidAPI-Host": "nairobi-stock-exchange-nse.p.rapidapi.com"
}

# Open tweets.txt file in append mode
with open('tweets.txt', 'a') as f:
    # Loop through each URL
    for url in urls:
        # Fetch data from the URL
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            if data:
                item = data[0]
                stock_name = item.get('name')
                volume = item.get('volume')
                price = item.get('price')
                change = item.get('change')

                # Format the tweet-like string
                tweet = f"Company: {stock_name}\nStock Name: {stock_name}\nVolume: {volume}\nPrice: {price}\nChange: {change}\n\n"

                # Write the tweet to tweets.txt file
                f.write(tweet)
                f.write('\n')
                print("Data updated for:", stock_name)
            else:
                print("No data found in response:", url)
        else:
            print("Failed to fetch data from:", url)

# (Your Twitter API Credentials here)
consumer_key = ""
consumer_secret = ""
access_token = "-"
access_token_secret = ""

# Initialize the Twitter client
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Path to the text file containing tweets
tweet_file_path = "tweets.txt"


def read_tweets_without_blanks():
  """
  Reads tweets from the file, removes blank lines, and returns a list.
  """
  with open(tweet_file_path, "r") as file:
    tweets = file.readlines()
  return [tweet.strip() for tweet in tweets if tweet.strip()]  # Filter blank lines


# Read tweets and remove blanks
tweets = read_tweets_without_blanks()

for i in range(0, len(tweets), 5):
  try:
   
    tweet_text = "\n".join(tweets[i:i+5])

    
    response = client.create_tweet(text=tweet_text)
    print(f"Tweet posted: {tweet_text}")
  except tweepy.TweepError as e:
    print(f"Error posting tweet: {e}")

  
  time.sleep(10)  


with open(tweet_file_path, "w") as file:
  file.write("")  # Write an empty string to clear the file

print("All tweets posted and tweets.txt cleared!")
