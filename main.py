import tkinter as tk

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return None
    return a / b

def mod(a, b):
    if b == 0:
        return None
    return a % b

def power(a, b):
    return a ** b

def click_add():
    try:

        n1 = entry_a.get()
        n2 = entry_b.get()

        result = add(float(n1), float(n2))
        label_result.config(text=result, fg="black")
    except ValueError:
        label_result.config(text="Введи только числа!", fg="red")


def click_sub():
    try:

        n1 = entry_a.get()
        n2 = entry_b.get()

        result = sub(float(n1), float(n2))
        label_result.config(text=result, fg="black")
    except ValueError:
        label_result.config(text="Введи только числа!", fg="red")


def click_mul():
    try:

        n1 = entry_a.get()
        n2 = entry_b.get()

        result = mul(float(n1), float(n2))
        label_result.config(text=result, fg="black")
    except ValueError:
        label_result.config(text="Введи только числа!", fg="red")


def click_div():
    try:

        n1 = entry_a.get()
        n2 = entry_b.get()
 
        
        result = div(float(n1), float(n2))
        if result == None:
            label_result.config(text="На ноль делить нельзя!", fg="red")
        else:
            label_result.config(text=result, fg="black")
    except ValueError:
        label_result.config(text="Введи только числа!", fg="red")


def click_mod():
    try:

        n1 = entry_a.get()
        n2 = entry_b.get()
 
        
        result = mod(float(n1), float(n2))
        if result == None:
            label_result.config(text="На ноль делить нельзя!", fg="red")
        else:
            label_result.config(text=result, fg="black")
    except ValueError:
        label_result.config(text="Введи только числа!", fg="red")


def click_power():
    try:

        n1 = entry_a.get()
        n2 = entry_b.get()

        result = power(float(n1), float(n2))
        label_result.config(text=result, fg="black")
    except ValueError:
        label_result.config(text="Введи только числа!", fg="red")


def click_clear():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    label_result.config(text="", fg="black")


root = tk.Tk()

root.title("Calculator 2.0")
root.geometry("300x400")

label_a = tk.Label(root, text="Первое число")
label_a.grid(row=0, column=0)

entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

label_b = tk.Label(root, text="Второе число")
label_b.grid(row=1, column=0)

entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

actions = [("Сложить", click_add), ("Вычесть", click_sub), ("Умножить", click_mul), ("Делить", click_div), ("Остаток", click_mod), ("Степень", click_power), ("Очистить", click_clear)]

for i, (name, func) in enumerate(actions):
    btn = tk.Button(root, text=name, command=func)
    btn.grid(row=2 + i, column=0)

label_result = tk.Label(root, text="")
label_result.grid(row=10, column=0, columnspan=2)

root.mainloop()