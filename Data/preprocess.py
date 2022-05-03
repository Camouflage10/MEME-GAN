# Takes a scraped json file and preprocesses it for AI use
# Use in commandline:
# preprocess.py data.json

import argparse
import os
import io
import json
import requests
from PIL import Image


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
    print(meme_data[:5])

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

    print("Removed", len(meme_data) - len(cleaned_data), "memes")
    print("Memes after cleaning:", len(cleaned_data))

    # -----------------------------
    # Download and scale template
    # -----------------------------

    # Download template
    print("Getting template from", template_url)
    r = requests.get(template_url, stream=True)
    img_bytes = r.raw.read()

    # Scale to size
    image = Image.open(io.BytesIO(img_bytes))
    print("Image size before:", image.size)
    scaled = image.resize((100, 100))
    print("Image size after:", scaled.size)

    # -----------------------------
    # Export all data to folder
    # -----------------------------

    output_folder = "Processed_Data" + "/"
    output_folder += "_".join(meme_name.split())
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)

    print("Saving files to", output_folder)
    scaled.save(output_folder + "/" + "image.jpg")
    with open(output_folder + "/" + "data.json", "w") as f:
        json.dump(cleaned_data, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="JSON file to preprocess")
    args = parser.parse_args()

    preprocess(args.filename)
