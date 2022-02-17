import requests


def download_images(urls, destination):
    for url in urls:
        download_image(url, destination)


def download_image(url, destination):
    # gets name of file from url
    splt = url.split("/")
    file_name = splt[len(splt) - 1]
    full_path = destination + file_name

    # download and save
    r = requests.get(url)
    with open(full_path, "wb") as outfile:
        outfile.write(r.content)
