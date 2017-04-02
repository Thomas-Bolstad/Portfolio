# Regnedata
import string
import math

fil1 = open("measurement2b.txt", "r")
fil2 = open("calculations2b.txt", "w")
fil2 = open("turndown2b.txt", "w")
replace = ["\n", " ", ":", "mb", "St", "OM", "VM", "TM", "CM", "UM", ";", ","]
replace_w = ["", "", "", "", "", "", "", "", "", "", ";", "."]
data = fil1.readlines()
manip_data = [[], [], [], [], [], []]
sifre = 2
d = 0.0305
C = 0.6125
D = 0.0508
A_2 = math.pi*(d/2.0)**2
rho = 1000

def fix_float(In_string, number):
    In_string = string.split(In_string, ".")
    In_string[0] = In_string[0] + "."
    In_string[1] = In_string[1][:number]
    In_string = string.join(In_string)
    In_string = string.replace(In_string, " ", "")
    return In_string

q_orifice = []

for line in data:
    for element in range(len(replace)):
        line = string.replace(line, replace[element], replace_w[element])
    line = string.split(line, ";")
    for i in range(len(line)):
        manip_data[i].append(eval(line[i]))

orifice_opening = [[],[],[],[]]
for i in range(len(manip_data[0])):
    for j in range(len(orifice_opening)):
        calc = 1/(5.9983*10**(5)*manip_data[1][i]/
                     (manip_data[j+2][i]**2)+1.5016*10**5)
        if calc < 0:
            element = "NEGATIV"
        else:
            element = 1/(calc)**(1/4.0)
            element = str(element)
            element = string.split(element, ".")
            element[0] = element[0] + "."
            element[1] = element[1][:sifre]
            element = string.join(element)
            element = string.replace(element, " ", "")
        orifice_opening[j].append(element)

    q_or = 3600*(C*A_2/(1-(d/D)**4)**0.5)*(2*manip_data[1][i]*100/rho)**0.5
    q_orifice.append(q_or)

newstring = "\\begin{table}[H]\n\\begin{center} \n "
newstring += "\\begin{tabular}{|l|l|l|} \n    \\hline \n"
newstring += "    Orifice Meter [m\^3/h] & Turbine Meter [m\^3/h] & deviation[\%]"
newstring += "\\\\ \\hline\n"
q_TM = manip_data[3]
for element in range(len(q_TM)):
    TM = fix_float(str(q_TM[element]), 4)
    Orifice = fix_float(str(q_orifice[element]), 4)
    Deviation = str(100*abs(eval(TM)-eval(Orifice))/eval(TM))
    Deviation = fix_float(str(Deviation), 2)
    newstring += "$" + Orifice + "$ & " + "$" + TM + "$ & " + "$" + Deviation
    newstring += "$ \\\\ \\hline \n"
newstring += "    \end{tabular}\n\end{center}\n\end{table}"


#Uncertainty:

Denom = "1/((1.599*10**(9)*C**(2)*Del_P/(rho*q**(2)))+(1/D**(4)))**(3.0/4.0)\
*(1.599*10**(9)*C**(2)*Del_P/(rho*q**(2))+(1/D**(4)))**(2)"


dD = "1000.0/(" + Denom + "*D**(5))"

dC = "7.99*10**11*C*Del_P/(" + Denom + "*rho*q**2)"

dDel_P = "4.0*10**11*C**(2)/(" + Denom + "*rho*q**2)"

dq = "7.99*10**11*C**(2)*Del_P/(" + Denom + "*rho*q**3)"

drho = "4.0*10**11*C**(2)*Del_P/(" + Denom + "*rho**(2)*q**(2))"

Un_D, Un_C, Un_Del_P, Un_q, Un_rho = [], [], [], [], []

sigma_D = 0.00005

sigma_C = 0.00005

sigma_Del_P = 5.0

sigma_q = [0.05/3600]*4

sigma_rho = 5.0

for i in range(20):
    q_l = [manip_data[j + 2][i] for j in range(4)]
    Del_P = manip_data[1][i]
    new = [eval(dC) for q in q_l]
    Un_C.append(new)
    new = [eval(dD) for q in q_l]
    Un_D.append(new)
    new = [eval(dDel_P) for q in q_l]
    Un_Del_P.append(new)
    new = [eval(dq) for q in q_l]
    Un_q.append(new)
    new = [eval(drho) for q in q_l]
    Un_rho.append(new)

formula = "((Un_D[i][j]*sigma_D)**(2) + (Un_C[i][j]*sigma_C)**(2) + \
(Un_Del_P[i][j]*sigma_Del_P)**2 + \
(Un_q[i][j]*sigma_q[j])**(2) + (Un_rho[i][j]*sigma_rho)**(2))**0.5"

Fin_Un = []
for i in range(20):
    new = [fix_float(str(eval(formula)), 2) for j in range(4)]
    Fin_Un.append(new)

newstring = "\\begin{center} \n    \\begin{tabular}{|l|l|l|l|l|} \n    \\hline \n"
newstring += "    measurement \# & Vortex & Turbine & Coriolis & Ultrasound"
newstring += "\\\\ \\hline \n"
for i in range(len(orifice_opening[0])):
    newstring += "$" + str(i+1) + "$ &" + \
                 " $" + orifice_opening[0][i] + "$ &" + \
                  "$" + orifice_opening[1][i] + "$ &" + \
                  "$" + orifice_opening[2][i] + "$ &" + \
                  "$" + orifice_opening[3][i] + "$" + \
                 "\\\\ \\hline \n"
    #print i
newstring += "    \end{tabular}\n\end{center}"
fil2.write(newstring)
print newstring
