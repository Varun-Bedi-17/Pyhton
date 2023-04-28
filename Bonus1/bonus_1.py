import json
from difflib import get_close_matches

data = json.load(open("Bonus1/data.json"))

def find_word(word):
    if word.lower() in data:
        return data[word]
    
    elif word.title() in data.keys():
        return data[word]

    elif word.upper() in data.keys():
        return data[word]
    
    elif get_close_matches(word, data.keys()):
        choice = input(f"Did you mean \'{get_close_matches(word, data.keys())[0]}\' instead. Press 'Y' for yes and 'N' for no : " )
        if choice.upper() == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif choice.upper() == 'N':
            return "The word doesn\'t exist in our library."
        else:
            return "Incorrect entry"
    
    else:
        return "The word doesn\'t exist in our library."
    


word = input("Enter word: ")
result = find_word(word)
if type(result) == list:
    for item in result:
        print(item)

else:
    print(result)
