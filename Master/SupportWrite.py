from Writer2 import *
from Plotter import *
import sys, traceback, pygame, time

extension = "asc"

def Support():
    pattern = Pattern()
    pattern.marks["Top Left"] = [570, 570]
    pattern.marks["Bottom Right"] = [30, 30]
    pattern.parameters["Position"] = [300, 300]
    pattern.parameters["Radius"] = 200
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
    pattern.parameters["Sub Lines"] = 10
    pattern.parameters["lambda"] = 50 * 10**(-12)
    pattern.output["Extension"] = extension
    pattern.GenFile("Magie_Support")
    pattern.Marks()
    pattern.Gen_Support_Pattern()
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
