'''
Ryan Lim
Web Crawler
'''

import requests
from bs4 import BeautifulSoup

'''
 Web Crawler
This web crawler will crawl through the
main site and get all the urls of the scripts
'''

def main_spider(url):
    # get the source code from the url
    source_code = requests.get(url)
    #convert source code to plain text
    plain_text = source_code.text
    #convert plain text to Beautiful Soup Object
    soup = BeautifulSoup(plain_text,"html.parser")
    #use a file object to open up a file to write to
    file_object = open("Data_Mining.txt", "w")
    '''
    loop through the website and get all the src websites,
    write them to the file, and then output them
    '''
    for script in soup.findAll("script", {"type":"text/javascript"}):
        src = script.get("src")
        file_object.write(str(src) + "\n")
        print(src)
    file_object.close()

#test out exception handling
while True:
    try:
        user_url = str(input("What website would you like to mine data from? Enter a url: "))
        main_spider(user_url)
    except ValueError:
        print("Please make sure to enter in a url as a string")
    except:
        print("Error. Please try again")
    finally:
        print("Ta Da!")