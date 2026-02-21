from tkinter import *

window = Tk()
window.geometry('400x350')
window.title('Calculator')

# Entry Display
e = Entry(window, width=35, bd=5, justify='right')
e.place(x=50, y=20)

# --- Functions ---
def click(num):
    result = e.get()
    e.delete(0, END) # Clear the box to rewrite the full string
    e.insert(0, str(result) + str(num))

def clear():
    e.delete(0, END)

def calculate():
    try:
        result = eval(e.get())
        e.delete(0, END)
        e.insert(0, result)
    except:
        e.delete(0, END)
        e.insert(0, "Error")

# --- ROW 1 ---
Button(window, text='7', width=10, height=2, command=lambda: click(7)).place(x=50, y=70)
Button(window, text='8', width=10, height=2, command=lambda: click(8)).place(x=140, y=70)
Button(window, text='9', width=10, height=2, command=lambda: click(9)).place(x=230, y=70)
Button(window, text='/', width=5, height=2, command=lambda: click('/')).place(x=320, y=70)

# --- ROW 2 ---
Button(window, text='4', width=10, height=2, command=lambda: click(4)).place(x=50, y=120)
Button(window, text='5', width=10, height=2, command=lambda: click(5)).place(x=140, y=120)
Button(window, text='6', width=10, height=2, command=lambda: click(6)).place(x=230, y=120)
Button(window, text='*', width=5, height=2, command=lambda: click('*')).place(x=320, y=120)

# --- ROW 3 ---
Button(window, text='1', width=10, height=2, command=lambda: click(1)).place(x=50, y=170)
Button(window, text='2', width=10, height=2, command=lambda: click(2)).place(x=140, y=170)
Button(window, text='3', width=10, height=2, command=lambda: click(3)).place(x=230, y=170)
Button(window, text='-', width=5, height=2, command=lambda: click('-')).place(x=320, y=170)

# --- ROW 4 ---
Button(window, text='C', width=10, height=2, command=clear).place(x=50, y=220)
Button(window, text='0', width=10, height=2, command=lambda: click(0)).place(x=140, y=220)
Button(window, text='=', width=10, height=2, command=calculate).place(x=230, y=220)
Button(window, text='+', width=5, height=2, command=lambda: click('+')).place(x=320, y=220)

window.mainloop()