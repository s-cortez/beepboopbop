import random
import tkinter as tk
from tkinter import messagebox

from PIL import ImageTk, Image

import MovableImage


# noinspection PyPep8Naming
class BasicGui:

    def __init__(self):
        self.imagerefs = set()
        self.mainWindow = self.configurewindow()
        self.canvas = self.createCanvas()

        self.soccerball = self.createMovableImage("sprites/soccer.PNG", 75,
                                                  100)  # .createImage(75, 100) #self.createImageFromFile("sprites/soccer.PNG", 75, 100)
        self.turtleSet = self.createTurtleSet(5)
        self.turtleDeleteSet = set()
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

    def createMovableImage(self, image, x, y):
        return MovableImage.MovableImage(self.canvas, image, x, y)

    def createTurtleSet(self, maxNumber):
        return set([self.createTurtle() for _ in range(maxNumber)])

    def createTurtle(self):
        return self.createMovableImage("sprites/Possessed boi.png", 900, 100)

    def createStaticImageFromFile(self, image, x, y):
        tkimage = ImageTk.PhotoImage(Image.open(image))
        self.imagerefs.add(tkimage)
        tk.Label(self.mainWindow, image=tkimage).place(x=x, y=y)

    def updateLives(self, lives):
        self.lives = lives

        try:
            self.canvas.delete(self.livestext)
        except:
            print("Initializing lives!")

        self.livestext = self.canvas.create_text(70, 20, text=str(self.lives) + " Lives Remaining")
        return self.livestext

    def updateScore(self, score):
        self.score = score

        try:
            self.canvas.delete(self.scoretext)
        except:
            print("Initializing score!")

        self.scoretext = self.canvas.create_text(50, 30, text="High Score: " + str(self.score))
        return self.scoretext

    def bindKeys(self):
        self.mainWindow.bind("s", self.soccerball.moveDown)
        self.mainWindow.bind("w", self.soccerball.moveUp)
        self.mainWindow.bind("d", self.soccerball.moveRight)
        self.mainWindow.bind('a', self.soccerball.moveLeft)

    def setLives(self, lives):
        self.canvas.delete(self.livestext)
        self.canvas.create_text(50, 20, text=str(self.lives) + " Lives Remaining")

    def turtleHitPlayer(self):
        self.updateLives(self.lives - 1)
        if self.lives <= 0:
            self.gameOver()

    def moveTurtles(self):
        for turtle in self.turtleSet:
            self.canvas.move(turtle.canvasimage, -10, random.randint(-100, 100))
            self.removeTurtleThatTouchesBall(turtle)
        self.turtleSet.difference_update(self.turtleDeleteSet)
        self.updateScore(self.score+len(self.turtleDeleteSet)*10)
        self.turtleDeleteSet = set()

        if self.turtleSet:
            if min([self.canvas.coords(t.canvasimage)[0] for t in self.turtleSet]) > 400:
                self.mainWindow.after(200, self.moveTurtles)
            else:
                self.turtleHitPlayer()
        else:
            self.winner()

    def removeTurtleThatTouchesBall(self, turtle):
        if self.checkTurtleCollision(turtle):
            self.deleteTurtle(turtle)

    def checkTurtleCollision(self, turtle):
        return self.oneDimCollision(self.soccerball.coords()[0], self.soccerball.coords()[0] + self.soccerball.size[0],
                                    turtle.coords()[0], turtle.coords()[0] + turtle.size[0]) and self.oneDimCollision(
            self.soccerball.coords()[1], self.soccerball.coords()[1] + self.soccerball.size[1], turtle.coords()[1],
            turtle.coords()[1] + turtle.size[1])

    def oneDimCollision(self, bx1, bx2, tx1, tx2):
        return bx1 < tx1 < bx2 or bx1 < tx2 < bx2 or (bx1 > tx1 and bx2 < tx2) or (bx1 < tx1 and bx2 > tx2)

    def deleteTurtle(self, turtle):
        self.turtleDeleteSet.add(turtle)
        self.canvas.delete(turtle.canvasimage)

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

        congrats = "You Win!! You Saved The Women's World Cup!"
        messagebox.showinfo("Congratulations", congrats)
        ask = messagebox.askretrycancel("Play Again", "Click retry to return to start")
        if ask:
            myGui.run()
        else:
            pass
            self.quitCallback()


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
