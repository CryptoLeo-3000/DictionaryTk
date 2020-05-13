from tkinter import *
import DictionaryBk as DictB
import DictionaryEntry as De

def searchword():
    meaning.delete("0.0", END)
    result = DictB.dictionary(search_value.get())
    for mean in result:
        meaning.insert(END, mean)
        meaning.insert(END, "\n")

windows = Tk()
windows.minsize(20, 20)
windows.title("Dictionary")

#Search Word:
search = Label(windows, text = "Search:")
search.grid(row = 0, column = 0)

#Word Input:
search_value = StringVar()
keyword = Entry(windows, text = search_value)
keyword.grid(row = 0, column = 1)

empty_label1 = Label(windows, text = " ")
empty_label1.grid(row = 0, column = 2)

#Search Button:
searchbutton = Button(windows, text = "👀", height = 1, width = 5, command = searchword)
searchbutton.grid(row = 0, column = 3)

empty_label2 = Label(windows, text = " ")
empty_label2.grid(row = 1, column = 0)

#Meaning of search word displayed:
meaning = Text(windows, height = 10, width = 40)
meaning.grid(row = 2, column = 0, rowspan = 1, columnspan = 4)

#Scroll Bar:
yscroll = Scrollbar(windows)
yscroll.grid(row = 2, column = 5)

meaning.configure(yscrollcommand = yscroll.set)
yscroll.configure(command = meaning.yview)

#Add Button:
add_button = Button(windows, text = "Add", height = 2, width = 6, command = De.entry)
add_button.grid(row = 3, column = 0)

#Exit Button:
exit_button = Button(windows, text = "Exit", height = 2, width = 6, command = windows.destroy)
exit_button.grid(row = 3, column = 1)

windows.mainloop()