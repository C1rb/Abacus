#Abacus Version 1.2

#Importing tkinter (tk and *)
import tkinter as tk
from tkinter import *

#Main window (Show screen, Title, Window size, Backround color, Resizable, Transparency/Window Stacking and Icon)
root = Tk()
root.title("Abacus")
root.geometry("220x300+550+200")
root.configure(bg = "grey")
root.resizable(False, False)
root.attributes("-topmost", 1)
#root.iconbitmap("C:/Users/Person/Images/Python Tkinter Icon/Abacus.ico") #There is no icon for this program, in order to add an icon kindly open and read ICON.md

#Entry widget
e = Entry(root, width = 22, font=("Consolas 14 bold"))
e.grid(row = 0, column = 1, columnspan = 12, ipady = 10)

#Functions
def click(num, e):
    global expr
    expr = expr + str(num)
    e.delete(0, END)
    e.insert(0, expr)
    return

def equal():
    global expr
    ans = str(eval(expr))
    e.delete(0, END)
    e.insert(0, ans)
    return

def clear():
    global expr
    expr = ""
    e.delete(0, END)
    return
    
expr = ""

#Button
#Numeric buttons
button_0 = Button(root, borderwidth = 8, padx = 0, pady = 0, text = "0", height = 2, width = 5, command = lambda: click(0, e)).grid(row = 5, column = 1)
button_1 = Button(root, borderwidth = 8, padx = 0, pady = 0, text = "1", height = 2, width = 5, command = lambda: click(1, e)).grid(row = 4, column = 1)
button_4 = Button(root, borderwidth = 8, padx = 0, pady = 0, text = "4", height = 2, width = 5, command = lambda: click(4, e)).grid(row = 3, column = 1)
button_7 = Button(root, borderwidth = 8, padx = 0, pady = 0, text = "7", height = 2, width = 5, command = lambda: click(7, e)).grid(row = 2, column = 1)

button_2 = Button(root, borderwidth = 8, padx = 0, pady = 0, text = "2", height = 2, width = 5, command = lambda: click(2, e)).grid(row = 4, column = 2)
button_5 = Button(root, borderwidth = 8, padx = 0, pady = 0, text = "5", height = 2, width = 5, command = lambda: click(5, e)).grid(row = 3, column = 2)
button_8 = Button(root, borderwidth = 8, padx = 0, pady = 0, text = "8", height = 2, width = 5, command = lambda: click(8, e)).grid(row = 2, column = 2)

button_3 = Button(root, borderwidth = 8, padx = 0, pady = 0, text = "3", height = 2, width = 5, command = lambda: click(3, e)).grid(row = 4, column = 3)
button_6 = Button(root, borderwidth = 8, padx = 0, pady = 0, text = "6", height = 2, width = 5, command = lambda: click(6, e)).grid(row = 3, column = 3)
button_9 = Button(root, borderwidth = 8, padx = 0, pady = 0, text = "9", height = 2, width = 5, command = lambda: click(9, e)).grid(row = 2, column = 3)
#Operator buttons
button_equal = Button(root, borderwidth = 8, padx = 0, pady = 0, text = "=", height = 2, width = 5, command = equal).grid(row = 5, column = 3)
button_clear = Button(root, borderwidth = 8, padx = 0, pady = 0, text = "C", height = 2, width = 29, command = clear).grid(row = 1, column = 1, columnspan = 4)
button_dec = Button(root, borderwidth = 8, padx = 0, pady = 0, text = ".", height = 2, width = 5, command = lambda: click(".", e)).grid(row = 5, column = 2)

button_add = Button(root, borderwidth = 8, padx = 0, pady = 0, text = "+", height = 2, width = 5, command = lambda: click("+", e)).grid(row = 2, column = 4)
button_minus = Button(root, borderwidth = 8, padx = 0, pady = 0, text = "-", height = 2, width = 5, command = lambda: click("-", e)).grid(row = 3, column = 4)
button_times = Button(root, borderwidth = 8, padx = 0, pady = 0, text = "*", height = 2, width = 5, command = lambda: click("*", e)).grid(row = 4, column = 4)
button_divide = Button(root, borderwidth = 8, padx = 0, pady = 0, text = "/", height = 2, width = 5, command = lambda: click("/", e)).grid(row = 5, column = 4)
 
#To maintain and close the main window
root.mainloop()
