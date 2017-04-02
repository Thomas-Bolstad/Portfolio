#Test v. 3
from GUIwrapper import *
import DK2, time, string, traceback

#Global Variables:
width, height = 1280, 800
borders = [width - 20, height - 20]
Interval = 0.02
Transp = (255, 255, 255)
BackGr = (255, 255, 255)
Name = "Thomas"
Files = {"enemy" : "enemy.png", "player" : "hero.png"}
EStartCoord = [250, 250]
PStartCoord = [100, 100]
Max_vel = (12, 12)
PFriction = [0.1, 0.1]
Acc = [0.2, 0.2]
Transparant = (255, 255, 255)
en_dimen = [20, 20]

#Data for the image files
    
CoordsR = {0 : (0, 0, 20, 20) , 1 : (20, 0, 20, 20),
          2 : (40, 0, 20, 20) , 3 : (60, 0, 20, 20),
          4 : (80, 0, 20, 20)}

CoordsL = {0 : (0, 20, 20, 20) , 1 : (20, 20, 20, 20),
          2 : (40, 20, 20, 20) , 3 : (60, 20, 20, 20),
          4 : (80, 20, 20, 20)}

class Avatar:

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
    
    def __init__(self, coords, widhei, Gobject):
        kinematic = DK2.Point(position = [i for i in coords],
                              borders = (0, 0, borders[0], borders[1]),
                              acceleration = [i for i in Acc])
        kinematic.RandInit(Max_vel)
        self.data = {"Coords" : [i for i in coords], "nose" : "R", "frame" : 0,
                     "Rframe" : -1, "kinematic" : kinematic,
                     "graphic" : Gobject, "width" : widhei[0], "height" : widhei[1]}

    def Move(self):
        self.data["kinematic"].RandMove()
        vel = [i for i in self.data["kinematic"].Get("velocity")]
        if vel[0] > 0:
            self.data["nose"] = "R"
        else:
            self.data["nose"] = "L"
        self.data["Coords"] = [i for i in self.data["kinematic"].Get("position")]
        self.data["Rframe"] += 1
        if self.data["Rframe"] % 5 == 1:
            self.data["frame"] += 1
        fr, no = self.data["frame"], self.data["nose"]
        co = [i for i in self.data["kinematic"].Get("position")]
        self.data["graphic"].DrawFrame(fr, no, co)

    def En_Hit(self, hitcheck, pos, vel):
        w = self.data["width"]
        h = self.data["height"]
        hit = hitcheck.Check(self.data["Coords"], w, h, [i for i in vel])
        if hit:
            self.data["new hit"] = time.time()
            newpos = [- pos[i] + self.data["Coords"][i] for i in range(len(pos))]
            for i in range(len(newpos)):
                factor = 5*(vel[0]**2+vel[1]**2)**0.5
                if newpos[i] < 0:
                    factor = -5*(vel[0]**2+vel[1]**2)**0.5
                self.data["kinematic"].data["position"][i] \
                = self.data["Coords"][i] + factor

