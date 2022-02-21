# Adapted from https://gist.github.com/WalterSimoncini/defca6de456bb168ada303085358bf0a

"""
imgflip.com scraper

This script scrapes memes from a category on imgflip.com
(e.g. https://imgflip.com/meme/Bird-Box). As an example,
to scrape the first 10 pages of Bird Box memes run:

python imgflip_scraper.py --source https://imgflip.com/meme/Bird-Box --pages 10

The program outputs the memes as a JSON file with the following format:

{
    "name": "Bird Box",
    "memes": [{
        "url": "i.imgflip.com/40y9fr.jpg",
        "text": "YOU CAN'T GET CORONA; IF YOU CAN'T SEE IT"
    }, ...]
}
"""

import time
import json
import argparse
import requests
from bs4 import BeautifulSoup


def info_from_file(filename):
    with open(filename) as f:
        data = json.load(f)
        urls, texts = get_JSON_info(data)
        return urls, texts


def get_JSON_info(json):
    urls = []
    texts = []
    for meme in json["memes"]:
        # Sometimes the JSON will contain memes with no text
        # In this instance it will give a text of: "image tagged in [categories]"
        # We do not include these memes in our lists
        if "image tagged in" not in meme["text"]:
            urls.append(meme["url"])
            texts.append(meme["text"])

    return urls, texts


# Scrapes a meme template from Imgflip
# source: link to meme template
# from_page: which page to start on
# pages: number of pages to scrape
# delay: delay between page loads
def scrape(source, from_page, pages, delay):
    fetched_memes = []

    meme_name = source.split("/")[-1].replace("-", " ")
    output_filename = source.split("/")[-1].replace("-", "_").lower() + ".json"

    for i in range(from_page, pages + 1):
        print(f"Processing page {i}")
        response = requests.get(f"{source}?page={i}")
        body = BeautifulSoup(response.text, "html.parser")

        if response.status_code != 200:
            # Something went wrong (e.g. page limit)
            break

        memes = body.findAll("div", {"class": "base-unit clearfix"})

        for meme in memes:
            if "not-safe-for-work images" in str(meme):
                # NSFW memes are available only to logged in users
                continue

            meme_text = meme.find("img", {"class": "base-img"})["alt"]
            meme_text = meme_text.split("|")[1].strip()

            rows = meme_text.split(";")

            meme_data = {
                "url": meme.find("img", {"class": "base-img"})["src"][2:],
                "text": meme_text,
            }

            fetched_memes.append(meme_data)

        time.sleep(delay)

    print(f"Fetched: {len(fetched_memes)} memes")

    with open(output_filename, "w") as out_file:
        data = {"name": meme_name, "memes": fetched_memes}

        out_file.write(json.dumps(data))


def main():
    parser = argparse.ArgumentParser(description="Scrape memes from imgflip.com")
    parser.add_argument(
        "--source",
        required=True,
        help="Memes list url (e.g. https://imgflip.com/meme/Bird-Box)",
        type=str,
    )
    parser.add_argument(
        "--from_page",
        default=1,
        help="Initial page",
        type=int,
    )
    parser.add_argument(
        "--pages",
        required=True,
        help="Maximum page number to be scraped",
        type=int,
    )
    parser.add_argument(
        "--delay",
        default=2,
        help="Delay between page loads (seconds)",
        type=int,
    )

    args = parser.parse_args()

    source = args.source
    from_page = args.from_page
    pages = args.pages
    delay = args.delay

    scrape(source, from_page, pages, delay)


if __name__ == "__main__":
    main()
