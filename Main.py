import random
import tkinter as tk

from PIL import ImageTk, Image


# noinspection PyPep8Naming
class BasicGui:

    def __init__(self):
        self.imagerefs = set()
        self.mainWindow = self.configurewindow()
        self.canvas = self.createCanvas()

        self.soccerball = self.createImageFromFile("sprites/soccer.PNG", 75, 100)
        self.turtle = self.createImageFromFile("sprites/Possessed boi.png", 900, 100)
        self.createStaticImageFromFile("sprites/pal.png", -100, 100)

        self.lives = 3
        self.livestext = self.updateLives(self.lives)

        # Score
        self.score = 0
        self.scoretext = self.updateScore(self.score)

        self.bindKeys()

    def configurewindow(self):
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

    def createStaticImageFromFile(self, image, x, y):
        tkimage = ImageTk.PhotoImage(Image.open(image))
        self.imagerefs.add(tkimage)
        tk.Label(self.mainWindow, image=tkimage).place(x=x, y=y)

    def updateLives(self, lives):
        self.lives = lives
        self.livestext = self.canvas.create_text(50, 20, text=str(self.lives) + " Lives Remaining")
        return self.livestext

    def updateScore(self, score):
        self.score = score
        self.scoretext = self.canvas.create_text(50, 30, text="High Score: " + str(self.score))
        return self.scoretext

    def bindKeys(self):
        self.mainWindow.bind("s", self.moveBallDown)
        self.mainWindow.bind("w", self.moveBallUp)
        self.mainWindow.bind("d", self.moveBallRight)
        self.mainWindow.bind('a', self.moveBallLeft)

    def moveBallDown(self, event):
        self.canvas.move(self.soccerball, 0, 5)

    def moveBallUp(self, event):
        self.canvas.move(self.soccerball, 0, -5)

    def moveBallLeft(self, event):
        self.canvas.move(self.soccerball, -5, 0)

    def moveBallRight(self, event):
        self.canvas.move(self.soccerball, 5, 0)

    # def moveTurtle(self):
    #     turtlecoords = self.canvas.coords(self.turt)
    #     self.canvas.move(self.turt, -10, random.randint(-100, 100))
    #     if turtlecoords[0] > 400:
    #         self.mainWindows.after(200, self.moveTurtle)
    #     else:
    #         self.setLives(self.lives - 1)

    def setLives(self, lives):
        self.canvas.delete(self.livestext)
        self.canvas.create_text(50, 20, text=str(self.lives) + " Lives Remaining")
        # self.laterDude()

    # def laterDude(self):
    #     self.mainWindows.after(300, self.canvas.delete(self.turt))

    def hitTurtle(self):
        turtlecoord = self.canvas.coords(self.turt)
        ballcoord = self.canvas.coords(self.soccerball)
        if turtlecoord == ballcoord:
            self.score += 10
            self.mainWindow.after(200, self.mainWindow.update)
            self.mainWindow.after(300, self.canvas.delete(self.turt))

    def run(self):
        self.mainWindow.mainloop()

    def quitCallback(self):
        self.mainWindow.destroy()


myGui = BasicGui()
myGui.run()
