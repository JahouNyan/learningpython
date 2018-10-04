#Multidimensional lists with snacknames

friends =[["Peter", "Jane", "Simon"], []]
snacks = [friends[1]]
for index, friend in enumerate(friends[0]):
    namelen = str(len(friend))
    snack = input(friend + " What is your favourite snack? ")
    snacks.append(snack)
    snack = str(snacks[index+1])
    friends.append(snack)
    print(friend +"'s name is " + namelen + " characters long.")
    print(friend + "'s favourite snack is: " + snack) 