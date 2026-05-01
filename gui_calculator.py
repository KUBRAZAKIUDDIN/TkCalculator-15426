import tkinter as tk

def add():
    try:
        result.set(float(e1.get()) + float(e2.get()))
    except:
        result.set("Error")

def sub():
    try:
        result.set(float(e1.get()) - float(e2.get()))
    except:
        result.set("Error")

def mul():
    try:
        result.set(float(e1.get()) * float(e2.get()))
    except:
        result.set("Error")

def div():
    try:
        result.set(float(e1.get()) / float(e2.get()))
    except:
        result.set("Error")

def square():
    try:
        num = float(e1.get())
        result.set(num * num)
    except:
        result.set("Error")

def sqrt():
    try:
        num = float(e1.get())
        result.set(num ** 0.5)
    except:
        result.set("Error")

# Window
root = tk.Tk()
root.title("Calculator")

# Inputs
e1 = tk.Entry(root)
e1.pack()

e2 = tk.Entry(root)
e2.pack()

# Result
result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

# Buttons
tk.Button(root, text="Add", command=add).pack()
tk.Button(root, text="Subtract", command=sub).pack()
tk.Button(root, text="Multiply", command=mul).pack()
tk.Button(root, text="Divide", command=div).pack()

tk.Button(root, text="Square", command=square).pack()
tk.Button(root, text="Square Root", command=sqrt).pack()

# Run
root.mainloop()