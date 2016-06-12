'''
Ryan Lim
Python Programming
Concept: Using APIs
'''

#module
import urllib.parse
from urllib.request import urlopen
import json

#url for api
service_url = "http://maps.googleapis.com/maps/api/geocode/json?"

#ask user to enter in a location, then make a call to an API to get the place id
while True:
    location = input("Enter in a location: ")
    if len(location) < 1:
        break

    url_encoding = service_url + urllib.parse.urlencode({'sensor':'false', 'address': location})
    print("Retrieving:", url_encoding)
    url = urlopen(url_encoding)
    data = url.read()
    encoded_data = str(data, encoding='UTF-8')
    print("Retrieved", len(encoded_data), "characters")

    #exception handling
    try: js = json.loads(encoded_data)
    except: js = None

    id = js["results"][0]["place_id"]
    print("Place ID:", id)





