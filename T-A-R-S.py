from tkinter import *
#import RPi.GPIO as gpio
import time
import sys
#from sensor import distance
import random

root = Tk()
root.title("T.A.R.S.")
root.geometry("200x200")

def forward(event):
    print("pressed", repr(event.char))
    key_press = event.char

    if key_press.lower() == 'w':
        print("Forward as she goes")
    elif key_press.lower() == 's':
        print("back dat shit up")
    elif key_press.lower() == 'a':
        print("Links muthatrucka")
    elif key_press.lower() == 'd':
        print("Recht muthatrucka")
    else:
        pass

f_btn = Button(root, text="FWD", command= forward)
f_btn.bind("<Key>", forward)
f_btn.grid(row=3, column=2, pady=10)
b_btn = Button(root, text="BACK")
b_btn.grid(row=5, column=2, pady=10)
l_btn = Button(root, text="LEFT")
l_btn.grid(row=4, column=1, pady=10)
r_btn = Button(root, text="RIGHT")
r_btn.grid(row=4, column=3, pady=10)
button4 = Button(root, text="Shut er Down", command=root.destroy)
button4.grid(row=6, column=5, pady=10)


root.mainloop()