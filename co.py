import tkinter
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


win = Tk()
win.title("Image Viewer")
win.geometry()
win.configure(bg="black")



def btnOp():
    global files
    global img1
    files = filedialog.askopenfilename()
    img1 = ImageTk.PhotoImage(file=files)
    lbl = Label(image=img1, bg="black")
    lbl.grid(row=0, column=0, columnspan=2)

btnback = Button(win, text="Open", command=btnOp,bg="black", fg="Green" )
btne = Button(win, text="Exit", command=win.quit,bg="black", fg="Green" )
th = Label(win, text="Please open an image",bg = "black",fg="green")

btnback.grid(row=1, column=0, sticky="NSEW",columnspan=1)
btne.grid(row=1, column=1, sticky="NSEW",columnspan=1)
th.grid(row=0, column=0 )
win.resizable(False,False)
win.mainloop()