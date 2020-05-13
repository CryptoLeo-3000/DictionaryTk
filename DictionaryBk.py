import json
import difflib

def dictionary(word):    
    data = open("data.json","r+")
    words = json.load(data)
    if word.lower() in words:
        meaning = words[word]
        return meaning
    elif word.upper() in words:
        meaning = words[word]
        return meaning
    elif word.isdigit():
        return "You entered number(s)\nPlease enter a meaningful word"
    else:
        return "No such word found 🤔"