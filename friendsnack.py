#create a list that can be appended and loop
friends =["Peter", "Jane", "Simon"]
friends.append("Annie")
friends.append("Luke")
snacks = []
index = 0
for name in friends:
    snack = input(name + " what is your favourite snack? ")
    snacks.append(snack)
    index += 1

#print list of snack and friends using indexing 
for name in friends:
    index = friends.index(name)
    snack = snacks[index]
    print(name + "'s favourite snack is: " + snack) 