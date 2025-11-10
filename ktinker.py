import tkinter

root = tkinter.Tk()
root.resizable(False, False)

myCanvas = tkinter.Canvas(root, bg="black", height=500, width = 800)

shape1 = myCanvas.create_oval(200, 250, 300, 300, fill="blue")

myCanvas.pack()
root.mainloop()
