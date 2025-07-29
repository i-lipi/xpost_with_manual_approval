import tweepy
import os
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

# ✅ Fetch API credentials
consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_secret = os.getenv("TWITTER_ACCESS_SECRET")
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

# ✅ Ensure API keys are loaded properly
if not consumer_key or not consumer_secret or not access_token or not access_secret:
    raise ValueError("⚠️ ERROR: Missing Twitter API keys. Check your .env file.")

# ✅ Authenticate with Tweepy Client (OAuth 2.0)
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_secret,
    bearer_token=bearer_token
)

# ✅ Function to post a tweet
def post_tweet_to_twitter(tweet_text):
    try:
        response = client.create_tweet(text=tweet_text)
        print("✅ Tweet posted successfully!")
        print("📌 Tweet ID:", response.data['id'])
        print("📝 Tweet Text:", response.data['text'])
    except tweepy.TweepyException as e:
        print(f"⚠️ Error posting tweet: {e}")

# ✅ Main function
def main():
    tweet_text = "Hello Twitter! Posting this using Tweepy with OAuth 2.0 🚀 #TwitterAPI"
    post_tweet_to_twitter(tweet_text)

# ✅ Run the script
if __name__ == "__main__":
    main()