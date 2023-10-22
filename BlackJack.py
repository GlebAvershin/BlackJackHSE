
from graphics import *
from GamePlay import *

def main():
    win = GraphWin("Blackjack", 500, 200)
    win.setCoords(0,200,415,0)
    win.setBackground("grey")

    # Draw the table
    table = Rectangle(Point(400,153),Point(87,27))
    table.setFill("brown")
    table.draw(win)

    Game(win)

    win.close()

if __name__ == "__main__":
    main()
