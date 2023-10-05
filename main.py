# I'm going to recreate the snake game without using any imports and just printing off the game
# It will be a 10x10 game but I will make it dynamically scaled

from snake import *

def main():
    # Create the dict to store the screen
    initialScreen()

    # Create the starting point of the snake
    snake

def initialScreen():
    screen: dict = {}

    xSize = 10
    ySize = 10

    dashes = 22

    print(" " + "-"*dashes)

    for y in range(ySize):
        print("| " + "  " * xSize + "|")

    print(" " + "-"*dashes)

main()