import tkinter as tk

def button_click(number):
    current = mainEntry.get()
    mainEntry.delete(0, tk.END)
    mainEntry.insert(0, str(number))

# Create the main window
root = tk.Tk()
root.title("My GUI calculator")
root.geometry("400x800")

# Add a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

mainEntry = tk.Entry(root, width=40, borderwidth=5)
mainEntry.pack()

button1 = tk.Button(root, text="1", padx=40, pady=20, command = lambda: button_click(1))
button1.pack()
button2 = tk.Button(root, text="2", padx=40, pady=20, command = lambda: button_click(2))
button2.pack()
button3 = tk.Button(root, text="3", padx=40, pady=20, command = lambda: button_click(3))
button3.pack()
button4 = tk.Button(root, text="4", padx=40, pady=20, command = lambda: button_click(4))
button4.pack()
button5 = tk.Button(root, text="5", padx=40, pady=20, command = lambda: button_click(5))
button5.pack()
button6 = tk.Button(root, text="6", padx=40, pady=20, command = lambda: button_click(6))
button6.pack()
button7 = tk.Button(root, text="7", padx=40, pady=20, command = lambda: button_click(7))
button7.pack()
button8 = tk.Button(root, text="8", padx=40, pady=20, command = lambda: button_click(8))
button8.pack()
button9 = tk.Button(root, text="9", padx=40, pady=20, command = lambda: button_click(9))
button9.pack()
button0 = tk.Button(root, text="0", padx=40, pady=20, command = lambda: button_click(0))
button0.pack()
button0 = tk.Button(root, text="0", padx=40, pady=20, command = lambda: button_click(0))
button0.pack()
button0 = tk.Button(root, text="0", padx=40, pady=20, command = lambda: button_click(0))
button0.pack()
button0 = tk.Button(root, text="0", padx=40, pady=20, command = lambda: button_click(0))
button0.pack()
button0 = tk.Button(root, text="0", padx=40, pady=20, command = lambda: button_click(0))
button0.pack()



# Start the GUI event loop
root.mainloop()