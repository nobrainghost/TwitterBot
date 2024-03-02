import tweepy
import time

# (Your Twitter API Credentials here)
consumer_key = "3dBuNo5M9bgpevzDk9hMUylYN"
consumer_secret = "bvLCHFMYdPxNz6gktv7gDNjntJXoc2x2fcwLM45nbaOTSkfgzG"
access_token = "1730822173055393792-i1fs681VlgMA2RdPz873CAyaEYTrgN"
access_token_secret = "nbnAve0khOUKX2466KK48kICRANej26vlXSmA4WFqjrBA"

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

# Loop to post tweets sequentially with a 10-second interval (for testing)
for i in range(0, len(tweets), 5):
  try:
    # Concatenate the next 5 lines into a single tweet
    tweet_text = "\n".join(tweets[i:i+5])

    # Post a tweet
    response = client.create_tweet(text=tweet_text)
    print(f"Tweet posted: {tweet_text}")
  except tweepy.TweepError as e:
    print(f"Error posting tweet: {e}")

  # Wait for 10 seconds before posting the next tweet (for testing)
  time.sleep(10)  # 10 seconds for testing

# Clear the tweets.txt file after all tweets are posted
with open(tweet_file_path, "w") as file:
  file.write("")  # Write an empty string to clear the file

print("All tweets posted and tweets.txt cleared!")
