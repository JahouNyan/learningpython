#create a list that can be appended and loop
friends = {"names": ["Peter", "Jane", "Simon"], "snacks":[]}

for index, name in enumerate(friends ['names']):
    namelen = len(name)
    snack = input(f"{name}, what is your favourite snack? ")
    snacks = friends['snacks']
    snacks.append(snack)
    
#print list of snack and friends using indexing 
    print(f"{name} 's name is {namelen} long.")
    print(f"{name} 's favourite snack is: {snack}") 