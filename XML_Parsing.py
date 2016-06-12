'''
Ryan Lim
Python Programming
Concept: XML Parsing
'''

# modules
from urllib.request import urlopen
import bs4 as bs

total = 0

# ask user for a url, open the url, read the data, and then parse the xml
user_input = input( "Enter a url and this program will parse the xml: " )
url = urlopen(user_input)
data = url.read()
soup = bs.BeautifulSoup(data, "xml")
for count in soup.findAll("count"):
    single_count = count.text
    int_count = int(single_count)
    total = total + int_count

print(total)
