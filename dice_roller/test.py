import random
from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Dice Roller")
root.geometry("550x300+300+150")
root.resizable(width=True, height=True)


def open_img():
    throw = random.randint(1, 6)
    if throw == 1:
        img = Image.open("one.jpg")  # open image
        img = img.resize((250, 250), Image.ANTIALIAS)  # resize to make all images a similar size
        img = ImageTk.PhotoImage(img)  # convert to ImageTk object which supports jpg, png etc.
        panel['image'] = img # assign to image panel in frame
        panel.image = img #
        panel.pack()
    if throw == 2:
        img = Image.open("two.png")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel['image'] = img
        panel.image = img
        panel.pack()
    if throw == 3:
        img = Image.open("three.png")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel['image'] = img
        panel.image = img
        panel.pack()
    if throw == 4:
        img = Image.open("four.png")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel['image'] = img
        panel.image = img
        panel.pack()
    if throw == 5:
        img = Image.open("five.png")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel['image'] = img
        panel.image = img
        panel.pack()
    if throw == 6:
        img = Image.open("6.png")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel['image'] = img
        panel.image = img
        panel.pack()


panel = Label(root)
btn = Button(root, text='Throw Dice', command=open_img).pack()

root.mainloop()
