from tkinter import *
from tkinter import ttk

first_variable = None
current_operator = None

# def format_number(n):
#     format

def insertNumber(number):
    entry.insert(entry.end, number)

# def operation(symbol):
#     operate

def calculate():
    expression = entry.get(0, END)
    eval(expression)

#def add_decimal():
#    add decimal

# def clear():
#     entry.delete(0, entry.end)


root =Tk()
root.title("GUI calculator")
root.geometry("300x250")

label = ttk.Label(root, font=("Ariel", 12))
label.grid (column=0, row=0)

entry = ttk.Entry(root)
entry.grid (column=0, row=1, columnspan=4, sticky="we")

buttons = {("7", 0, 2), ("8", 1, 2), ("9", 2, 2), ("/", 3, 2),
           ("4", 0, 3), ("5", 1, 3), ("6", 2, 3), ("*", 3, 3),
           ("1", 0, 4), ("2", 1, 4), ("3", 2, 4), ("-", 3, 4),
           (".", 0, 5), ("0", 1, 5), ("C", 2, 5), ("+", 3, 5),
                        ("=", 1, 6)}

for (text, column, row) in buttons:
    if (text.isdigit()):
        action = lambda t=text: insertNumber(text)
    # elif (text == {"*", "/", "+", "-"}):
    #     action = lambda t=text: operation(text)
    elif (text == "="):
        action = calculate
    # elif (text == "."):
    #     action = add_decimal
    # elif (text == "C"):
    #     action == clear
    else :
        action = None
    button = ttk.Button (root, text=text, command=action)
    button.grid(column=column, row=row)

root.mainloop()