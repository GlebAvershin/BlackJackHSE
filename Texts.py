
from graphics import *

class Scorebox(Text):
    def __init__(self, win, center,text,value):
        x = center.getX()
        y = center.getY()

        self.text = Text(Point(x-15,y), text)
        self.text.setSize(12)
        self.text.draw(win)

        self.value = self.text.clone()
        self.value.move(30,0)
        self.value.setText(value)
        self.value.draw(win)

    def updateText(self,new_value):
        if self.value.getText() == new_value:
            pass
        else:
            self.value.setText(new_value)
            for i in range(2):
                time.sleep(0.1)

                if i % 2 == 0:
                    self.value.setStyle('bold')
                else:
                    self.value.setStyle('normal')

def FlashyText(win,center,text,timing):
    winner = Text(center,text)
    winner.setFace("arial")
    winner.setFill("black")
    winner.setSize(30)
    for i in range(1,6):
        time.sleep(timing)
        if i % 2 == 0:
            winner.draw(win)
        else:
            winner.undraw()
