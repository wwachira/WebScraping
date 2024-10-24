# Extract Text From HTML With Regular Expressions without whitespace
import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
html_page = urlopen(url)
# The .read() method returns a byte string, so you use .decode() to decode the bytes
html_text = html_page.read().decode("utf-8") 

for string in ["Name: ", "Favorite Color:"]:
    string_start_idx = html_text.find(string)
    text_start_idx = string_start_idx + len(string)

    next_html_tag_offset = html_text[text_start_idx:].find("<")
    text_end_idx = text_start_idx + next_html_tag_offset

    raw_text = html_text[text_start_idx : text_end_idx]
    clean_text = raw_text.strip(" \r\n\t")
    print(clean_text)


