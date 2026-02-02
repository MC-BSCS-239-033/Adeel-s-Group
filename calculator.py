# ================================
# Scientific Calculator in Python
# Using Tkinter (GUI)
# ================================

import tkinter as tk
import math

# ----------------
# Main Window
# ----------------
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("360x520")
root.resizable(False, False)

# ----------------
# Entry Widget
# ----------------
expression = ""

entry = tk.Entry(
    root,
    font=("Arial", 20),
    borderwidth=5,
    relief=tk.RIDGE,
    justify="right"
)
entry.pack(fill="both", padx=10, pady=10, ipady=10)

# ----------------
# Functions
# ----------------
def press(key):
    """Insert pressed button value into entry"""
    global expression
    expression += str(key)
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

def clear():
    """Clear the calculator"""
    global expression
    expression = ""
    entry.delete(0, tk.END)

def calculate():
    """Evaluate the expression"""
    global expression
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        expression = str(result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        expression = ""

def scientific(func):
    """Apply scientific functions"""
    global expression
    try:
        value = float(entry.get())
        if func == "sin":
            result = math.sin(math.radians(value))
        elif func == "cos":
            result = math.cos(math.radians(value))
        elif func == "tan":
            result = math.tan(math.radians(value))
        elif func == "log":
            result = math.log10(value)
        elif func == "ln":
            result = math.log(value)
        elif func == "sqrt":
            result = math.sqrt(value)
        elif func == "square":
            result = value ** 2

        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        expression = str(result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        expression = ""

# ----------------
# Buttons Frame
# ----------------
frame = tk.Frame(root)
frame.pack()

# ----------------
# Button Layout
# ----------------
buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("+",4,2), ("=",4,3)
]

# Create Number & Operator Buttons
for (text,row,col) in buttons:
    if text == "=":
        btn = tk.Button(frame, text=text, width=7, height=2,
                        command=calculate, font=("Arial", 14))
    else:
        btn = tk.Button(frame, text=text, width=7, height=2,
                        command=lambda t=text: press(t),
                        font=("Arial", 14))
    btn.grid(row=row, column=col, padx=5, pady=5)

# ----------------
# Scientific Buttons
# ----------------
tk.Button(frame, text="sin", width=7, height=2,
          command=lambda: scientific("sin")).grid(row=5,column=0)

tk.Button(frame, text="cos", width=7, height=2,
          command=lambda: scientific("cos")).grid(row=5,column=1)

tk.Button(frame, text="tan", width=7, height=2,
          command=lambda: scientific("tan")).grid(row=5,column=2)

tk.Button(frame, text="√", width=7, height=2,
          command=lambda: scientific("sqrt")).grid(row=5,column=3)

tk.Button(frame, text="log", width=7, height=2,
          command=lambda: scientific("log")).grid(row=6,column=0)

tk.Button(frame, text="ln", width=7, height=2,
          command=lambda: scientific("ln")).grid(row=6,column=1)

tk.Button(frame, text="x²", width=7, height=2,
          command=lambda: scientific("square")).grid(row=6,column=2)

tk.Button(frame, text="π", width=7, height=2,
          command=lambda: press(math.pi)).grid(row=6,column=3)

# ----------------
# Clear Button
# ----------------
tk.Button(root, text="CLEAR", width=30, height=2,
          font=("Arial", 14), command=clear).pack(pady=10)

# ----------------
# Run App
# ----------------
root.mainloop()
