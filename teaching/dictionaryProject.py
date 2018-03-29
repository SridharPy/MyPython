import json

data = json.load(open("data.json"))

def findWord(word):
    if word in data:
        return data[word]
    else:
        return "Word not found in the dictionary"


str1=input("Enter a word to find its meaning: ")
print(str1)
#print(findWord(str1))
