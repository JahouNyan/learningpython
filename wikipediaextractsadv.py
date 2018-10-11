#Import the requests and json libraries
import requests
import json


#Ask the user for an article and strip it and replaces the spaces with underscores (_)
article = input("What wikipedia article do you want? ")
article = article.strip().replace(" ", "_")
language = input("select your language: en, af or fr: ")


# list language choices
en = "https://en.wikipedia.org/api/rest_v1/page/summary/"
af = "https://af.wikipedia.org/api/rest_v1/page/summary/"
fr = "https://fr.wikipedia.org/api/rest_v1/page/summary/"

#Format the API endpoint with the article
searcharticle = (language) + article
#Use requests.get() to get the data
r = requests.get(searcharticle)
print(r)

#Check if we got a 200 status code, otherwise abort the program
if r.status_code is 200:
    print("ok")
        
else:
    print ("error")
    exit()

#Display the title of the article, description and extract
lines = r.text
lines = json.loads(lines)

title = lines["title"]
description = lines["description"]
extract = lines["extract"]
print(title)
#some articles don't habe descriptions so:
if description not in lines:
    print ("No Description")
else:
    print(f"The description on wikipedia is: {description}")
print(f"The extract is: {extract}")

#show the description and extract in three languages of your choice e.g 'en', 'es', 'nl', etc.)

