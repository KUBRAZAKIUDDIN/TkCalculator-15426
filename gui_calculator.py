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

root = tk.Tk()
root.title("Calculator")

e1 = tk.Entry(root)
e1.pack()

e2 = tk.Entry(root)
e2.pack()

result = tk.StringVar()

tk.Label(root, textvariable=result).pack()

tk.Button(root, text="Add", command=add).pack()
tk.Button(root, text="Subtract", command=sub).pack()
tk.Button(root, text="Multiply", command=mul).pack()
tk.Button(root, text="Divide", command=div).pack()

root.mainloop()