from graphics2 import *
from random import *
from string import *

class Button:

    def __init__(self , x , y , width):
        self.color = "Grey"
        self.state1 = True
        self.x1 = x - width/2
        self.x2 = x + width/2
        self.y1 = y - 2
        self.y2 = y + 2
        self.point1 = Point(self.x1 , self.y1)
        self.point2 = Point(self.x2 , self.y2)
        self.graph_but = Rectangle(self.point1 , self.point2)
        self.graph_but.setFill(self.color)
        self.graph_but.setOutline(self.color)
        self.state1 = True

    def buttonText(self , text):
        self.text_but = Text( Point((float(self.x1) + self.x2)/2 , \
                               (float(self.y1) + self.y2)/2) , text)

    def buttonDraw(self , window):
        self.graph_but.draw(window)
        self.text_but.draw(window)

    def buttonActive(self , state1):
        self.state1 = state1
        if self.state1 == True:
            self.text_but.setTextColor("Black")
        else:
            self.text_but.setTextColor("darkgrey")
            
        

    def buttonClick(self , x , y):
        self.state2 = self.x1 <= x <= self.x2
        self.state3 = self.y1 <= y <= self.y2
        if self.state1 == self.state2 == self.state3 == True:
            self.graph_but.setFill("Black")
            self.text_but.setFill("White")
            for i in range(200000):
                a = 0
            self.graph_but.setFill(self.color)
            self.text_but.setFill("Black")
            return True
        else:
            return False

class Dice:

    def __init__(self , x , y , size , window):
        self.linje = [0]*4
        self.select = False
        self.window = window
        self.size = size
        self.psize = size/5
        self.x = x
        self.y = y
        self.firkant = Rectangle(Point(x - size , y - size) , \
                                 Point(x + size , y + size))
        self.firkant.setFill("White")
        self.firkant.setOutline("Black")
        self.firkant.draw(window)

    def __drawNumber(self , x , y):
        dot = Circle(Point(x , y) , self.psize)
        dot.setFill("White")
        dot.setOutline("White")
        dot.draw(self.window)
        return dot

    def diceNumber(self , number):
        dist = self.size * 0.6
        self.number = number
        self.sirkel_pos = [0]*7
        self.sirkel = ["OFF"]*7
        self.sirkel_pos[0] = self.__drawNumber(self.x - dist , self.y - dist)
        self.sirkel_pos[1] = self.__drawNumber(self.x - dist , self.y)
        self.sirkel_pos[2] = self.__drawNumber(self.x - dist , self.y + dist)
        self.sirkel_pos[3] = self.__drawNumber(self.x + dist , self.y - dist)
        self.sirkel_pos[4] = self.__drawNumber(self.x + dist , self.y)
        self.sirkel_pos[5] = self.__drawNumber(self.x + dist , self.y + dist)
        self.sirkel_pos[6] = self.__drawNumber(self.x, self.y)
        if number is 1:
            self.sirkel[0] = self.sirkel_pos[6]
        elif number is 2:
            self.sirkel[0] = self.sirkel_pos[1]
            self.sirkel[1] = self.sirkel_pos[4]
        elif number is 3:
            self.sirkel[0] = self.sirkel_pos[0]
            self.sirkel[1] = self.sirkel_pos[6]
            self.sirkel[2] = self.sirkel_pos[5]
        elif number is 4:
            self.sirkel[0] = self.sirkel_pos[0]
            self.sirkel[1] = self.sirkel_pos[2]
            self.sirkel[2] = self.sirkel_pos[3]
            self.sirkel[3] = self.sirkel_pos[5]
        elif number is 5:
            self.sirkel[0] = self.sirkel_pos[0]
            self.sirkel[1] = self.sirkel_pos[2]
            self.sirkel[2] = self.sirkel_pos[3]
            self.sirkel[3] = self.sirkel_pos[5]
            self.sirkel[4] = self.sirkel_pos[6]
        elif number is 6:
            self.sirkel[0] = self.sirkel_pos[0]
            self.sirkel[1] = self.sirkel_pos[1]
            self.sirkel[2] = self.sirkel_pos[2]
            self.sirkel[3] = self.sirkel_pos[3]
            self.sirkel[4] = self.sirkel_pos[4]
            self.sirkel[5] = self.sirkel_pos[5]
        for i in range(6):
            if self.sirkel[i] is not "OFF":
                self.sirkel[i].setFill("Black")
            else:
                break

    def diceUndraw(self):
        for i in range(6):
            if self.sirkel[i] is not "OFF":
                self.sirkel[i].undraw()
            else:
                break

    def diceSelect(self , x_click , y_click):
        state1 = self.x - self.size <= x_click <= self.x + self.size
        state2 = self.y - self.size <= y_click <= self.y + self.size
        if state1 == state2 == True:
            if self.select == False:
                self.__selectDraw()
                return self.select
            else:
                self.__selectUnDraw()
                return self.select
        else:
            return self.select

    def diceDeSelect(self):
        self.select = False
        if self.linje != [0 , 0 , 0 , 0]:
            for i in self.linje:
                i.undraw()

    def __selectDraw(self):
        self.select = True
        ssize = self.size
        self.linje[0] = Line(Point(self.x - ssize , self.y + ssize) , \
                      Point(self.x + ssize , self.y + ssize))
        self.linje[1] = Line(Point(self.x - ssize , self.y + ssize) ,
                      Point(self.x - ssize , self.y - ssize))
        self.linje[2] = Line(Point(self.x - ssize , self.y - ssize) ,
                      Point(self.x + ssize , self.y - ssize))
        self.linje[3] = Line(Point(self.x + ssize , self.y + ssize) ,
                      Point(self.x + ssize , self.y - ssize))
        for i in self.linje:
            i.setWidth(3)
            i.setFill("Red")
            i.setOutline("Red")
            i.draw(self.window)

    def __selectUnDraw(self):
        self.select = False
        for i in self.linje:
            i.undraw()

    def diceGetNumber(self):
        return self.number

