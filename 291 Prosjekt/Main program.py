#Innlevering 291:

#Dette er et stigespill med et usynlig brett, med skriftlig input og feedback.
from string import *
from random import *

filename = "leveldesign.level"


def Initial():
    print "Introduksjonstekst"
    players = 0
    while players not in [1,2,3,4]:
        players = int(raw_input("How many players do you want (1-4)? "))
    return players

def LoadBoard(filename):
    type_p, end, zone = [], [], []
    level = open(filename, "r")
    level = level.readlines()
    seperator_1 = "\n"
    seperator_2 = ";"
    for i in level:
        data = split(i, seperator_2)
        zone.append(data[0])
        type_p.append(data[1])
        end.append(data[2])
    return type_p, end

class Dice:

    def RandRoll(self):
        return randint(1,6)

def MovePlayer(steps, current):
    newplace = current + steps
    return newplace
        
def Update(zone, type_p, end, steps, ladder, player):
    near_lad = 0
    near_fall = 0
    for i in range(zone, len(type_p)):
        if near_lad == 0:
            if type_p[i] == "1":
                near_lad = i
        if near_fall == 0:
            if type_p[i] == "2":
                near_fall = i
    print "Player " + str(player) + ":"
    print "you rolled a " + str(steps) + ", you are now on zone " + str(zone)
    if near_lad != 0:
        print "and the nearest upwards" + "ladder is at zone " + str(near_lad)
    if near_fall != 0:
        print "and the nearest downward" + "ladder is at zone " + str(near_fall)
    if ladder == 1:
        print "You went up a ladder!"
    elif ladder == 2:
        print "you went down a ladder!"
    print

def EndResults(places, turns):
    current = 1
    for i in places:
        print "player " + str(i + 1) + " ended in place " + str(current) + \
              " after " + str(turns[i]) + " turns"
        current += 1

def main():
    players = Initial()
    current = []
    places = []
    turns = [0,0,0,0]
    for i in range(players):
        current.append(0)
    running = True
    type_p, end = LoadBoard(filename)
    for i in range(len(type_p)):
        if type_p[i] == "3":
            last = i
    newdice = Dice()
    while running:
        for i in range(players):
            valid = False
            while not valid:
                ladder = 0
                choice = raw_input("R for roll, Q for quit: ")
                if choice == "R":
                    valid = True
                    steps = newdice.RandRoll()
                    turns[i] += 1
                    newzone = MovePlayer(steps, current[i])
                    if newzone < last:
                        if type_p[newzone] == "0":
                            pass
                        elif type_p[newzone]== "1":
                            ladder = 1
                            newzone = int(end[newzone])
                        elif type_p[newzone] == "2":
                            ladder = 2
                            newzone = int(end[newzone])
                    else:
                        places.append(i)
                        players += -1
                        newzone = last
                    Update(newzone, type_p, end, steps, ladder, i+1)
                    current[i] = newzone
                elif choice == "Q":
                    running = False
                    valid = True
        if players == 0:
            running = False
    EndResults(places, turns)

main()
                
                
                
