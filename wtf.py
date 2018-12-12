import tkinter as tk
from PIL import Image, ImageTk
class gui:
    def init(self):
        self.mainWin = tk.Tk()
        self.mainWin.configure(background='white')
        self.soccer = ImageTk.PhotoImage(Image.open("sprites/soccer.PNG"))
        self.canvas = tk.Canvas(bg='white', width=170, height=140)
        # canvas.pack()
        # canvas.grid(row=2, column=2)
        self.canvas.place(x=150, y=200)
        ball = self.canvas.create_image(image=self.soccer, bg='white')  # switch to canvas create imag
        canx = 100
        self.canvas.create_window(canx, 100, window=ball)
    def run(self):
        self.mainWin.mainloop()

gui= gui()
gui.run()