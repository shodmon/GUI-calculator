import tkinter as tk

# Globals for storing state
current_operator = None
first_number = None

def format_number(n):
    if isinstance(n, float) and n.is_integer():
        return str(int(n))
    return str(n)

def button_click(number):
    current = entry.get()
    if current == "0":
        entry.delete(0, tk.END)
    entry.insert(tk.END, str(number))

def clear():
    global current_operator, first_number
    entry.delete(0, tk.END)
    label.config(text="")
    current_operator = None
    first_number = None

def add_decimal():
    current = entry.get()
    if "." not in current:
        entry.insert(tk.END, ".")

def set_operator(operator):
    global current_operator, first_number
    first_number = float(entry.get())
    current_operator = operator
    label.config(text=f"{format_number(first_number)} {operator}")
    entry.delete(0, tk.END)

def calculate():
    global current_operator, first_number
    if current_operator is None or first_number is None:
        return
    second_number = float(entry.get())
    expression = f"{format_number(first_number)} {current_operator} {format_number(second_number)}"
    try:
        result = eval(expression)
        if isinstance(result, float):
            result = round(result, 10)   
            if result.is_integer():      
                result = int(result)
        label.config(text=f"{expression} =")
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
        # reset for next calculation
        first_number = result
        current_operator = None
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        label.config(text="")

# Create main window
root = tk.Tk()
root.title("GUI Calculator")
root.geometry("400x500")

# Label to show expression
label = tk.Label(root, text="", anchor="e", font=("Arial", 14))
label.grid(row=0, column=0, columnspan=4, sticky="we")

# Entry for current number
entry = tk.Entry(root, width=20, borderwidth=5, font=("Arial", 24), justify="right")
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
entry.insert(0, "0")

# Buttons
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('C', 5, 0), ('0', 5, 1), ('.', 5, 2), ('+', 5, 3),
                                           ('=', 6, 3),
]

for (text, row, col) in buttons:
    if text.isdigit():
        action = lambda t=text: button_click(t)
    elif text == ".":
        action = add_decimal
    elif text in ['+', '-', '*', '/']:
        action = lambda t=text: set_operator(t)
    elif text == '=':
        action = calculate
    elif text == 'C':
        action = clear

    button = tk.Button(root, text=text, padx=30, pady=20, command=action)
    button.grid(row=row, column=col)

root.mainloop()