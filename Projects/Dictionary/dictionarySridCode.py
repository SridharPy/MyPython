import json
import difflib # import difflib library
from difflib import get_close_matches # Imports get close match function from difflib

data = json.load(open(("data.json"))) # loads content of data.json into data dictionary in python

def translate(w): #function to perfrom dictionary operation
    if w in data.keys(): # data.keys() pulls just the keys from dictionary
        return data[w]
    elif w.title() in data.keys(): # converts first letter of each word in the text to upper case for Noun serach e.g. searches dictionary for Delhi instead of delhi
        return data[w.title()]
    elif len(get_close_matches(w,data.keys(),cutoff = 0.8)) > 0: # checks if closer match words are found or not
        newword = get_close_matches(w,data.keys(),cutoff = 0.8)[0] # puts first closer match word into the new variable for any typos
        res = input("Do you mean %s instead ? (y/n): " %newword ) #
        if res == 'y' or res == 'Y':
            return data[newword]  # Provides meaning of first similar word
        elif res == 'n' or res == 'N' :
            return "This word doesn't exist in the dictionary" # if not a typo then that word doesn't exist
        else:
            return "Invalid response" # for any otehr response other than y/n

    else:
        return "This word doesn't exist in the dictionary" # word is not found neither a close match found

word = input("Enter a word to find its meaning: ") #asks user to enter a word and stores in a vriable word
output = translate(word.lower()) # Call the function to do a word search for the supplied word sent as parameter and gets function return value in output variable

if type(output) == list: #check if the function return value is list then prints each item one per line
    print("Definition(s) of %s: " %word)
    for item in output:
        print(item)
else: #If the function return is a string then prints the entire string output
    print(output)
