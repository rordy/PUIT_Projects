6

# plot a function like y = sin(x) with Tkinter canvas and line

import tkinter as tk
import math

root = tk.Tk()
root.title("Simple plot using canvas and line")

width = 400
height = 300
center = height//2
x_increment = 1
# width stretch
x_factor = 0.04
# height stretch
y_amplitude = 80


c = tk.Canvas(width=width, height=height)
c.pack()


image = c.create_rectangle(50,0,0,50, fill ='red')
str1 = "sin(x)=blue"
c.create_text(10, 20, anchor=tk.SW, text=str1)

#center_line = c.create_line(0, center, width, center, fill='green')

# create the coordinate list for the sin() curve, have to be integers
xy1 = []
for x in range(400):
    # x coordinates
    xy1.append(x * x_increment)
    # y coordinates
    xy1.append(int(math.sin(x * x_factor) * y_amplitude) + center)

#image = c.create_image(0,0,anchor=tk.NW, image=img)

DELAY = 100

#print("TEST",xy1[1])

def move_b():
    for x in range(0, 200,2):
        c.after(DELAY,c.move(image, xy1[x], xy1[x+1]))
    # move again after 25ms (0.025s)
    #root.after(25, move_b)


move_b()


#sin_line = c.create_line(xy1, fill='blue')
root.mainloop()