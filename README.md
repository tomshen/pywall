# PyWall
Downloads new wallpapers from a RSS/Atom feed to a directory of your choosing.

Currently only supports [Simple Desktops](http://simpledesktops.com/).

## Requirements
* Python 3
* [feedparser](https://pypi.python.org/pypi/feedparser)

## Setup
1. Clone the repo.
2. Change `WALLPAPER_DIRECTORY` to the directory where you want to store your downloaded wallpapers.
3. (Optional) Set up a virtualenv in `venv`.
4. `pip install feedparser`
5. If you are using a virtualenv, run one of the `.bat` or `.sh` scripts. Otherwise, just run the `.py` file to download wallpapers.
6. (Optional) Set your OS to monitor the download directory for new wallpapers.