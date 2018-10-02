#define good and bad words
badwords = ["appel", "appels", "lemn", "bannana", "orang", "gapes"]
goodwords = ["apple", "apples", "lemon", "banana", "orange", "grapes"]
sentence = input("Name a fruit: ")
new_sentence = []

#compare, warn and exchange
for word in sentence.split(" "):
	if word in badwords:
		index = badwords.index(word)
		check = goodwords[index]
		print("***" + word + " is spelt wrong. " + word + " should be " + check)
		new_sentence.append(check)
	else:
		new_sentence.append(word)
new_sentence = " ".join(new_sentence)
print(new_sentence)

