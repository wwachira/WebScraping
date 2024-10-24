### Learning outcomes
### Author: W. Wachira, Liz
Request a web page using Python’s built-in urllib module
Parse HTML using Beautiful Soup
Interact with web forms using MechanicalSoup
Repeatedly request data from a website to check for updates
https://realpython.com/python-web-scraping-practical-introduction/ 
https://realpython.com/what-is-pip/
http://learn-co-curriculum.github.io/site-for-scraping/courses

### Command Run
python scrape.py

The output you’re seeing is the HTML code of the website.

### terminal
git init
git add .
git commit -m "..."
git remote add origin https://github.com/your_username/filename
git push -u origin main(it can bemaster depending on which branch you're @)

### 1. Extracting Source code (scrape)
### 2. Extract Text From HTML With String Methods (scrape1)
### 3. Extract Text From HTML With Regular Expressions (scrape2)
### 4. Extract Text From HTML With Regular Expressions without whitespace (scrape3)
### 5. Use an HTML Parser for Web Scraping in Python (BeautifulSoup) (scrape4)
To install Beautiful Soup, you can run the following in your terminal:
 python -m pip install beautifulsoup4
 - soup.title.string: This directly extracts the text inside the <title> tag. - BeautifulSoup automatically removes the HTML tags.
 - You can extract other elements from the HTML with ease by using various BeautifulSoup methods (find, find_all, etc.).
 ### 6. Interact With HTML Forms (MechanicalSoup) (scrape5,6)
Always install inside your virtual environment when working on a specific project, so that dependencies are isolated from your global Python environment.
python -m pip install --upgrade pip
python -m venv venv\  (you can use this too: pipenv shell)
venv\Scripts\activate.bat - optional
python -m pip install MechanicalSoup (You can install in the Virtual Env (venv)).

# Python has the built-in venv module for creating virtual environments. 
The parentheses (()) surrounding your venv name indicate that you successfully activated the virtual environment. 
eg... 
(venv) PS>  pip3 --version
(venv) PS>  pip --version

## To leave or deactivate a virtual environment, you can simply run the following command in your terminal:
deactivate
### 7. Interact With Websites in Real Time (scrape6)
Important: Most websites publish a Terms of Use document. You can often find a link to it in the website’s footer.
Failure to comply with the Terms of Use could result in your IP being blocked, so be careful!

## PLEASE NOTE:
With techniques like this, you can scrape data from websites that periodically update their data. However, you should be aware that requesting a page multiple times in rapid succession can be seen as suspicious, or even malicious, use of a website.

