import json
import praw
import os
from dotenv import load_dotenv


load_dotenv()


REDDIT_API_CLIENT_ID = os.getenv("REDDIT_API_CLIENT_ID")
REDDIT_API_SECRET = os.getenv("REDDIT_API_SECRET")

def fetch_reddit_post():
    reddit = praw.Reddit(
        client_id=REDDIT_API_CLIENT_ID,
        client_secret=REDDIT_API_SECRET,
        user_agent="tts-video-bot"
    )
    for post in reddit.subreddit("AmItheAsshole").hot(limit=100):
        print(f"Title: {post.title}\nBody length: {len(post.selftext)}")
        if not post.stickied and post.selftext.strip() and len(post.selftext) < 1000:
            return (post.title, post.selftext)
        
    
            


