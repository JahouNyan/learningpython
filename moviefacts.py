#program shows the title, release year, duration (in minutes) and director of your favourite movie.
movie = [{ 
        "title":"Avatar",
        "year":2009,
        "duration":162,
        "director":"James Cameron"
            },
        {"title":"Vanity Fair",
        "year":2007,
        "duration":87,
        "director":"George Lucas"}]
#Loop over  keys and create a variable value containing value associated with the key.


print(f"{movie['duration']} minutes") 
#Add a new key called actors u get to this list in your loop, join them together as a string
movie["actor"] = "Sigourney Weaver", "Zoe Saldana", "Sam Worthington"
print(movie["actor"])
movie["actor"] = ",".join(movie["actor"])

S