class Player:
    check = {'f1': 282, 'f2': 283, 'f3': 284, 'f4': 285, 'f5': 286,
                  'f6': 287, 'f7': 288, 'f8': 289, 'f9': 290, 'l': 108,
                  'down': 274, 'd': 100, 'right': 275, 'tab': 9,
                  'escape': 27, 'home': 278, 'u': 117, 'pause': 19,
                  'end': 279, 'space': 32, 'z': 122, '-': 45,
                  ',': 44, '.': 46, '1': 49, '0': 48, '3': 51,
                  '2': 50, 'backspace': 8, '4': 52, '7': 55,
                  'right shift': 303, '9': 57, '5': 53, '=': 61,
                  'left shift': 304, 'return': 13, '`': 96, 's': 115,
                  '6': 54, 'page up': 280, 'c': 99, 'y': 121, '8': 56,
                  '[': 91, ']': 93, 'left ctrl': 306, 'a': 97,
                  'insert': 277, 'page down': 281, 'b': 98, 'e': 101,
                  'left': 276, 'g': 103, 'f': 102, 'i': 105, 'h': 104,
                  'k': 107, 'j': 106, 'm': 109, 'up': 273, 'o': 111,
                  'n': 110, 'q': 113, 'p': 112, 'left alt': 308, 'r': 114,
                  'right ctrl': 305, 't': 116, 'w': 119, 'v': 118,
                  'f12': 293, 'x': 120, 'f10': 291, 'f11': 292, 'delete': 127}

    def __init__(self, coords, Gobject):
        kinematic = DK2.Point(position = [i for i in coords],
                              borders = (0, 0, borders[0], borders[1]),
                              acceleration = [i for i in Acc], friction = PFriction)
        
        self.data = {"Coords" : [i for i in coords], "nose" : "R", "lastnose" : "R",
                     "frame" : 0, "Rframe" : -1, "kinematic" : kinematic,
                     "direction" : [0, 0], "event" : [0, 0],
                     "graphic" : Gobject}

        self.directs = {"up" : (0, -1), "down" : (0, 1),
                        "left" : (-1, 0), "right" : (1, 0)}

        self.pressed = {"up" : False, "down" : False,
                        "right" : False, "left" : False}

    def _UpdateKinGraph(self):
        self.data["kinematic"].WallFix()
        self.data["kinematic"].Move()
        self.data["Coords"] = [i for i in self.data["kinematic"].Get("position")]
        self.data["Rframe"] += 1
        if self.data["Rframe"] % 5 == 1:
            self.data["frame"] += 1
        fr, no= self.data["frame"], self.data["nose"]
        co = [i for i in self.data["Coords"]]
        self.data["graphic"].DrawFrame(fr, no, co)

    def _FixNose(self):
        vel = [i for i in self.data["kinematic"].Get("velocity")]
        if vel[0] > 0:
            self.data["nose"] = "R"
            self.data["lastnose"] = "R"
        elif vel[0] <0:
            self.data["nose"] = "L"
            self.data["lastnose"] = "L"
        else:
            if self.data["lastnose"] == "R":
                self.data["nose"] = "R"
            else:
                self.data["nose"] = "L"

    def _FixAcc(self):
        newacc = [i for i in self.data["direction"]]
        vel = [i for i in self.data["kinematic"].Get("velocity")]
        newacc = [newacc[i] * Acc[i] for i in range(len(newacc))]
        for i in range(len(vel)):
            if abs(vel[i]) > Max_vel[i]:
                newacc[i] =0
        self.data["kinematic"].Modify("acceleration", newacc)

    def _EventToDirection(self, values):
        self.data['direction'][1] = values[self.check['down']] \
                                    - values[self.check['up']]
        self.data['direction'][0] = values[self.check['right']] \
                                    - values[self.check['left']]


    def Move(self, values):
        self._EventToDirection(values)
        self._FixAcc()
        self._FixNose()
        self._UpdateKinGraph()

class HitCheck:

    def __init__(self, player):
        self.data = {"player" : player, "height" : 20, "width" : 20,
                     "position" : player.data["kinematic"].data["position"],
                     }

    def Check(self, position, width, length, dim = (10, 10)):
        pos = self.data["position"]
        width = self.data["width"] + dim[0]
        height = self.data["height"] + dim[1]
        if abs(position[0] - pos[0]) < width:
            if abs(position[1] - pos[1]) < height:
                return True
        return False
    
def main():
    win = Window(Name, width, height)
    win.Modify("background", BackGr)
    screen = win.Get("screen")
    EnGraph = Avatar(screen, Files["enemy"], Transp)
    enemies = []
    for i in range(1000):
        coord = [j for j in EStartCoord]
        new = Enemy(coord, en_dimen, EnGraph)
        enemies.append(new)
    last_frame = 0
    PGraph = Avatar(screen, Files["player"], Transp)
    player = Player(PStartCoord, PGraph)
    check = HitCheck(player)
    while True:
        new_time = time.time()
        if new_time - last_frame > Interval:
            last_frame = new_time
            win.Blit()
            for i in enemies:
                i.Move()
                i.En_Hit(check, player.data["Coords"], \
                         player.data["kinematic"].Get("velocity"))
            win.Event()
            event = win.Get("event")
            values = win.Get("eventlist")
            player.Move(values)
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
#Enemy_init tar ekstra argument med hoyde og bredde i en liste widhei
