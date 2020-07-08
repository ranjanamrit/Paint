from tkinter import *   
from tkinter.colorchooser import askcolor

class Paint(object):
    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()

        self.penButton = Button(self.root, text= 'Pen', command=self.usePen)
        self.penButton.grid(row=0, column=0)

        self.brushButton = Button(self.root, text= 'Brush', command=self.useBrush)
        self.brushButton.grid(row=0, column=1)

        self.colorButton = Button(self.root, text= 'Colour', command=self.chooseColor)
        self.colorButton.grid(row=0, column=2)

        self.eraserButton = Button(self.root, text= 'Eraser', command=self.useEraser)
        self.eraserButton.grid(row=0, column=3)
        
        self.chooseSizeButton = Scale(self.root, from_=1, to=20 , orient=HORIZONTAL)
        self.chooseSizeButton.grid(row=0, column=4)

        self.canvas = Canvas(self.root, bg='white', width=800, height=800)
        self.canvas.grid(row=1, columnspan=5)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.oldX = None
        self.oldY = None
        self.lineWidth = self.chooseSizeButton.get()
        self.color = self.DEFAULT_COLOR
        self.eraserOn = False
        self.activeButton = self.penButton
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

    def usePen(self):
        self.activateButton(self.penButton)

    def useBrush(self):
        self.activateButton(self.brushButton)

    def chooseColor(self):
        self.eraserOn = False
        self.color = askcolor(color=self.color)[1]

    def useEraser(self):
        self.activateButton(self.eraserButton, eraserMode= True)

    def activateButton(self, someButton, eraserMode=False):
        self.activeButton.config(relief=RAISED)
        someButton.config(relief=SUNKEN)
        self.activeButton = someButton
        self.eraserOn= eraserMode

    def paint(self, event):
        self.lineWidth = self.chooseSizeButton.get()
        paintColor = 'white' if self.eraserOn else self.color
        if self.oldX and self.oldY:
            self.canvas.create_line(self.oldX, self.oldY, event.x, event.y,
                               width= self.lineWidth, fill=paintColor,
                               capstyle=ROUND, smooth= TRUE, splinesteps=40)
        self.oldX=event.x
        self.oldY=event.y

    def reset(self, event):
        self.oldX, self.oldY= None, None

if __name__ == '__main__':
    Paint()

        