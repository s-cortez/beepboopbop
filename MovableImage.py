from PIL import ImageTk, Image


class MovableImage:

    def __init__(self, canvas, imagesrc, x, y):
        self.canvas = canvas

        self.imagesrc = imagesrc

        self.tkimage = None
        self.canvasimage = self.createImage(x, y)
        self.size = (self.tkimage.width(), self.tkimage.height())

        self.movementScaling = 50

    def createImage(self, x, y):
        self.tkimage = ImageTk.PhotoImage(Image.open(self.imagesrc))
        return self.canvas.create_image(x, y, image=self.tkimage)

    def moveUp(self, event):
        self.canvas.move(self.canvasimage, 0, -self.movementScaling)

    def moveDown(self, event):
        self.canvas.move(self.canvasimage, 0, self.movementScaling)

    def moveLeft(self, event):
        self.canvas.move(self.canvasimage, -self.movementScaling, 0)

    def moveRight(self, event):
        self.canvas.move(self.canvasimage, self.movementScaling, 0)

    def coords(self):
        return self.canvas.coords(self.canvasimage)

    def delete(self):
        self.tkimage = None
