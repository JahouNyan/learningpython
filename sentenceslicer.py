# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 10:40:43 2018

@author: Jahou
"""
#Ask for a sentence
#Calculate the start and end character of the sliced sentence
#Create a new string that is sliced with those numbers

sentence = input("Hello, whats on your mind today? ")
sentencelength = len(sentence)
start = int(round(sentencelength)*0.25)
end = int(round(sentencelength)*0.75)
new_sentence = sentence[start:end]
print(new_sentence)

    
#Convert the sentence to a list, split() by the space character
words = sentence.split(" ")
wordslength = len(words)
start = round(wordslength * 0.25)
end = round(wordslength * 0.75)
new_words = words[start:end]
print(" ".join(new_words)) 


    

