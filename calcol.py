from tkinter import *

window = Tk()
window.geometry('350x450')
window.title('Modern Calculator')
window.configure(bg='#1c1c1c') # Dark background for the window

# Styled Entry Display
# 'borderwidth=0' and a nice 'pady' make it look sleek
e = Entry(window, width=18, bd=0, font=('Arial', 24), bg='#1c1c1c', fg='white', justify='right')
e.place(x=20, y=40)

# --- Functions ---
def click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

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

# --- Styling Settings ---
# relief="flat" makes them look modern. 'activebackground' is the color when clicked.
num_config = {'width': 5, 'height': 2, 'font': ('Arial', 14, 'bold'), 'bg': '#333333', 'fg': 'white', 'relief': 'flat', 'activebackground': '#4d4d4d'}
op_config  = {'width': 5, 'height': 2, 'font': ('Arial', 14, 'bold'), 'bg': '#ff9500', 'fg': 'white', 'relief': 'flat', 'activebackground': '#ffaa33'}
spec_config = {'width': 5, 'height': 2, 'font': ('Arial', 14, 'bold'), 'bg': '#a5a5a5', 'fg': 'black', 'relief': 'flat', 'activebackground': '#d4d4d4'}

# --- ROW 1 ---
Button(window, text='7', **num_config, command=lambda: click(7)).place(x=20, y=110)
Button(window, text='8', **num_config, command=lambda: click(8)).place(x=100, y=110)
Button(window, text='9', **num_config, command=lambda: click(9)).place(x=180, y=110)
Button(window, text='/', **op_config,  command=lambda: click('/')).place(x=260, y=110)

# --- ROW 2 ---
Button(window, text='4', **num_config, command=lambda: click(4)).place(x=20, y=180)
Button(window, text='5', **num_config, command=lambda: click(5)).place(x=100, y=180)
Button(window, text='6', **num_config, command=lambda: click(6)).place(x=180, y=180)
Button(window, text='*', **op_config,  command=lambda: click('*')).place(x=260, y=180)

# --- ROW 3 ---
Button(window, text='1', **num_config, command=lambda: click(1)).place(x=20, y=250)
Button(window, text='2', **num_config, command=lambda: click(2)).place(x=100, y=250)
Button(window, text='3', **num_config, command=lambda: click(3)).place(x=180, y=250)
Button(window, text='-', **op_config,  command=lambda: click('-')).place(x=260, y=250)

# --- ROW 4 ---
Button(window, text='C', **spec_config, command=clear).place(x=20, y=320)
Button(window, text='0', **num_config, command=lambda: click(0)).place(x=100, y=320)
Button(window, text='=', **op_config,  command=calculate).place(x=180, y=320)
Button(window, text='+', **op_config,  command=lambda: click('+')).place(x=260, y=320)

window.mainloop()