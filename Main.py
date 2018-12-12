import tkinter as tk
from PIL import ImageTk, Image
import turtleatr
import time
import random


class BasicGui:

    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.configure(background='white')
        # Christine
        self.pal = ImageTk.PhotoImage(Image.open("sprites/pal.png"))
        palLabel = tk.Label(self.mainWin, image=self.pal)
        palLabel.place(x=-100, y=100)

        # Soccer ball
        self.soccer = ImageTk.PhotoImage(Image.open("sprites/soccer.PNG"))
        self.canvas = tk.Canvas(bg='white', width=2000, height=950)
        self.canvas.place(x=150, y=0)
        self.x = 75
        self.y = 100
        self.ball = self.canvas.create_image(self.x, self.y, image=self.soccer)  # switch to canvas create imag
        # Turtle
        self.turtle = ImageTk.PhotoImage(Image.open("sprites/Possessed boi.png"))
        self.turtx = 900
        self.turty = 100
        self.turt = self.canvas.create_image(self.turtx, self.turty, image=self.turtle)
        self.moveTurt()
        # Lives
        self.setLives(3)
        # Score
        self.lives = lives
        self.score = 0
        self.canvas.create_text(50, 30, text="High Score: " + str(self.score))
        # binding:
        self.mainWin.bind("s", self.down)
        self.mainWin.bind("w", self.up)
        self.mainWin.bind("d", self.right)
        self.mainWin.bind('a', self.left)

    def down(self, event):
        self.canvas.move(self.ball, 0, 5)
        self.y += 5

    def up(self, event):
        self.canvas.move(self.ball, 0, -5)
        self.y += -5

    def left(self, event):
        self.canvas.move(self.ball, -5, 0)
        self.x -= 5

    def right(self, event):
        self.canvas.move(self.ball, 10, 0)
        # self.mainWin.after(600, self.returnBall)

    def moveTurt(self):
        turtlecoords = self.canvas.coords(self.turt)
        self.canvas.move(self.turt, -10, random.randint(-100, 100))
        if turtlecoords[0] > 400:
            self.mainWin.after(200, self.moveTurt)
        else:
            self.setLives(self.lives-1)

    def setLives(self, lives):
        self.canvas.delete(self.livetext)
        self.canvas.create_text(50, 20, text=str(self.lives) + " Lives Remaining")
        self.laterDude()

    def laterDude(self):
        self.mainWin.after(300, self.canvas.delete(self.turt))

    def hitTurtle(self):
        turtlecoord = self.canvas.coords(self.turt)
        ballcoord = self.canvas.coords(self.ball)
        if turtlecoord == ballcoord:
            self.score += 10
            self.mainWin.after(200, self.mainWin.update)
            self.mainWin.after(300, self.canvas.delete(self.turt))

    def run(self):
        self.mainWin.mainloop()

    def quitCallback(self):
        self.mainWin.destroy()


myGui = BasicGui()
myGui.run()
