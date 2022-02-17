import os
import praw
import ImageDownloader
from dotenv import load_dotenv


def scrape_subreddit(subreddit_name):
    load_dotenv()
    id = os.getenv("reddit_scrape_client_id")
    agent = os.getenv("reddit_scrape_user_agent")
    secret = os.getenv("reddit_scrape_secret")

    reddit_reader = praw.Reddit(
        client_id=id,
        user_agent=agent,
        client_secret=secret,
    )

    subreddit = reddit_reader.subreddit(subreddit_name)

    print("Getting urls...")
    urls = []
    for submission in subreddit.hot(limit=20):
        urls.append(submission.url)

    for url in urls:
        print(url)

    print("Downloading...")
    # downloads all .jpg files scraped
    for url in urls:
        if ".jpg" in url:
            ImageDownloader.download_image(url, "images/")


def main():
    SUBREDDIT = "AdviceAnimals"
    scrape_subreddit(SUBREDDIT)
    # scrape_subreddit(input("Subreddit to scrape: ")) # User input


if __name__ == "__main__":
    main()
