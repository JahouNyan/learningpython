#Import the requests and json libraries
import requests
import json

#Ask the user for an article and strip it and replaces the spaces with underscores (_)
article = input("What wikipedia article do you want? ")
article = article.strip().replace(" ", "_")

#Format the API endpoint with the article
url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{article}"
print(article)

#Use requests.get() to get the data
r = requests.get(url)
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
print(title)
if "description" not in lines:
    print ("No Description")
else:
    print(f"The description on wikipedia is: {'description'}")
extract = lines["extract"]
print(f"The extract is: {extract}")
