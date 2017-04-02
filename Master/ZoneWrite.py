from Writer2 import *
from Plotter import *
import sys, traceback, pygame, time

extension = "asc"
def write():
    pattern = Pattern()
    pattern.data["Top Left"] = [1200, 1200]
    pattern.circle["Position"] = [600, 600]
    pattern.circle["Radius"] = 260
    pattern.data["Mark Offset"] = 30
    pattern.circle["Iterations"] = 1000000
    pattern.data["Circle Dose"] = 160.0
#    pattern.data["Output"] = filename
    pattern.data["Ext"] = extension
    pattern.GenFile()    
    pattern.Output()    
    pattern.Output_Circle()
    return pattern.data["Output"] + "." + extension

def Support():
    pattern = Pattern()
    pattern.marks["Top Left"] = [1670, 1670]
    pattern.marks["Bottom Right"] = [30, 30]
    pattern.parameters["Position"] = [850, 850]
    pattern.parameters["Radius"] = 96
    pattern.marks["Offset"] = 30
    pattern.marks["Dose"] = 100.0
    pattern.marks["Layer"] = 1
    pattern.marks["Width"] = [3.0, 0.2]
    pattern.marks["Length"] = [0.80, 0.20]
    pattern.parameters["Layer"] = 2
    pattern.parameters["Dose"] = 100.0
    pattern.parameters["Width"] = 0.450
    pattern.parameters["g"] = 1.500
    pattern.parameters["b"] = 0.700
    pattern.parameters["lambda"] = 50 * 10**(-12)
    pattern.output["Extension"] = extension
    pattern.GenFile("Magie_Zones")
    pattern.Gen_Zones()
    return pattern.output["Filename"] + "." + extension



def plot(filename):
    Plotter = Plot()
    Plotter.Read_Fixed(filename, False)
    Plotter.Plot()
    win = Plotter.data["win"]
    win.Update()
    Plotter.Draw()
    while True:
        win.Event()
        event = win.Get("event")
        win.Update()
        if event == "quit" or event == "q":
            win.Quit()


def main():
    #filename =  write()
    filename = Support()
    plot(filename)


if __name__ == "__main__":
    try:
        main()
    except Exception, e:
        tb = sys.exc_info()[2]
        traceback.print_exception(e.__class__, e, tb)
    pygame.quit()   

