'''
Ryan Lim
Python Programming
Concept: JSON Parsing
'''

#modules
from urllib.request import urlopen
import json

total = 0

#prompt the user for a url, open the url, then read in and parse the JSON
user_input = input("Enter in a url, and this program will parse the JSON: ")
url = urlopen(user_input)
data = url.read()
string_data = str(data, encoding="UTF-8")
info = json.loads(string_data)

#sum up the comment counts
for counter in info["comments"]:
    total = total + counter["count"]

print(total)
