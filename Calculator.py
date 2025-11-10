import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("500x500")

answer = Text(width=50, height=3)
answer.place(x = 50, y = 50)

def show(x):
    try:
        if x == "=":
            final_answer = eval(answer.get(1.0, "end-lc"))
            answer.insert(tk.INSERT, x)
            answer.insert(tk.INSERT, final_answer)
        else:
            answer.insert(tk.INSERT, x)
        if x == "C":
            answer.delete(1.0, END)
    except:
        answer.delete(1.0, END)


b1 = Button(top, text="1", width=10, height=5, command=lambda: show("1"))
b1.place(x = 70, y = 120)

b2 = Button(top, text="2", width=10, height=5, command=lambda: show("2"))
b2.place(x = 170, y = 120)

b3 = Button(top, text="3", width=10, height=5, command=lambda: show("3"))
b3.place(x = 270, y = 120)

b4 = Button(top, text="4", width=10, height=5, command=lambda: show("4"))
b4.place(x = 70, y = 220)

b5 = Button(top, text="5", width=10, height=5, command=lambda: show("5"))
b5.place(x = 170, y = 220)

b6 = Button(top, text="6", width=10, height=5, command=lambda: show("6"))
b6.place(x = 270, y = 220)

b7 = Button(top, text="7", width=10, height=5, command=lambda: show("7"))
b7.place(x = 70, y = 320)

b8 = Button(top, text="8", width=10, height=5, command=lambda: show("8"))
b8.place(x = 170, y = 320)

b9 = Button(top, text="9", width=10, height=5, command=lambda: show("9"))
b9.place(x = 270, y = 320)

bmulti = Button(top, text="*", width=10, height=2, command=lambda: show("*"))
bmulti.place(x = 370, y = 120)

bdivide = Button(top, text="/", width=10, height=2, command=lambda: show("/"))
bdivide.place(x = 370, y = 170)

badd = Button(top, text="+", width=10, height=2, command=lambda: show("+"))
badd.place(x = 370, y = 220)

bminus = Button(top, text="-", width=10, height=2, command=lambda: show("-"))
bminus.place(x = 370, y = 270)

bequal = Button(top, text="=", width=10, height=2, command=lambda: show("="))
bequal.place(x = 370, y = 320)

bC =Button(top, text="C", width=10, height=2, command=lambda: show("C"))
bC.place(x = 370, y = 370)

top.mainloop()