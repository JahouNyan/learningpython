#import jsoon library
import json
json.load
f = open("movies.json")
movies = json.load(f)
 
#give the use 3 options
request = input("How do you want to filter movies: \n1. Director \n2. Actor(s) \n3. Year \n4. Genre(s) \n5. Actor/Director \nPlease enter your option number: ")
    
#quit if out of range
if request not in ["1", "2", "3", "4", "5"]:
    print("Invalid request!")
    exit()

#operations for each filter request   
if request == "1":
   directorname = input ("What is the name of the director? ")
   for item in movies:
       director = item["director"]
       if director == directorname:
           print(f"{director} directed {item['title']} movie.")
     
 
if request == "2":
   actorname = input ("What is the name of the actor? ")
   for item in movies:
       actor = item["actors"]
       if actor == actorname:
           print(f"{actor} starred in {item['title']} movie.")
       

if request == "3":
   releaseyr = int(input ("Which year's releases do you want to see? "))
   for item in movies:
        year = item["year"]
        if year == releaseyr:
           print(f"{item['title']} movie was released in {year}.")
           
# due to formatting in this list there may be errors
if request == "4":
   genrename = input ("What film genre are you interested in? ")
   genrename = (genrename + " film")
   for item in movies:
       #genre = item["genres"]
       for genre in item["genres"]:
           genre.split(",")
       if genre == genrename:
           print(f"{item['title']} movie is a {genre}.")
           

if request == "5":
   diractname = input ("What is the name of the director and actor? ")
   for item in movies:
       diract = item["actors"] and item["director"]
       if diract == diractname:
           print(f"{diract} directed and acted in {item['title']} movie.")
          
            
else:
    print("Sorry, there are no records for your request")
        

