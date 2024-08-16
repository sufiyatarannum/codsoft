from tkinter import *

def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            value.set(eval(value.get()))
        except Exception as e:
            value.set("Error")
    elif text == "C":
        value.set("")
    else:
        value.set(value.get() + text)
    
    screen.update()

root = Tk()
root.geometry("644x900")
root.title("CALCULATOR")

value = StringVar()
value.set("")
screen = Entry(root, textvar=value, font='lucida 20 bold')
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

# First row of buttons
f = Frame(root, bg="grey")
for text in ["9", "8", "7"]:
    b = Button(f, text=text, padx=28, pady=22, font='lucida 15 bold')
    b.pack(side=LEFT, padx=18, pady=12)
    b.bind("<Button-1>", click)
f.pack()

# Second row of buttons
f = Frame(root, bg="grey")
for text in ["6", "5", "4"]:
    b = Button(f, text=text, padx=28, pady=22, font='lucida 15 bold')
    b.pack(side=LEFT, padx=18, pady=12)
    b.bind("<Button-1>", click)
f.pack()

# Third row of buttons
f = Frame(root, bg="grey")
for text in ["3", "2", "1"]:
    b = Button(f, text=text, padx=28, pady=22, font='lucida 15 bold')
    b.pack(side=LEFT, padx=18, pady=12)
    b.bind("<Button-1>", click)
f.pack()

# Fourth row of buttons
f = Frame(root, bg="grey")
for text in ["0", "+", "*"]:
    b = Button(f, text=text, padx=28, pady=22, font='lucida 15 bold')
    b.pack(side=LEFT, padx=18, pady=12)
    b.bind("<Button-1>", click)
f.pack()

# Fifth row of buttons
f = Frame(root, bg="grey")
for text in ["/", "=","C"]:
    b = Button(f, text=text, padx=28, pady=22, font='lucida 15 bold')
    b.pack(side=LEFT, padx=18, pady=12)
    b.bind("<Button-1>", click)
f.pack()



root.mainloop()
