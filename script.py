import json
from difflib import get_close_matches
import time
import os
import platform

# //////////////////// GET OS ////////////////////
platform_type = platform.system()

# //////////////////// DICTIONARY ////////////////////

if platform_type == 'Windows':


    data = json.load(open(r".\Data\data.json"))

    def searchdic(word):
        word = word.lower()
        if word in data:
            return data[word]
        elif word.title() in data:
            return data[word.title()]
        elif word.upper() in data:
            return data[word.upper()]
        elif len(get_close_matches(word, data.keys())) > 0:
            print("[?] Did you mean %s word instead? " %get_close_matches(word, data.keys())[0])
            decide = input("[?] y or n: ")
            if decide.lower() == "y":
                return data[get_close_matches(word, data.keys())[0]]
            elif decide.lower() == "n":
                return ("[!!] The word does not exist! ")
            else:
                return ("[!!] Command does not exist! ")
        else:
            print("[!!] The word does not exist")

    os.system('cls')

    iword = input("[+] Enter the word: ")
    output = searchdic(iword)

    if type(output) == list:
        for item in output:
            print(item)

    else:
        print(output)

    # //////////////////// Settings ////////////////////

    settings = json.load(open(r".\Data\settings.json"))
    time_to_wait = settings["time"] # will be used as the time to wait before closing the program

    print("\n\nThank you for using the program!\nThis window will close automatically in " + str(time_to_wait) + " seconds")
    time.sleep(int(time_to_wait))
    exit()

else:

    data = json.load(open(r"./Data/data.json"))

    def searchdic(word):
        word = word.lower()
        if word in data:
            return data[word]
        elif word.title() in data:
            return data[word.title()]
        elif word.upper() in data:
            return data[word.upper()]
        elif len(get_close_matches(word, data.keys())) > 0:
            print("[?] Did you mean %s word instead? " %get_close_matches(word, data.keys())[0])
            decide = input("[?] y or n: ")
            if decide.lower() == "y":
                return data[get_close_matches(word, data.keys())[0]]
            elif decide.lower() == "n":
                return ("[!!] The word does not exist! ")
            else:
                return ("[!!] Command does not exist! ")
        else:
            print("[!!] The word does not exist")

    os.system('clear')

    iword = input("[+] Enter the word: ")
    output = searchdic(iword)

    if type(output) == list:
        for item in output:
            print(item)

    else:
        print(output)

    # //////////////////// Settings ////////////////////

    settings = json.load(open(r"./Data/settings.json"))
    time_to_wait = settings["time"] # will be used as the time to wait before closing the program

    print("\n\nThank you for using the program!\nThis window will close automatically in " + str(time_to_wait) + " seconds")
    time.sleep(int(time_to_wait))
    exit()


