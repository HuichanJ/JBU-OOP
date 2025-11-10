import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("500x500")


class Queue:
    answer = Text(width=50, height=3)
    answer.place(x=50, y=50)

    andEn = Text(width=15, height=3)
    andEn.place(x=300, y=200)

    def __init__(self):
        self.answer.insert(tk.INSERT, "Queue Created")
        self.q = []

    def enqueue(self):
        self.q.append(self.andEn.get(1.0, END))
        self.andEn.delete("1.0", END)
        for x in range(self.q):
            self.answer.insert(tk.INSERT, x)

    def dequeue(self):
        self.q.pop(0)
        for x in range(self.q):
            self.answer.insert(tk.INSERT, x)


que = Queue()
def que():
    que = Queue()
    

b1 = Button(top, text="Create Queue", width=10, height=5, command=lambda: que())
b1.place(x = 70, y = 120)

b2 = Button(top, text="Enqueue", width=10, height=5, command=lambda: que.enqueue())
b2.place(x = 70, y = 220)

b3 = Button(top, text="Dequeue", width=10, height=5, command=lambda: dequeue())
b3.place(x = 70, y = 320)


top.mainloop()

