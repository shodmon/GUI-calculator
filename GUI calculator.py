import tkinter as tk

def button_click(number):
    current = entry.get()
    if current == "0":
        current = ""
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Create the main window
root = tk.Tk()
root.title("My GUI calculator")
root.geometry("400x800")

# Add a label widget
#label = tk.Label(root, text="Hello, Tkinter!")
#label.pack()

#mainEntry = tk.Entry(root, width=40, borderwidth=5)
#mainEntry.pack()

entry = tk.Entry(root, width=20, borderwidth=5, font=("Arial", 24))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('0', 4, 1),
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=40, pady=20,
                       command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)



# Start the GUI event loop
root.mainloop()