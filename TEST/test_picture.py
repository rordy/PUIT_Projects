import tkinter as tk
import math
import time

root = tk.Tk()

canvas = tk.Canvas(root, width=800, height = 800)
canvas.pack()

img = tk.PhotoImage(file="test.png")
image = canvas.create_image(0,674,anchor=tk.NW, image=img)

def move(event):
    if event.char =="a":
        i = range(-1,1)
        print(i)
        canvas.move(image, math.sin(i))
        print(i)
    return

root.bind("<Key>",move)

root.mainloop()