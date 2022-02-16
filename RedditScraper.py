import os
import praw
from dotenv import load_dotenv


SUBREDDIT_NAME = "memes"


def scrape_subreddit(subreddit):
    load_dotenv()
    id = os.getenv("reddit_scrape_client_id")
    agent = os.getenv("reddit_scrape_user_agent")
    secret = os.getenv("reddit_scrape_secret")

    reddit_reader = praw.Reddit(
        client_id=id,
        user_agent=agent,
        client_secret=secret,
    )

    subreddit = reddit_reader.subreddit(SUBREDDIT_NAME)

    urls = []
    for submission in subreddit.hot(limit=5):
        urls.append(submission.url)

    for url in urls:
        print(url)


def main():
    scrape_subreddit(SUBREDDIT_NAME)


if __name__ == "__main__":
    main()
