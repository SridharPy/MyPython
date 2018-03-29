#List of Python standard libraries: https://docs.python.org/3/library/index.html
import json
import difflib # This is a library to compare texts
from difflib import get_close_matches #We don't have to write difflib.get_close_matches everytime we use this function
#from difflib import SequenceMatcher # importing sequencematcher from difflib
#print("ignore the below just for testing")
#print(SequenceMatcher(None,"rainn","rain").ratio()) # This is used just for example, for our dictionary we are using get_close_matches function from the difflib library
"""SequenceMatch compares two block of text
the first argument is used to skip a phrase like if we have blank space or , that we dont wnat to comapre as we are comparing only two text we put None
next the two block of phrases
the we apply ratio method to see the match ratios between two texts"""

data = json.load(open("data.json"))

def findWord(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0 :
        return "Did you mean %s instead" % get_close_matches(word,data.keys())[0]
        # first arg word is the actual word
        #2nd arg list of words to compare against we are using data.keys() to check only keys from the dictionary keys() is the function that can be used with dictionary to extract just keys
        #3rd arg n=3 is to return the number of matches, its optinal, default is 3 if not specified , n=3
        #4rth arg cutoff by default is .6 which is also optional, its the matching/similarity ratio e.g. cutoff = 0.6
        #[0] is used to just get the first match from the list as that will be having the highest similarity ratio

    else:
        return "Word not found in the dictionary"


str1=input("Enter a word to find its meaning: ")
#print(str1=difflib.get_close_matches(str1,data,n=1))
print(findWord(str1.lower()))
