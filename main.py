import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("1", 0, 0),
    ("2", 0, 1),
    ("3", 0, 2),
    ("4", 1, 0),
    ("5", 1, 1),
    ("6", 1, 2),
    ("7", 2, 0),
    ("8", 2, 1),
    ("9", 2, 2),
    ("0", 3, 1),
    (".", 3, 0),  # Добавленная кнопка для десятичной точки
    ("+", 0, 3),
    ("-", 1, 3),
    ("*", 2, 3),
    ("/", 3, 3),

]

for button_text, row, column in buttons:
    button = tk.Button(root, text=button_text, padx=43, pady=20, command=lambda text=button_text: button_click(text))
    button.grid(row=row+1, column=column)

clear_button = tk.Button(root, text="С", padx=43, pady=20, command=button_clear)
clear_button.grid(row=4, column=5,)

equal_button = tk.Button(root, text="=", padx=43, pady=20, command=button_equal)
equal_button.grid(row=4, column=2, )



root.mainloop()
