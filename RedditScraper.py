import os
import praw
from dotenv import load_dotenv

from urllib.request import urlretrieve

SUBREDDIT_NAME = "memes"


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
            splt = url.split("/")
            file_name = splt[len(splt) - 1]  # gets name of file
            download_image(url, "images/", file_name)


# Uses urllib to download images from a url
def download_image(url, file_path, file_name):
    full_path = file_path + file_name
    urlretrieve(url, full_path)


def main():
    scrape_subreddit(SUBREDDIT_NAME)


if __name__ == "__main__":
    main()
