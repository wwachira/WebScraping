# Extract Text From HTML With String Methods
from urllib.request import urlopen


url = "http://olympus.realpython.org/profiles/aphrodite"
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


print(title)