class Money:

    def __init__(self , amount , x , y , window):
        self.window = window
        self.string = Text(Point(x , y) , str(amount)+"$")
        self.string.setSize(30)
        self.string.draw(window)
        
    def monUpdate(self , delta):
        val = self.string.getText()
        val = int(val[: len(val) - 1])
        self.string.setText(str(val + delta) + "$")

    def monPrize(self):
        val = self.string.getText()
        val = int(val[: len(val) - 1])
        self.string.setText(str(val - 10) + "$")

    def monGet(self):
        val = self.string.getText()
        val = int(val[: len(val) - 1])
        return val

class Combination:

    def __init__(self , liste):
        self.resultat = []
        for i in range(1 , 7):
            self.resultat.append(count(liste , i))

    def CombCheck(self):
        for i in self.resultat:
            if i >= 5:
                return 30
        teller = 0
        if self.resultat[0] > 0 and self.resultat[1] > 0 and \
           self.resultat[2] > 0 and self.resultat[3] > 0 and \
           self.resultat[4] > 0:
                return 20
        if self.resultat[1] > 0 and self.resultat[2] > 0 and \
           self.resultat[3] > 0 and self.resultat[4] > 0 and \
           self.resultat[5] > 0:
                return 20
        for i in self.resultat:
            if i >= 4:
                return 15
        teller = 0
        for i in self.resultat:
            if i == 3:
                for j in self.resultat:
                    if i != j:
                        if j >= 2:
                            return 12
            teller = teller + 1
        for i in self.resultat:
            if i==3:
                return 8
        teller = 0
        for i in self.resultat:
            if i == 2:
                for j in self.resultat:
                    if i != j:
                        if j == 2:
                            return 5
            teller = teller + 1
        return 0

def Buttoncheck(terning , window , trillknapp , quitknapp , doneknapp , \
                terningcheck):
    p = window.getMouse()
    x = p.getX()
    y = p.getY()
    for i in range(5):
        terningcheck[i] = terning[i].diceSelect(x , y)
    trillcheck = trillknapp.buttonClick(x , y)
    quitcheck = quitknapp.buttonClick(x , y)
    donecheck = doneknapp.buttonClick(x , y)
    return terningcheck , trillcheck , quitcheck , donecheck
            
def Paycheck(terning , penger):
    tall = []
    for i in terning:
        tall.append(i.diceGetNumber())
    check = Combination(tall)
    delta = check.CombCheck()
    penger.monUpdate(delta)

def triller(window , terning , terningcheck , antall):
    if antall < 2:
        for i in range(len(terning)):
            if terningcheck[i] == False:
                terning[i].diceNumber(randint(1 , 6))
    antall = antall + 1
    return terning , antall

def test():
    terning = []
    terningcheck = [False]*5
    avslutt = False
    window = GraphWin("Thomas" , 500 , 500)
    window.setBackground("Blue")
    window.setCoords(0 , 0 , 60 , 60)
    for i in range(5):
        terning.append(Dice(i*12 + 6 , 25 , 5 , window))
        terning[i].diceNumber(randint(1 , 6))
    penger = Money(100 , 30 , 40 , window)
    trillknapp = Button(30 , 15 , 10)
    trillknapp.buttonText("Roll")
    trillknapp.buttonDraw(window)
    quitknapp = Button(30 , 5 , 5)
    quitknapp.buttonText("Quit")
    quitknapp.buttonDraw(window)
    doneknapp = Button(30 , 10 , 10)
    doneknapp.buttonText("Done")
    doneknapp.buttonDraw(window)
    antall = 0
    penger.monPrize()
    while avslutt == False:
        terningcheck , trillcheck , quitcheck , donecheck = \
                     Buttoncheck(terning , window , trillknapp , \
                                 quitknapp , doneknapp , terningcheck)
        if trillcheck == True:
            terning , antall = triller(window , terning , terningcheck \
                                       , antall)
            if antall > 2 : donecheck = True
        if donecheck == True:
            penger.monPrize()
            terningcheck = [False]*5
            Paycheck(terning , penger)
            for i in terning:
                i.diceDeSelect()
            for i in range(5):
                terning[i].diceNumber(randint(1 , 6))
            antall = 0
        if penger.monGet() <= 10: quitcheck = True
        if quitcheck == True:
            avslutt = True
    window.close()
test()
