from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import json
import platform
from difflib import get_close_matches

root = Tk()
root.title("Dictionary v1.0")
root.resizable(False, False)
root['background'] = "#313131"

def fetch_data(word):
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
                swyon_msg = "Did you mean " + get_close_matches(word, data.keys())[0] + " word instead?"
                swyon = messagebox.askquestion ('Word Guess',swyon_msg,icon = 'warning')
                if swyon == "yes":
                    return data[get_close_matches(word, data.keys())[0]]
                elif swyon == "no":
                    return ("\nThe word does not exist! ")
                else:
                    return ("\nThe word does not exist! ")
            else:
                return "\nThe word does not exist"

        output = searchdic(word)

        if type(output) == list:
            for item in output:
                tmain.insert(END, "\n\n" + item)
                print("\n" + item)


        else:
            tmain.insert(END, "\n" + output)
            print(output)


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
                swyon_msg = "Did you mean " + get_close_matches(word, data.keys())[0] + " word instead?"
                swyon = messagebox.askquestion ('Word Guess',swyon_msg,icon = 'warning')
                if swyon == "yes":
                    return data[get_close_matches(word, data.keys())[0]]
                elif swyon == "no":
                    return ("\nThe word does not exist! ")
                else:
                    return ("\nThe word does not exist! ")
            else:
                return "\nThe word does not exist"

        output = searchdic(word)

        if type(output) == list:
            for item in output:
                tmain.insert(END, "\n\n" + item)
                print("\n" + item)


        else:
            tmain.insert(END, "\n" + output)
            print(output)


def clear():
    egword.delete(0, END)
    tmain.delete("1.0", END)

def save_to_txt():
    current_word = egword.get() + ".txt"
    current_meaning = tmain.get("1.0", END)

    file = open(current_word, "w+")
    file.write(current_meaning)
    file.close()

def search():
    search_word = egword.get()
    fetch_data(search_word)
    
fontbtn = font.Font(family="Arial", size="13", weight="bold")

ltop = Label(root, text="Dictionary", bg="#313131", fg="#FFFFFF")
ltop.grid(row=2, column=0, columnspan=3)
ltop['font'] = font.Font(family="Arial", size="15", weight="bold")

egword = Entry(root, bg="#C5C5C5", fg="#000000", width=37, borderwidth=6)
egword.grid(row=3, column=0, columnspan=3, pady=5)
egword['font'] = font.Font(family="Arial", size="12", weight="bold")

tmain = Text(root, height=10, width=40, bg="#C5C5C5", fg="#000000")
tmain.grid(row=4, column=0, columnspan=3, pady=5)
tmain['font'] = font.Font(family="Arial", size="12")

bsearch = Button(root, text="Search", command=search, padx=60, bg="#007700", fg="#FFFFFF")
bsearch.grid(row=5, column=0, columnspan=1)
bsearch['font'] = fontbtn

bsave = Button(root, text="Save", command=save_to_txt, padx=20, bg="#D3A500", fg="#FFFFFF")
bsave.grid(row=5, column=1, columnspan=1)
bsave['font'] = fontbtn

bclear = Button(root, text="Clear", command=clear, padx=20, bg="#DC0000", fg="#FFFFFF")
bclear.grid(row=5, column=2, columnspan=1)
bclear['font'] = fontbtn

root.mainloop()
