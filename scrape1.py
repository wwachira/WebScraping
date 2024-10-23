# Extract Text From HTML With String Methods
import re
from urllib.request import urlopen

#URL Exanmples to test
# url = "http://olympus.realpython.org/profiles/aphrodite"
url = "http://olympus.realpython.org/profiles/poseidon"



page = urlopen(url)

html_bytes = page.read()

html = html_bytes.decode("utf-8")

title_index = html.find("<title>")
title_index


start_index = title_index + len("<title>")
start_index

end_index = html.find("</title>")
end_index

title = html[start_index:end_index]
title
'Profile: Aphrodite'

# Remove HTML tags (if any) using regular expressions
title = re.sub("<.*?>", "", title)  # This will remove any remaining HTML tags

print(title)
