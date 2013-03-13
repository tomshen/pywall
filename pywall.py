from settings import FEED_URL, WALLPAPER_DIRECTORY
import feedparser
import urllib.request as request
import os

def main():
    print('Reading feed...')
    feed = feedparser.parse(FEED_URL)
    if 'simpledesktops' in FEED_URL:
        print('Processing entries...')
        for entry in feed.entries:
            entry_content = entry['summary_detail']['value']
            image_url_start = entry_content.index('img src="') + len('img src="')
            image_url_end = entry_content.index('.png', image_url_start) + len('.png')
            image_url = entry_content[image_url_start:image_url_end]
            image_filepath = os.path.join(WALLPAPER_DIRECTORY, image_url[image_url.rfind('/') + 1:])
            if not os.path.exists(image_filepath):
                print('Saving ' + image_url + ' to ' + image_filepath)
                request.urlretrieve(image_url, image_filepath)
    else:
        print 'Feed currently not supported.'

if __name__ == "__main__":
    main()