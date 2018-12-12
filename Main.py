import functools
import random
import tkinter as tk
from tkinter import messagebox

from PIL import ImageTk, Image


# noinspection PyPep8Naming
class BasicGui:

    def __init__(self):
        self.imagerefs = set()
        self.mainWindow = self.configurewindow()
        self.canvas = self.createCanvas()

        self.soccerball = self.createImageFromFile("sprites/soccer.PNG", 75, 100)
        self.turtleSet = self.createTurtleSet(1)
        self.createStaticImageFromFile("sprites/pal.png", -100, 100)

        self.lives = 3
        self.livestext = self.updateLives(self.lives)

        self.score = 0
        self.scoretext = self.updateScore(self.score)

        self.bindKeys()
        self.moveTurtles()

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

    def createTurtleSet(self, maxNumber):
        return set([self.createTurtle() for _ in range(maxNumber)])

    def createTurtle(self):
        return self.createImageFromFile("sprites/Possessed boi.png", 900, 100)

    def createStaticImageFromFile(self, image, x, y):
        tkimage = ImageTk.PhotoImage(Image.open(image))
        self.imagerefs.add(tkimage)
        tk.Label(self.mainWindow, image=tkimage).place(x=x, y=y)

    def updateLives(self, lives):
        self.lives = lives

        try:
            self.canvas.delete(self.livestext)
        except:
            print("Initializing!")

        self.livestext = self.canvas.create_text(70, 20, text=str(self.lives) + " Lives Remaining")
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

    def setLives(self, lives):
        self.canvas.delete(self.livestext)
        self.canvas.create_text(50, 20, text=str(self.lives) + " Lives Remaining")

    def turtleHitPlayer(self):
        self.updateLives(self.lives - 1)
        if self.lives <= 0:
            self.gameOver()

    def moveTurtles(self):
        for turtle in self.turtleSet:
            self.canvas.move(turtle, -10, random.randint(-100, 100))
            self.removeTurtleThatTouchesBall(turtle)

        if min([self.canvas.coords(t)[0] for t in self.turtleSet]) > 400:
            self.mainWindow.after(200, self.moveTurtles)
        else:
            self.turtleHitPlayer()

    def removeTurtleThatTouchesBall(self, turtle):
        if self.checkTurtleCollision(turtle):
            self.canvas.delete(turtle)

    def checkTurtleCollision(self, turtle):
        print(self.canvas.find_above(self.soccerball))
        print(turtle)
        return False

    # def laterDude(self):
    #     self.mainWindows.after(300, self.canvas.delete(self.turt))

    # def hitTurtle(self):
    #     turtlecoord = self.canvas.coords(self.turt)
    #     ballcoord = self.canvas.coords(self.soccerball)
    #     if turtlecoord == ballcoord:
    #         self.score += 10
    #         self.mainWindow.after(200, self.mainWindow.update)
    #         self.mainWindow.after(300, self.canvas.delete(self.turt))

    def gameOver(self):
        """Runs when player has lost all of their lives to inform them that they lost and ask if they want to play again."""
        if self.lives == 0:
            warning = "Game Over"
            messagebox.showwarning(warning, "You Lose!")
            again = messagebox.askretrycancel("Play again",
                                              "Do you want to try again? Or do you give up when the going gets tough?")
            if again:
                myGui.run()
            else:
                self.quitCallBack()
        else:
            pass

    def winner(self):
        """Runs when the player defeats the last enemy turtle.
        Congratulates them on winning and asks if they'd like to play again"""
        if turtleLife == 0:
            congrats = "You Win!! You Saved The Women's World Cup!"
            messagebox.showinfo("Congratulations", congrats)
            ask = messagebox.askretrycancel("Play Again", "Click retry to return to start")
            if ask:
                myGui.run()
            else:
                pass
                self.quitCallBack()
        else:
            pass

    def run(self):
        self.mainWindow.mainloop()

    def quitCallback(self):
        self.mainWindow.destroy()


def intro():
    """Creates the GUI and walks user through a tutorial of gameplay, allowing the user to start the game."""
    messagebox.showinfo("Welcome", "Welcome to TURTLE SOCCER SMASH SISTERS")
    ans = messagebox.askyesnocancel("Start Game", "Do you need a tutorial?")
    print(ans)
    if ans:
        win = tk.Tk()
        win.title("Tutorial")
        L = tk.Label(win, text="Use the 'w' key to move your aim up. Use the 's' key to move it down.\n" +
                               "Press d to go right and a to go left.\n You have three lives to defeat your"
                               " turtle enemy. Good luck!",
                     bg="light green", bd=5, relief=tk.SUNKEN, padx=100, pady=100)
        L.grid(row=1, column=2)
        win.mainloop()
    else:
        play = messagebox.askyesno("Start Game", "Start Gameplay?")
        if play:
            myGui = BasicGui()
            # myGui.run()
        else:
            messagebox.showinfo("Welcome", "Welcome to TURTLE SOCCER SMASH SISTERS")

myGui = BasicGui()
myGui.run()
# intro()