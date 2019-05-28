import tkinter as tk
from tkinter import messagebox

mainWindow = tk.Tk()
mainWindow.title("Calculator")

first_number_label = tk.Label(mainWindow, text="Enter first number", padx=10, pady=20)
first_number_label.pack()

first_number = tk.Entry(mainWindow)
first_number.pack()

second_number_label = tk.Label(mainWindow, text="Enter second number", padx=10, pady=20)
second_number_label.pack()

second_number = tk.Entry(mainWindow)
second_number.pack()

operation_label = tk.Label(mainWindow, text="Operation", padx=10, pady=20)
operation_label.pack()

add_button = tk.Button(mainWindow, text="+", padx=5, pady=5, command=lambda: add())
add_button.pack()

subtract_button = tk.Button(mainWindow, text="-", padx=5, pady=5, command=lambda: subtract())
subtract_button.pack()

multiply_button = tk.Button(mainWindow, text="*", padx=5, pady=5, command=lambda: multiply())
multiply_button.pack()

divide_button = tk.Button(mainWindow, text="/", padx=5, pady=5, command=lambda: divide())
divide_button.pack()

result_label = tk.Label(mainWindow, text="Operation result is:", padx=10, pady=20)
result_label.pack()


def add():
    try:
        no1 = int(first_number.get())
        no2 = int(second_number.get())
        result = no1 + no2
        result_label.config(text="Operation result is:" + str(result))
    except ValueError:
        if (len(first_number.get()) == 0) or (len(second_number.get()) == 0):
            messagebox.showerror("Error", "Please enter a value")
        else:
            messagebox.showerror("Error", "Enter only integer value")


def subtract():
    try:
        no1 = int(first_number.get())
        no2 = int(second_number.get())
        result = no1 - no2
        result_label.config(text="Operation result is:" + str(result))
    except ValueError:
        if (len(first_number.get()) == 0) or (len(second_number.get()) == 0):
            messagebox.showerror("Error", "Please enter a value")
        else:
            messagebox.showerror("Error", "Enter only integer value")


def multiply():
    try:
        no1 = int(first_number.get())
        no2 = int(second_number.get())
        result = no1 * no2
        result_label.config(text="Operation result is:" + str(result))
    except ValueError:
        if (len(first_number.get()) == 0) or (len(second_number.get()) == 0):
            messagebox.showerror("Error", "Please enter a value")
        else:
            messagebox.showerror("Error", "Enter only integer value")


def divide():
    try:
        no1 = int(first_number.get())
        no2 = int(second_number.get())
        result = no1 / no2
        result_label.config(text="Operation result is:" + str(result))
    except ValueError:
        if (len(first_number.get()) == 0) or (len(second_number.get()) == 0):
            messagebox.showerror("Error", "Please enter a value")
        else:
            messagebox.showerror("Error", "Enter only integer value")
    except ZeroDivisionError:
        tk.messagebox.showerror('ALERT!!', 'Cannot divide by zero')


mainWindow.mainloop()