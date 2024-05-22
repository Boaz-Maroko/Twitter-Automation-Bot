import tweepy
from long import api_key, api_key_secret, access_token, access_token_secret, bearer_token



# Authenticate with twitter API

# auth = tweepy.OAuth1UserHandler(
#     api_key, api_key_secret, access_token, access_token_secret
# )

client = tweepy.Client(consumer_key=api_key, 
                       consumer_secret=api_key_secret, 
                       access_token=access_token, 
                       access_token_secret=access_token_secret
)

# api = tweepy.API(auth)

# get the user's tweets

def get_user_tweets(username):
    try:
        user = client.get_user(username=username, user_fields=['id'])
        user_id = user.data.id

        tweets = client.get_users_tweets(id=user_id, tweet_fields=["created_at", "text"], max_results=100)


        # tweets = api.user_timeline(screen_name=username, count=100, tweet_mode="extended")

        if not tweets.data:
            print("No tweets were found for the user with the username {username}")
            return
        
        for tweet in tweets:
            print(f"At {tweet.created_at}, {username} said {tweet.text}")

    except tweepy.TweepyException as e:
        print(f"TweepyException Error: {e}")

    except Exception as e:
        print(f"Error {e}")
    
def main():
    username = input("Enter username to your twitter account: ")
    get_user_tweets(username)

if __name__ == "__main__":
    main()