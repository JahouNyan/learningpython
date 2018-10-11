#Import the requests and json libraries
import requests
import json

#Ask the user for an article and strip it and replaces the spaces with underscores (_)
article = input("What wikipedia article do you want? ")
article = article.strip().replace(" ", "_")
# list language choices
languages = {
    "en" : "English",
    "af" : "Afrikaans",
    "fr" : "French"
}

for lang, langname in languages.items():
    print(f"{article.capitalize()} on {langname} wikipedia page:")
    #Format the API endpoint with the article
    url = f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/{article}"
    #Use requests.get() to get the data
    r = requests.get(url)
    
    

    #Check if we got a 200 status code, otherwise abort the program
    if r.status_code is 200:
        print("the url status is ok.")
            
    else:
        print ("error")
        exit()
    
    #Display the title of the article, description and extract
    lines = r.text
    lines = json.loads(lines)    
    title = lines["title"]
    extract = lines["extract"]
    print(title)
    #some articles don't have descriptions so:
    #description = lines["description"]
    if 'description' not in lines:
        print ("No Description")
    else:
        print(f"The description on wikipedia is: {lines['description']}")
    print(f"The extract is: {extract}")


