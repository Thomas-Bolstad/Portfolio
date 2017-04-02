from string import *
from random import *

filename = "leveldesign.level"

class Board:

    def __init__(self, filename):
        self.type_p, self.end, self.zone = [], [], []
        levelread = open(filename, "r")
        level = levelread.readlines()
        seperator = ";"
        for i in level:
            data = split(i, seperator)
            self.zone.append(data[0])
            self.type_p.append(data[1])
            self.end.append(data[2])
        for i in range(len(self.type_p)):
            if self.type_p[i] == "3":
                self.final = i

    def GetInfo(self, zone):
        return self.type_p[zone], self.end[zone]

    def GetLenght(self):
        return self.final


class Player:

    def __init__(self):
        self.position = 0
        self.turns = 0
        self.lad_up = 0
        self.lad_down = 0
        self.total_dice = 0
        #self.ladder = 0

    def Move(self, newpos, dice):
        self.position = int(newpos)
        self.turns += 1
        self.total_dice += dice
        self.cur_dice = dice
        self.ladder = 0

    def LadderUp(self):
        self.lad_up += 1
        self.ladder = 1

    def LadderDown(self):
        self.lad_down += 1
        self.ladder = 2

    def GetPos(self):
        return self.position

    def GetInfo(self):
        average_dice = float(self.total_dice)/self.turns
        return self.turns, self.lad_up, self.lad_down, average_dice

    def Update(self, player, board, steps):
        near_up = 0
        near_down = 0
        final = board.GetLenght()
        for i in range(self.position, final):
            type_p, end = board.GetInfo(i)
            if near_up == 0 and type_p == "1":
                near_up = i
            if near_down == 0 and type_p == "2":
                near_down = i

        print "Player " + str(player + 1) + ":"
        print "you rolled a " + str(steps) + ", you are now on zone " \
              + str(self.position)
        
        if near_up != 0:
            print "and the nearest upwards ladder is at zone " + str(near_up)
        if near_down != 0:
            print "and the nearest downward ladder is at zone " + str(near_down)
        if self.ladder == 1:
            print "You went up a ladder!"
        elif self.ladder == 2:
            print "you went down a ladder!"
        print


def Initial():
    print "Introduksjonstekst"
    players = 0
    while players not in [1,2,3,4]:
        num = raw_input("How many players do you want (1-4)? ")
        try:
            players = int(num)
        except:
            pass
            
    return players

def Dice():
    return randint(1,6)

def playerMove(number, player, board):
    goal = False
    roll = Dice()
    position = player.GetPos()
    newpos = position + roll
    final = board.GetLenght()
    if newpos < final:
        zone_type, end = board.GetInfo(newpos)
        if zone_type == "0":
            player.Move(newpos, roll)
        elif zone_type == "1":
            newpos = end
            player.Move(newpos, roll)
            player.LadderUp()
        elif zone_type == "2":
            newpos = end
            player.Move(newpos, roll)
            player.LadderDown()
    else:
        player.Move(final, roll)
        goal = True
    return goal, roll
    
def inputCheck():
    valid = False
    while not valid:
        choice = raw_input("R for roll, L for ladders, P for positions," \
                           + " Q for quit: ")
        if choice == "R" or "Q" or "L" or "P":
            valid = True
    print
    return choice

def EndResults(players, places):
    str_place = ["first", "second", "third", "fourth"]
    for i in range(len(places)):
        turns, lad_up, lad_down, avg_dice = players[places[i]].GetInfo()
        print
        print "Player " + str(places[i] + 1) + " ended on " + str_place[i] + \
              " place. And went up " + str(lad_up) + " ladders, and down " \
              + str(lad_down) + " ladders.\n And used " + str(turns) + \
              " turns, and threw in average %0.2f" % avg_dice + \
              " with the dice."

def Listzones(board):
    length = board.GetLenght()
    print
    for i in range(length):
        type_p, end = board.GetInfo(i)
        if type_p == "1":
            print "Upward ladder at zone " + str(i) + " which ends at " \
                  + "zone " + str(end),
        if type_p == "2":
            print "Downward ladder at zone " + str(i) + " which ends at " \
                  + "zone " + str(end),
    print

def Positions(players):
    pos = []
    for i in range(len(players)):
        pos.append(players[i].GetPos())
    for i in range(len(pos)):
        print "Player " + str(i + 1) + " is in zone " + str(pos[i])
    print
            

def main():
    newplayers = []
    active = []
    players = Initial()
    for i in range(players):
        newplayers.append(Player())
        active.append(i)
    place = []
    playing = True
    newboard = Board(filename)
    while playing:
        i = 0
        while i < len(active):
            cur = active[i] 
            choice = inputCheck()
            if choice == "R":
                goal, roll = playerMove(cur, newplayers[cur], newboard)
                newplayers[cur].Update(cur, newboard, roll)
                if goal == True:
                    place.append(cur)
                    active.remove(cur)
                    print "Player " + str(cur + 1) + " reached the goal!"
                else:
                    i += 1
            elif choice == "L":
                Listzones(newboard)
            elif choice == "P":
                Positions(newplayers)
            elif choice == "Q":
                playing = False
                break
        if len(active) == 0:
            playing = False
    EndResults(newplayers, place)
main()
                
