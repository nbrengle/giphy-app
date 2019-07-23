#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

import argparse
import webbrowser
import requests
import toolz as z

GIPHY_URL = "http://api.giphy.com/v1/gifs/search?q={}&api_key=DLCVuTK6KZExOS7JoMq82bi5MaI6EbWO&limit=1"


def main(search_key, url=GIPHY_URL):
    url = url.format(search_key)
    response = requests.get(url)
    looping = z.get_in(['data', 0, 'images', 'looping', 'mp4'], response.json())
    if looping:
        webbrowser.open(looping)


def HardcodedCompleter(**kwargs):
    """
    https://argcomplete.readthedocs.io/en/latest/

    I was hoping this would work so simply.
    At the moment it doesn't work, but it has no ill-effects.

    """
    return [
        "about"
        "above",
        "across",
        "app",
        "apple",
        "appreciate",
        "bad",
        "ball",
        "balloon",
        "bell",
        "cat",
    ]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('searchkey').completer = HardcodedCompleter

    args = parser.parse_args()
    main(args.searchkey)
