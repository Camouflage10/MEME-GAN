# Takes a scraped json file and preprocesses it for AI use
# Use in commandline:
# preprocess.py data.json

import argparse
import os
import io
import json
import requests
from PIL import Image


def download_and_scale_img(download_url):
    SCALE = (100, 100)
    r = requests.get(download_url, stream=True)
    img_bytes = r.raw.read()
    img = Image.open(io.BytesIO(img_bytes))
    scaled = img.resize(SCALE)
    return scaled


def preprocess(filename):
    # -------------
    # Load data
    # -------------

    meme_name: str
    template_url: str
    meme_data: list
    with open(filename) as f:
        data = json.load(f)
        meme_name = data["name"]
        template_url = data["template"]
        meme_data = [(meme["url"], meme["text"]) for meme in data["memes"]]
    print("Total memes:", len(meme_data))

    # -------------
    # Clean data
    # -------------

    NUM_TEXT_BLOCKS = 2
    cleaned_data = []
    for url, text in meme_data:
        # Sometimes the JSON will contain memes with no text,
        # which will give a text of: "image tagged in [categories]"
        # Don't include these samples
        if "image tagged in" in text:
            continue
        # Don't include samples that do not meet desired # of text blocks
        if len(text.split(";")) != NUM_TEXT_BLOCKS:
            continue
        cleaned_data.append((url, text))

    print("Cleaned", len(meme_data) - len(cleaned_data), "memes")
    print("Memes after cleaning:", len(cleaned_data))

    # -----------------------------
    # Export all data to folder
    # -----------------------------

    # Make directory
    output_dir = "Processed_Data" + "/"
    output_dir += "_".join(meme_name.split())
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    # Download template
    print("Getting template from", template_url)
    template = download_and_scale_img(template_url)
    template.save(output_dir + "/template.png")

    # Split urls and texts
    urls = [url for url, _ in cleaned_data]
    texts = [text for _, text in cleaned_data]

    # Save text
    print("Saving text to text.json")
    with open(output_dir + "/text.json", "w") as f:
        json.dump(texts, f)

    # Download images
    img_dir = output_dir + "/imgs"
    print("Downloading", len(urls), "images to /imgs")
    if not os.path.isdir(img_dir):
        os.makedirs(img_dir)
    for i, url in enumerate(urls):
        print(f"\rImage: {i} / {len(urls)}", end="")
        img = download_and_scale_img("https://" + url)
        img.save(img_dir + "/" + f"{i}" + ".png")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="JSON file to preprocess")
    args = parser.parse_args()

    preprocess(args.filename)
