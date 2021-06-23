import json
from difflib import get_close_matches

data = json.load(open("teaching/data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        user_input = input("Did you mean %s instead? (Y/N)" % get_close_matches(w, data.keys())[0])
        if user_input == "Y" or user_input == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif user_input == "N" or user_input == "n":
            return "The word does not exist"
        else:
            return "Unknown user input"
    else:
        return "That word does not exist"


print("Type /exit to exit the program")

while True:
    word = input("Enter a word: ")
    if word == "/exit":
        break
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
