# website-to-note
# simple python app that giving a url from the clipboard scrapes a web page for its title and returns a useful information for use in docs, notetaking apps, etc.
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20200420
import requests
import pyperclip
import validators
# script for getting the date in format yyyymmdd for easy use
from dateformate import current_date

# scrape url for title
# credit goes to this stackoverflow post
# https://stackoverflow.com/questions/51233/how-can-i-retrieve-the-page-title-of-a-webpage-using-python
def get_website_title(url):
    if not url:
        print("no url givin")
        return -1
    hearders = {'headers':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    
    n = requests.get(url, headers=hearders) 
    al = n.text; 
     
    title = al[al.find('<title>') + 7 : al.find('</title>')]
    return title

def main():
    # grab the contents of the clipboard
    clipboard_url = pyperclip.paste()


    #check if the clipboard has a url 

    if not validators.url(clipboard_url):
        print("Clipboard Does not contain a URL")
        return -1

    # format the title, url, and date for the website in a string
    result = f"""
{get_website_title(clipboard_url)}
{clipboard_url}
{current_date()}
"""
    print(result)

    #copy result back into clipboard
    pyperclip.copy(result)


if __name__ == "__main__":
    print("website-to-note by oran collins 20200420")
    # start of the program
    main()