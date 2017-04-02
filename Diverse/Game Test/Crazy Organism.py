#Test v. 2
from GUIwrapper import *
import random, DK2, time, string, traceback

#Global Variables:
width, height = 500, 500
border = [width - 20, height - 20]
Interval = 0.05
Transp = (255, 255, 255)
BackGr = (255, 255, 255)
name = "Thomas"
files = {"enemy" : "enemy.png", "player" : "hero.png"}
EStartCoord = [250, 250]
PStartCoord = [100, 100]
Max_vel = (5, 5)
Friction = [0.5, 0.5]
Acc = [1, 1]

#Data for the image files
    
CoordsR = {0 : (0, 0, 20, 20) , 1 : (20, 0, 20, 20),
          2 : (40, 0, 20, 20) , 3 : (60, 0, 20, 20),
          4 : (80, 0, 20, 20)}

CoordsL = {0 : (0, 20, 20, 20) , 1 : (20, 20, 20, 20),
          2 : (40, 20, 20, 20) , 3 : (60, 20, 20, 20),
          4 : (80, 20, 20, 20)}
Transparant = (255, 255, 255)

class GraphObject:

    def __init__(self, screen, filename, Transp):
        avatarL, avatarR = [], []
        for element in range(len(CoordsR)):
            avatar = Object(filename)
            avatar.Transparent(Transp)
            avatar.Modify("chop", CoordsR[element])
            avatarR.append(avatar)
            avatar = Object(filename)
            avatar.Transparent(Transp)
            avatar.Modify("chop", CoordsL[element])
            avatarL.append(avatar)
        self.avatarL, self.avatarR = tuple(avatarL), tuple(avatarR)
        self.data = {"screen" : screen}

    def DrawFrame(self, frame, direction, coords):
        if direction == "R":
            self.avatarR[frame % 5].Modify("coords", coords)
            self.avatarR[frame % 5].Blit(self.data["screen"])

        elif direction == "L":
            self.avatarL[frame % 5].Modify("coords", coords)
            self.avatarL[frame % 5].Blit(self.data["screen"])        

class Enemy:

    def __init__(self, coords, Gobject):
        kinematic = DK2.Point(position = coords,
                              borders = (0, 0, border[0], border[1]),
                              acceleration = Acc)
        kinematic.RandInit(Max_vel)
        self.data = {"coords" : coords, "nose" : "R", "frame" : 0,
                     "Rframe" : -1, "kinematic" : kinematic,
                     "graphic" : Gobject}

    def Move(self):
        self.data["kinematic"].RandMove()
        x, y = self.data["kinematic"].Get("position")
        vel = self.data["kinematic"].Get("velocity")
        if vel[0] > 0:
            self.data["nose"] = "R"
        else:
            self.data["nose"] = "L"
        self.data["coords"] = (x, y)
        self.data["Rframe"] += 1
        if self.data["Rframe"] % 5 == 1:
            self.data["frame"] += 1
        fr, no, co = self.data["frame"], self.data["nose"], self.data["coords"]
        self.data["graphic"].DrawFrame(fr, no, co)



def main():
    win = Window(name, width, height)
    win.Modify("background", BackGr)
    screen = win.Get("screen")
    EnGraph = GraphObject(screen, files["enemy"], Transp)
    enemies = []
    for i in range(1000):
        #coord = [EStartCoord[0], EStartCoord[1]]
        coord = EStartCoord
        new = Enemy(coord, EnGraph)
        enemies.append(new)
    last_frame = 0
    while True:
        new_time = time.time()
        if new_time - last_frame > Interval:
            last_frame = new_time
            win.Blit()
            for i in enemies:
                i.Move()
            win.Event()
            event = win.Get("event")
            #player.Move(event)
            if event == "quit" or event == "q":
                win.Quit()
            win.Update()
            

if __name__ == "__main__":
    try:
        main()
    except Exception, e:
        tb = sys.exc_info()[2]
        traceback.print_exception(e.__class__, e, tb)
    pygame.quit()    
