import tkinter

root = tkinter.Tk()
root .resizeable(False, False)

myCanvas = tkinter.Canvas(root, bg="black", height=500, width = 800)

shape1 = myCanvas.creat_oval(200, 250, 300, 300, fill="blue")

myCanvas.pack()
root.mainloop()
