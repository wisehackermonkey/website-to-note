# website-to-note
# simple python app that giving a url from the clipboard scrapes a web page for its title and returns a useful information for use in docs, notetaking apps, etc.
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20200420

import pyperclip
import validators
from newsplease import NewsPlease

from dateformate import current_date

def main():
    clipboard = pyperclip.paste()


    #check if the clipboard has a url 

    if not validators.url(clipboard):
        print("Clipboard Does not contain a URL")
        return -1

    # scrape url for title
    article = NewsPlease.from_url(clipboard)
    
    result = f"""{article.title}{current_date()}{clipboard}"""
    print(result)


if __name__ == "__main__":
    print("website-to-note by oran collins 20200420")
    main()