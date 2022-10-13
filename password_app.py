from tkinter import *
from PIL import ImageTk,Image
import sqlite3
import random



def newPassword():
    number = 15
    lower_case_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                       "s",
                       "t", "u", "v", "w", "x", "y", "z"]
    upper_case_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                       "S",
                       "T", "U", "V", "W", "X", "Y", "Z"]
    number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    special_list = ["!", "@", "#", "$", "%", "^", "&", "*"]
    char_list = [lower_case_list, upper_case_list, number_list]
    enddex = 2
    special_chars = True
    if special_chars is True:
        char_list.insert(3, special_list)
        enddex = 3
    good_pass = False
    word = ""
    while not good_pass:
        word = ""
        constraint1 = False
        constraint2 = False
        constraint3 = False
        constraint4 = False
        for i in range(number):
            index = random.randint(0, enddex)
            current_list = char_list.__getitem__(index)
            if index == 0:
                constraint1 = True
            if index == 1:
                constraint2 = True
            if index == 2:
                constraint3 = True
            if index == 3:
                constraint4 = True
            new_char = current_list.__getitem__(random.randint(0, len(current_list) - 1))
            word = word + new_char
        if constraint1 and constraint2 and constraint3:
            if special_chars is True and constraint4 is True:
                good_pass = True
            elif special_chars is False:
                good_pass = True
    print(word)
    user = input("Would you like to save:  ")
    if user.upper() == "YES":
        with open('pw.txt', 'w+') as output:
            output.write(word)
    return word

def createTable():
    conn = sqlite3.connect('password_book.db')
    c = conn.cursor()
    c.execute(""" CREATE TABLE passwords (
                p_name text,
                p_word text )""")
    conn.commit()
    conn.close()

def app():
    window = Tk()
    window_title = Label(window, text="Password App")
    window_title.pack()
    window.title('Password App')
    #window.iconbitmap('C:\Users\jontg\PycharmProjects\pythonStuff\codemy.ico')
    window.geometry("400x400")


    #special_chars = BooleanVar()
    #c1 = Checkbutton(window, text='Special Characters', variable=special_chars, onvalue=True, offvalue=0)
    #c1.pack()
    pButton= Button(window, text = 'Generate',command = newPassword)
    pButton.pack()
    #save_button = Button(window,text = "Save Password",command = newPassword)
    l = Label(window, text = "New Password")
    l.config(font=("Courier", 14))
    l.pack()
    window.mainloop()

if __name__ == "__main__":
    app()
