# # mech_soup.py
# import time
# import mechanicalsoup

# # Create a StatefulBrowser instance
# browser = mechanicalsoup.StatefulBrowser()

# # Open the dice roll page
# for i in range(4):
#     browser.open("http://olympus.realpython.org/dice")

# # Select the result element by its id
# tag = browser.page.select("#result")[0]
# result = tag.text

# print(f"Roll {i + 1}: The result of your dice roll is: {result}")

# if i < 3:
#     time.sleep(10)
# # print(result)

# give periodic updates in the terminal, (you can set up a code for updates after 24hours eg for news)
import time
import mechanicalsoup

# Create a StatefulBrowser instance
browser = mechanicalsoup.StatefulBrowser()

# Loop to roll the dice 4 times with periodic updates
for i in range(4):
    # Open the dice roll page
    browser.open("http://olympus.realpython.org/dice")
    
    # Select the result element by its id
    tag = browser.page.select("#result")[0]
    result = tag.text
    
    # Print the result of the current roll
    print(f"Roll {i + 1}: The result of your dice roll is: {result}")
    
    # Sleep for 10 seconds between rolls (except after the last roll)
    if i < 3:
        time.sleep(10)
