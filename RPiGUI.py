from tkinter import *
import tkinter.font

from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## DEF ##
red = LED(26)
grn = LED(19)
blu = LED(13)

## GUI ##
win = Tk()
win.title("LED")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12)

## FUNCTIONS ##
def redToggle():
    grn.off()
    blu.off()
    red.on()
        
def grnToggle():
    red.off()
    blu.off()
    grn.on()
        
def bluToggle():
    red.off()
    grn.off()
    blu.on()

def close():
    RPi.GPIO.cleanup()
    win.destroy()

## WIDGET ##
redButton = Button(win, text = 'Turn on RED', font = myFont, command = redToggle, bg = 'bisque2', height = 1, width = 24)
grnButton = Button(win, text = 'Turn on GREEN', font = myFont, command = grnToggle, bg = 'bisque2', height = 1, width = 24)
bluButton = Button(win, text = 'Turn on BLUE', font = myFont, command = bluToggle, bg = 'bisque2', height = 1, width = 24)

redButton.grid(row=0, column = 1)
grnButton.grid(row=1, column = 1)
bluButton.grid(row=2, column = 1)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()
