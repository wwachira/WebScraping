# Use an HTML Parser for Web Scraping in Python using (BeautifulSoup)
# beauty_soup.py
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser") # this creates a BeautifulSoup object and assigns it to the soup variable


# print Scraping data tags examples
# print(soup.get_text())
print(soup.find_all("img"))