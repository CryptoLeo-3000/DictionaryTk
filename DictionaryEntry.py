from tkinter import *
import json
import difflib


def entry():

    def update():
        data = open("data.json","r+")
        words = json.load(data)
        word = entry.get()
        mean = meaning.get()
        updates = {word:mean}
        words.update(updates)
        data.seek(0)
        json.dump(words,data)
        
    windows = Tk()
    windows.minsize(10, 40)
    windows.title("Word Entry")

    word_label = Label(windows, text = "Word:")
    word_label.grid(row = 0, column= 0)
    entry_word = StringVar()
    entry = Entry(windows, text = entry_word)
    entry.grid(row = 0, column = 1)

    meaning_label = Label(windows, text = "Meaning:")
    meaning_label.grid(row = 1, column = 0)
    entry_meaning = StringVar()
    meaning = Entry(windows, text= entry_meaning)
    meaning.grid(row = 1, column = 1)

    update_button = Button(windows, text = "Update", command = update)
    update_button.grid(row = 2, column = 0)
    done_button = Button(windows, text = "Done", command = windows.destroy)
    done_button.grid(row = 2, column= 1)
    cancel_button = Button(windows, text = "Cancel", command = windows.destroy)
    cancel_button.grid(row = 2, column = 2)

    windows.mainloop()