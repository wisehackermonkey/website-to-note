# website-to-note
# simple python app that giving a url from the clipboard scrapes a web page for its title and returns a useful information for use in docs, notetaking apps, etc.
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20200420
import requests
import pyperclip
import validators
from newsplease import NewsPlease

from dateformate import current_date

# scrape url for title
def get_website_title(url):
    title = ""
    response = NewsPlease.from_url(url)
    title = response.title
    return title

def main():
    clipboard_url = pyperclip.paste()


    #check if the clipboard has a url 

    if not validators.url(clipboard_url):
        print("Clipboard Does not contain a URL")
        return -1
   
    result = f"""
{get_website_title(clipboard_url)}
{clipboard_url}
{current_date()}
"""
    print(result)
    pyperclip.copy(result)


if __name__ == "__main__":
    print("website-to-note by oran collins 20200420")
    main()