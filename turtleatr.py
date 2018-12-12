import random
import time

def lives():
    """This function figures out how many lives are left and will end the game once the lives run out"""
    # a lot of this is a placeholder because I don't have the other pieces it needs
    life = 5
    while life>0:
        if input("rip"): #representing when the turtle gets to half the screen
            life=life-1
            print("You have lost a life! you now have",life,"lives.")

        if life == 0:
            print("Ok you're dead thanks for playing")

# lives()


def goturtle():
    """This function figures out the path of a turtle."""
    #Again placeholders
    x=1000
    while x>400:
        x = x - 10
        y = random.randint(400,1000)
        return x, y
def holdinfo():
    turtleinfo={}
