import string

TM5 = 7
TM15 = 5
Ordered_Keys5 = ["TM5", "GD5", "CM5", "OMF5", "VM5", "UM5"]
Ordered_Keys15 = ["TM15", "GD15", "CM15", "OMF15", "VM15", "UM15"]
Replace = ["TM;", "GD;", ";CM", ";OMF", ";VM", ";UM", ",", "\n"]
Replace_W = ["", "", "", "", "", "", ".", ""]
In_file = "measurement_2d.mes"
filename = "Latex_Maple.txt"

def fix_float(In_string, number):
    In_string = string.split(In_string, ".")
    In_string[0] = In_string[0] + "."
    In_string[1] = In_string[1][:number]
    In_string = string.join(In_string)
    In_string = string.replace(In_string, " ", "")
    return In_string

def order(data):
    newdata = {}
    for element in Ordered_Keys5:
        newdata[element] = []
    for element in Ordered_Keys15:
        newdata[element] = []
    count = 0
    for line in data:
        for i in range(len(Replace)):
            line = string.replace(line, Replace[i], Replace_W[i])
        line = string.split(line, ";")
        for ele in range(len(line)):
            if count < TM5:
                newdata[Ordered_Keys5[ele]].append(line[ele])
            else:
                newdata[Ordered_Keys15[ele]].append(line[ele])
        count += 1
    return newdata

def perc(data):
    deviation = {}
    for element in range(len(Ordered_Keys5) - 2):
        deviation[Ordered_Keys5[element + 2]] = []
    for element in range(len(Ordered_Keys15) - 2):
        deviation[Ordered_Keys15[element + 2]] = []
    for i in range(len(data[Ordered_Keys5[0]])):
        for j in range(len(Ordered_Keys5)-2):
            TB = eval(data[Ordered_Keys5[0]][i])
            Cur_M = eval(data[Ordered_Keys5[j + 2]][i])
            rate = abs((TB - Cur_M)/TB)
            rate = str(fix_float(str(100*rate), 1))
            GD = str(fix_float(str(data[Ordered_Keys5[1]][i]), 3))
            deviation[Ordered_Keys5[j + 2]].append([GD, rate])
    for i in range(len(data[Ordered_Keys15[0]])):
        for j in range(len(Ordered_Keys15)-2):
            TB = eval(data[Ordered_Keys15[0]][i])
            Cur_M = eval(data[Ordered_Keys15[j + 2]][i])
            rate = abs((TB - Cur_M)/TB)
            rate = str(fix_float(str(100*rate), 1))
            GD = str(fix_float(str(data[Ordered_Keys15[1]][i]), 3))
            deviation[Ordered_Keys15[j + 2]].append([GD, rate])
    return deviation

def calc_perc(filen):
    fil = open(filen, "r")
    data = fil.readlines()
    ordered = order(data)
    deviation = perc(ordered)
    return deviation, ordered
    
def int_string():
    newstring = "Latex:\n\n\\begin{table}[H]\n\\begin{center} \n "
    newstring += "\\begin{tabular}{|l|l|l|l|l|l|} \n    \\hline \n"
    newstring += "    \\multicolumn{6}{|l|}{Flow rate ~ 5 $m^3/h$} \\\\ \\hline\n"
    newstring += "    Turbine & Gamma & Coriolis & Orifice (Fluid) & Vortex & Ultrasound" 
    newstring += "\\\\ \\hline \n"
    return newstring

def manip_table(data):
    ending = "\\\\ \\hline\n"
    newstring = ""
    for i in range(TM5):
        newstring += "    "
        for element in Ordered_Keys5:
            newstring += data[element][i] + " & "
        newstring = newstring[:-2] + ending
    newstring += "    \\multicolumn{6}{|l|}{Flow rate ~ 15 $m^3/h$} \\\\ \\hline \n"
    for i in range(TM15):
        newstring += "    "
        for element in Ordered_Keys15:
            newstring += data[element][i] + " & "
        newstring = newstring[:-2] + ending
    print newstring
    return newstring

def end_string():
    return "    \\end{tabular} \n\\end{center}\n\\end{table}"

def Latex(fil, data):
    filestring = int_string()
    filestring += manip_table(data)
    filestring += end_string()
    fil.write(filestring)

def Maple(fil, data):
    filestring = "\n\nMaple:\n\n"
    for element in data:
        filestring += element + ":=" + str(data[element]) + "\n"
    fil.write(filestring)

def main():
    fil = open(filename, "w")
    deviation, ordered = calc_perc(In_file)
    Latex(fil, ordered)
    Maple(fil, deviation)

if __name__=="__main__":
    main()
