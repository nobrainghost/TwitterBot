import tweepy
import time

# Set your Twitter API credentials. Get these from the developer portal


# Initialize the Twitter client
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
client = tweepy.Client(auth=auth)

# Path to the text file containing tweets
tweet_file_path = "tweets.txt"

# Read tweets from the text file into a list
with open(tweet_file_path, "r") as file:
    tweets = file.readlines()

# Remove any leading or trailing whitespace and join multiline tweets
tweets = [tweet.strip() for tweet in tweets]
tweets = [" ".join(tweet.splitlines()) for tweet in tweets]

# Loop to post tweets sequentially with a 30-minute interval
for tweet_text in tweets:
    try:
        # Post a tweet
        response = client.create_tweet(text=tweet_text)
        print(f"Tweet posted: {tweet_text}")
    except tweepy.error.TweepError as e:
        print(f"Error posting tweet: {e}")
    
    # Wait for 30 minutes before posting the next tweet
    time.sleep(0.3 * 60)  # 30 minutes in seconds
