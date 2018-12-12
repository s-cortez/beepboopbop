import random
import tkinter as tk

from PIL import ImageTk, Image


class BasicGui:

    def __init__(self):
        self.imagerefs = set()
        self.mainWindows = self.configureWindow()
        self.canvas = self.createCanvas()

        # Christine
        self.pal = ImageTk.PhotoImage(Image.open("sprites/pal.png"))
        palLabel = tk.Label(self.mainWindows, image=self.pal)
        palLabel.place(x=-100, y=100)

        self.soccerball = self.createImageFromFile("sprites/soccer.PNG", 75, 100)

        # Turtle
        self.turtle = ImageTk.PhotoImage(Image.open("sprites/Possessed boi.png"))
        self.turtx = 900
        self.turty = 100
        self.turt = self.canvas.create_image(self.turtx, self.turty, image=self.turtle)
        self.moveTurtle()
        # Lives
        self.lives = 3
        self.livetext = self.canvas.create_text(50, 20, text=str(self.lives) + " Lives Remaining")
        self.setLives(3)

        # Score
        self.score = 0
        self.canvas.create_text(50, 30, text="High Score: " + str(self.score))
        # binding:
        self.mainWindows.bind("s", self.moveBallDown)
        self.mainWindows.bind("w", self.moveBallUp)
        self.mainWindows.bind("d", self.moveBallRight)
        self.mainWindows.bind('a', self.moveBallLeft)

    def configureWindow(self):
        mainwindow = tk.Tk()
        mainwindow.configure(background='white')
        return mainwindow

    def createCanvas(self):
        canvas = tk.Canvas(bg='white', width=2000, height=950)
        canvas.place(x=150, y=0)
        return canvas

    def createImageFromFile(self, image, x, y):
        tkimage = ImageTk.PhotoImage(Image.open(image))
        self.imagerefs.add(tkimage)
        return self.canvas.create_image(x, y, image=tkimage)

    def moveBallDown(self, event):
        self.canvas.move(self.soccerball, 0, 5)

    def moveBallUp(self, event):
        self.canvas.move(self.soccerball, 0, -5)

    def moveBallLeft(self, event):
        self.canvas.move(self.soccerball, -5, 0)

    def moveBallRight(self, event):
        self.canvas.move(self.soccerball, 10, 0)
        # self.mainWin.after(600, self.returnBall)

    def moveTurtle(self):
        turtlecoords = self.canvas.coords(self.turt)
        self.canvas.move(self.turt, -10, random.randint(-100, 100))
        if turtlecoords[0] > 400:
            self.mainWindows.after(200, self.moveTurtle)
        else:
            self.setLives(self.lives - 1)

    def setLives(self, lives):
        self.canvas.delete(self.livetext)
        self.canvas.create_text(50, 20, text=str(self.lives) + " Lives Remaining")
        self.laterDude()

    def laterDude(self):
        self.mainWindows.after(300, self.canvas.delete(self.turt))

    def hitTurtle(self):
        turtlecoord = self.canvas.coords(self.turt)
        ballcoord = self.canvas.coords(self.soccerball)
        if turtlecoord == ballcoord:
            self.score += 10
            self.mainWindows.after(200, self.mainWindows.update)
            self.mainWindows.after(300, self.canvas.delete(self.turt))

    def run(self):
        self.mainWindows.mainloop()

    def quitCallback(self):
        self.mainWindows.destroy()


myGui = BasicGui()
myGui.run()
