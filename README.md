### Learning outcomes
Request a web page using Python’s built-in urllib module
Parse HTML using Beautiful Soup
Interact with web forms using MechanicalSoup
Repeatedly request data from a website to check for updates

### Command Run
python scrape.py

The output you’re seeing is the HTML code of the website.

### terminal
git init
git add .
git commit -m "..."
git remote add origin https://github.com/your_username/filename
git push -u origin main(it can bemaster depending on which branch you're @)

### Extracting Source code
from urllib.request import urlopen


url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)

<!-- page
# <http.client.HTTPResponse object at 0x105fef820> -->
html_bytes = page.read()

html = html_bytes.decode("utf-8")
print(html)

