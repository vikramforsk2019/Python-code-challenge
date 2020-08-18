
from math import pi
from tkinter import *
import tkinter as tk
root = Tk()

#Label
radiusLabel = Label(root, text="Enter the radius(m): ")
radiusLabel.grid(row=0,column=0)

radiusLabel = Label(root, text="Enter the side(m): ")
radiusLabel.grid(row=0,column=1)
#Entering the radius
radiusEntry = Entry(root)
radiusEntry.grid(row=1, column=0)
#Entering the side
sideEntry = Entry(root)
sideEntry.grid(row=1, column=1)
#Canvas 
canvas = Canvas(width=800,height=500, bg="#cedbd2")
canvas.grid(row=2,column=0)


#Drawing the circle
def circle():
    x1=100
    y1=100
    r = 0
    if radiusEntry.get():
        r = int(radiusEntry.get())
    label3 = tk.Label(root, text= 'The Area of Circle ' + str(r) + ' is:',font=('helvetica', 10))
    canvas.create_window(200, 210, window=label3)
    label4 = tk.Label(root, text= round(pi * r**2,2),font=('helvetica', 10, 'bold'))
    canvas.create_window(200, 230, window=label4)
    id = canvas.create_oval(x1-r,y1-r,x1+r,y1+r, fill="pink")

#Drawing the square
def square():
	x2=700
	y2=100
	a=0
	if sideEntry.get():
		a = int(sideEntry.get())
	label3 = tk.Label(root, text= 'The Area of square ' + str(a) + ' is:',font=('helvetica', 10))
	canvas.create_window(700, 210, window=label3)
	label4 = tk.Label(root, text= str(a*a),font=('helvetica', 10, 'bold'))
	canvas.create_window(700, 230, window=label4)
	id = canvas.create_rectangle(x2-a, y2-a, x2+a, y2+a, fill="blue", outline = 'black')
#Calling the function for drawing the circle button
radiusButton = Button(root, text="Create Circle", command=circle)
radiusButton.grid(row=2,column=0)
radiusButton = Button(root, text="Create Square", command=square)
radiusButton.grid(row=2,column=1)


root.mainloop()