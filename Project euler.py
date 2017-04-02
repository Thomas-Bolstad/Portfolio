#Project euler:

#!/usr/bin/python
# -*- coding: ascii -*-


from string import *
from time import *
import sys, os

def Progress(perc):
    orig = "[----------]"
    orig2 = "[---------]"
    perc = perc + 1
    posB = (perc - perc % 10)/10
    posS = perc % 10
    newstring2 = orig2[0] + posS*"x" + orig2[posS + 1: 11]
    newstring = orig[0] + posB*"X" + orig[posB + 1: 12]
    newstring = "%07s %3s"  % (newstring, perc)
    newstring += " %"
    newstring += "  " + newstring2 + "\b"*32
    if perc < 100:
        sys.stdout.write(newstring)
        sys.stdout.flush()
    else:
        sys.stdout.write("\b"*32 + " "*32 + "\b"*32)
        sys.stdout.flush()

def Nummer1():
    Liste = []
    Initial = 0
    for i in range(0 , 1000):
        if (i+0.0)/3 == int(i)/3:
            Liste.append(i)
        elif (i+0.0)/5 == int(i)/5:
            Liste.append(i)
    for i in range(len(Liste)):
        Initial = Initial + Liste[i]
    print Initial

def Nummer2():
    Liste = []
    Initial = 0
    Fibbonacci1 = 1
    Fibbonacci2 = 2
    print Fibbonacci1
    Liste.append(Fibbonacci2)
    for i in range(0 , 1000):
        Fibbonacci2 = Fibbonacci1 + Fibbonacci2
        Fibbonacci1 = Fibbonacci2 - Fibbonacci1
        if Fibbonacci2 > 4000000:
            break
        if (Fibbonacci2 + 0.0)/2 == int(Fibbonacci2)/2:
            Liste.append(Fibbonacci2)
    for i in range(len(Liste)):
        Initial = Initial + Liste[i]
    print Initial


def Nummer3():
    Initial = 600851475143
    Av , i = 0 , 2
    while Av == 0:
        if i == Initial:
            break
        if (Initial + 0.0)/i == int(Initial)/i:
            Initial = int(Initial)/i
            i = i - 1
        i = i + 1
    print Initial

def Nummer4():
    Maks = 0
    Liste = []
    Initial = 1000
    for i in range(900):
        Teller = Initial - i - 1
        for j in range(900):
            Teller2 = Initial - j -1
            Baklengs = ""
            Verdi = Teller*Teller2
            Verdistring = str(Verdi)
            for i in range(len(Verdistring)):
                Baklengs = Verdistring[i] + str(Baklengs)
            if Baklengs == str(Verdi):
                Liste.append(Verdi)
    for i in range(len(Liste)):
        if Liste[i] > Maks:
            Maks = Liste[i]
    print Maks

#Feil:
def Nummer5v2():
    Verdi = []
    Pa = 1
    for i in range(1 , 21):
        Verdi.append(i)
    Verdi = Verdi[0]*Verdi[1]*Verdi[2]*Verdi[3]*Verdi[4]*Verdi[5]*Verdi[6] \
		    *Verdi[7]*Verdi[8]*Verdi[9]*Verdi[10]*Verdi[11]*Verdi[12] \
		    *Verdi[13]*Verdi[14]*Verdi[15]*Verdi[16]*Verdi[17] \
		    *Verdi[18]*Verdi[19]
    while Pa == 1:
        if (Verdi + 0.0)/2 != int(Verdi)/2:
            Pa = 0
        else:
            Verdi = Verdi/2
    print Verdi
    
#Nye:
def Nummer5v3():
    tid_a = time()
    current = 2520
    primes = range(10, 21)
    while True:
        current += 20
        for i in primes:
            check = current % i
            if check:
                break
        if not current % i:
            break
    tid_b = time()
    print current, i, tid_b - tid_a



def Nummer5():
    tall = 2*2*2*2*3*3*19*17*13*11*7*5
    
def Nummer6():
    Verdi1 = 0
    Verdi2 = 0
    for i in range(1 , 101):
        Verdi1 = Verdi1 + i**2
        Verdi2 = Verdi2 + i
    Total = Verdi2**2 - Verdi1
    print Total


def Nummer7():
    i = 0
    k = 3
    Teller = 0
    Prim = 0
    Liste = [2 , 3]
    while i < 1000:
        for j in Liste:
            if k == j:
                Teller = 0
                break
            if float(k)/j == k/j:
                Teller = 1
                break
        if Teller == 0:
            Liste.append(k)
            Prim = Prim + 1
            i = i + 1
            k = Liste[i + 1] + 2
        if Teller == 1:
            k = k + 2
        Teller = 0
    #Fjerner det siste tillagte leddet.
    k = k - 2
    print k
    print len(Liste)


def Nummer8():
    Liste = []
    Regn = [0]*5
    Maks = 0
    String = "73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"
    Lengde = len(String)
    print Lengde
    for i in range(Lengde - 4):
        Regn[0] = int(String[i])
        Regn[1] = int(String[i + 1])
        Regn[2] = int(String[i + 2])
        Regn[3] = int(String[i + 3])
        Regn[4] = int(String[i + 4])
        
        Liste.append(Regn[0]*Regn[1]*Regn[2]*Regn[3]*Regn[4])
    for i in range(len(Liste)):
        if Liste[i] > Maks:
            Maks = Liste[i]
    print Maks

def Nummer9():
    Liste1 = []
    Liste2 = []
    for i in range(1 , 500):
        Liste1.append(i**2)
        for j in range(1 , 500):
            Liste2.append(j**2)
            if Liste1[i - 1]**0.5 + Liste2[j - 1]**0.5 \
            + (Liste1[i - 1] + Liste2[j - 1])**0.5 == 1000:
                print int(Liste1[i - 1]**0.5*Liste2[j - 1]**0.5*(Liste1[i - 1] + Liste2[j - 1])**0.5)
            

def Nummer10(value):
    Primliste = [2,3]
    PrimTall = 3
    nytall = 3
    tid_a = time()
    while PrimTall < value:
        nytall += 2
        primCheck = True
        for objekt in Primliste:
            if nytall % objekt == 0:
                primCheck = False
                break
            if objekt > nytall**0.5:
                break
        if primCheck:
            Primliste.append(nytall)
            PrimTall = nytall
    tid_b = time()
    Primliste.pop(len(Primliste) - 1)
    summmm = 0
    for i in Primliste:
        summmm += i
    print "tid: ", tid_b - tid_a
    print PrimTall
    print summmm

                
def Nummer10v2(value):
    i = 0
    k = 3
    Teller = 0
    Prim = 0
    Liste = [2 , 3]
    Liste2 = [2]
    l = 0
    summer = 0
    a = time()
    while Prim < value:
        for j in Liste2:
            if k == j:
                Teller = 0
                break
            if float(k)/j == k/j:
                Teller = 1
                break
        if Teller == 0:
            Liste.append(k)
            Prim = Prim + 1
            #Sjekker om det navaerende ytterste listeelementet i Liste2
            #er mindre enn halvparten enn tallet den har talt til na.
            #I sa fall, legger den til et nytt element i listen. Pa denne
            #maten halveres nesten tiden som brukes pa a regne ut et primtall.
            if k**0.5 > Liste2[l]:
                l = l + 1
                Liste2.append(Liste[l])
            i = i + 1
            summer = summer + k
            k = k + 2
        if Teller == 1:
            k = k + 2
        Teller = 0
        if k > value:
            summer = summer
            break
    print summer
    #Fjerner det siste tillagte leddet.
    k = k - 2
    b = time()
    print b-a
    
def Nummer10v3(value):
    tid_a = time()
    primes = [2, 3]
    cur_number = 5
    primeX = 2
    lastperc = 0
    while primeX < value:
        for element in primes:
            check = cur_number % element            
            if cur_number**0.5 < element:
                break
            if not check:
                break
        if check:
            primes.append(cur_number)
            primeX += 1
        cur_number += 2
        newperc = int(primeX*100 / value)
        if newperc - lastperc:
            Progress(newperc)
            lastperc = newperc
    tid_b = time()
    print tid_b - tid_a
    print primes[-1]








def Nummer11():
    Max1 = 0
    Max2 = 0
    Liste1 = []
    Liste2 = [""]*20
    Liste3 = [""]*20
    Liste4 = [""]*20
    Liste5 = [""]*20
    Liste6 = [""]*20
    Maks = 0
    String = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 \
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 \
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 \
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 \
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 \
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 \
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 \
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 \
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 \
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 \
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 \
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 \
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 \
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 \
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 \
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 \
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 \
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 \
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 \
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"

    #Lager liste for loddrett og vannrett
    for i in range (20):
        for j in range(20):
            Liste2[i] = Liste2[i] + String[j*60 + i*3 : 3 + j*60 + i*3]
                                                  
                                                 
        Liste1.append(String[i*60 : 59 + i*60])

    #Lager liste for skratt. Lager 4 lister her. Far et element som er felles
    #for 2 lister to ganger, men det er ikke noe problem.
    for j in range(4 , 21):
        i = j - 4
        for k in range(j):
            Ny = String[60*(16 - i) + 63*k \
                        : 60*(16 - i) + 63*k + 3]
            Liste3[i] = Liste3[i] + Ny

            Ny = String[48 - 3*i + 63*k \
                        : 48 - 3*i + 63*k + 3]
            Liste4[i] = Liste4[i] + Ny

            Ny = String[60*(16 - i) + 57 + 57*k \
                        : 60*(16 - i) + 60 + 57*k]
            
            Liste5[i] = Liste5[i] + Ny

            Ny = String[9 + 3*i + 57*k \
                        : 9 + 3*i + 57*k + 3]
            
            Liste6[i] = Liste6[i] + Ny
    #Fjerner her tallene som er skrevet "08" og "09". med 8 og 9 fordi Python
    #behandler de som oktogonal. Siden alt under er det samme for titallsystemet
    #trenger ikke vi a rette det. Og alle tall har to siffer. Sa vi erstatter
    #bare spesialtilfellene 08 og 09!
    for i in range(20):
        Liste1[i] = replace(Liste1[i] , "08" , " 8")
        Liste1[i] = replace(Liste1[i] , "09" , " 9")
        Liste2[i] = replace(Liste2[i] , "08" , " 8")
        Liste2[i] = replace(Liste2[i] , "09" , " 9")
        Liste3[i] = replace(Liste3[i] , "08" , " 8")
        Liste3[i] = replace(Liste3[i] , "09" , " 9")
        Liste4[i] = replace(Liste4[i] , "08" , " 8")
        Liste4[i] = replace(Liste4[i] , "09" , " 9")
        Liste5[i] = replace(Liste5[i] , "08" , " 8")
        Liste5[i] = replace(Liste5[i] , "09" , " 9")
        Liste6[i] = replace(Liste6[i] , "08" , " 8")
        Liste6[i] = replace(Liste6[i] , "09" , " 9")
    for i in range(0 , 17):
        for j in range(i):
            Liste = Liste3[i]
            Temp1 = int(Liste[j*3 : j*3 + 3]) * \
                    int(Liste[j*3 + 3 : j*3 + 6]) * int(Liste[j*3 + 6 : j*3 + 9])\
                    * int(Liste[j*3 + 9 : j*3 + 12])
            Temp2 = int(Liste[j*3 : j*3 + 3]) * \
                    int(Liste[j*3 + 3 : j*3 + 6]) * int(Liste[j*3 + 6 : j*3 + 9])\
                    * int(Liste[j*3 + 9 : j*3 + 12])
            Liste = Liste5[i]
            Temp3 = int(Liste[j*3 : j*3 + 3]) * \
                    int(Liste[j*3 + 3 : j*3 + 6]) * int(Liste[j*3 + 6 : j*3 + 9])\
                    * int(Liste[j*3 + 9 : j*3 + 12])
            Liste = Liste6[i]
            Temp4 = int(Liste[j*3 : j*3 + 3]) * \
                    int(Liste[j*3 + 3 : j*3 + 6]) * int(Liste[j*3 + 6 : j*3 + 9])\
                    * int(Liste[j*3 + 9 : j*3 + 12])
            if Temp1 > Maks:
                Maks = Temp1
            if Temp2 > Maks:
                Maks = Temp2
            if Temp3 > Maks:
                Maks = Temp3
            if Temp4 > Maks:
                Maks = Temp4
    for i in range(17):
        Liste = Liste1[i]
        Temp1 =  int(Liste[i*3 : i*3 + 3]) * \
                    int(Liste[i*3 + 3 : i*3 + 6]) * int(Liste[i*3 + 6 : i*3 + 9])\
                    * int(Liste[i*3 + 9 : i*3 + 12])
        Liste = Liste2[i]
        Temp2 = int(Liste[i*3 : i*3 + 3]) * \
                    int(Liste[i*3 + 3 : i*3 + 6]) * int(Liste[i*3 + 6 : i*3 + 9])\
                    * int(Liste[i*3 + 9 : i*3 + 12])
        if Temp1 > Maks:
            Maks = Temp1
        if Temp2 > Maks:
            Maks = Temp2

        
    print Maks


def Nummer12():
    Teller, Teller2, Total = 1, 0, 0
    while Teller2 < 500:
        Teller2 = 0
        Total = Total + Teller
        for i in range(1 , int(Total**0.5) + 1):
            if Total % i == 0:
                Teller2 = Teller2 + 2
        Teller += 1
    print Total
    raise SyntaxError

def Nummer13():
    Fil = open("Radata" , "r")
    Total = 0
    for i in Fil:
        Linje = i[0:11]
        Total = int(Linje) + Total
    print Total

def Nummer14():
    Pa = 1
    Max = 0
    MaxTall = 0
    Prosent = 0
    Prosent2 = 0
    for Ny in range(2 , 1000000):
        Tall = Ny
        Tall2 = Ny
        Teller = 0
        if Prosent2 != Prosent:

            print Prosent
        Prosent2 = Prosent
        while Pa == 1:
            if Ny % 10000 == 0:
                Prosent =  Ny/10000
            if Tall % 2 == 0 and Tall == Tall2:
                break
            if Tall % 2 == 0:
                Teller = Teller + 1
                Tall = Tall/2
            else:
                if Tall != 1:
                    Tall = Tall*3 + 1
                    Teller = Teller + 1
                else:
                    if Teller > Max:
                        Max = Teller
                        MaxTall = Ny
                    break
    print Max
    print MaxTall

def Fakultet(n):
    Produkt = 1
    if n == 0:
        return Produkt
    elif n==1:
        return Produkt
    else:
        for i in range(n):
            Produkt = (i + 1)*Produkt
        return Produkt
    
def Nummer15():
    a= time()
    Tall = Fakultet(40)/(Fakultet(20)*Fakultet(20))
    b = time()
    print b - a
    print Tall

def Nummer16():
    x = str(2**1000)
    Tall = 0
    print len(x)
    for i in range (len(x)):
        Tall = Tall + int(x[i])
    print Tall

def Nummer17():
    Hundre = 100
    Sum = 0
    Teller = 0
    Num0_19 = [0 , 3 , 3 , 5 , 4 , 4 , 3 , 5 , 5 , 4 , \
               3 , 6 , 6 , 8 , 8 , 7 , 7 , 9 , 8 , 8]
    Num20_90 = [6 , 6 , 5 , 5 , 5 , 7 , 6 , 6]
    Num100_900 = [13 , 13 , 15 , 14 , 14 , 13 , 15 , 15 , 14]
    Num1000 = 11
    for i in range(1 , 1001):
        if i < 20:
            Sum = Sum + Num0_19[i]
        elif 20 <= i < 100:
            if i/10 == float(i)/10:
                Teller = 0
            Sum = Sum + Num20_90[int(i - 20)/10] + Num0_19[Teller]
            Teller = Teller + 1
        elif 100 <= i < 1000:
            Sum = Sum + Num100_900[int(i - 100)/100]
            if i == Hundre:
                Hundre = Hundre + 100
                Teller = 0
                Sum = Sum - 3
            elif 0 < i - Hundre + 100 < 20:
                Teller = Teller + 1
                Sum = Sum + Num0_19[Teller]
                if Teller == 19:
                    Teller = 0
            elif 20 <= i - Hundre + 100 < 100:
                if Teller/10 == 1:
                    Teller = 0
                    Sum = Sum + Num20_90[int(i - Hundre + 100 - 20)/10]
                    Teller = Teller + 1
                else:
                    Sum = Sum + Num20_90[int(i - Hundre + 100 - 20)/10]\
                          + Num0_19[Teller]
                    Teller = Teller + 1
        if i == 1000:
            Sum = Sum + Num1000
    print Sum

def Nummer18():
    Max = 0
    Pos = 0
    start = 75
    String = []
    Temp = []
    av = 0
    teller = 0
    String.append("75")
    String.append("95 64")
    String.append("17 47 82")
    String.append("18 35 87 10")
    String.append("20 04 82 47 65")
    String.append("19 01 23 75 03 34")
    String.append("88 02 77 73 07 63 67")
    String.append("99 65 04 28 06 16 70 92")
    String.append("41 41 26 56 83 40 80 70 33")
    String.append("41 48 72 33 47 32 37 16 94 29")
    String.append("53 71 44 65 25 43 91 52 97 51 14")
    String.append("70 11 33 28 77 73 17 78 39 68 17 57")
    String.append("91 71 52 38 17 14 91 43 58 50 27 29 48")
    String.append("63 66 04 68 89 53 67 30 73 16 69 87 40 31")
    String.append("04 62 98 27 23 09 70 98 73 93 38 53 60 04 23")
    for i in range(15):
        String[i] = replace(String[i] , "09" , "9")
        String[i] = replace(String[i] , "08" , "8")
        String[i] = split(String[i] , " ")
    for i in range(14):
        for j in range(2):
            Temp.append(14)
            if j is 0:
                Pos = Pos
                Temp[teller]
            if j is 1:
                Pos = Pos + 1
            teller = teller + 1

    print Max

def nummer19():
    dager = ["Monday" , "Tuesday" , "Wedensday" , "Thursday" , "Friday" ,\
             "Saturday" , "Sunday"]
    maneder = [31 , 28 , 31 , 30 , 31 , 30 , 31 , 31 , 30 , 31 , 30 , 31]
    ar_lengde = [0]
    ar = []
    man1 = [1]
    sondager = []
    totaldag = 0
    teller = 0
    for i in range(1901 , 2001):
        temp = 1 + totaldag
        ar.append(i)
        if i % 4 == 0:
            if str(i)[2:] == "00":
                if i % 400 == 0:
                    ar_lengde.append(366)
                    maneder[1] = 29
                else:
                    ar_lengde.append(365)
                    maneder[1] = 28
            else:
                ar_lengde.append(366)
                maneder[1] = 29
        else:
            ar_lengde.append(365)
            maneder[1] = 28
        for j in range (12):
            temp = maneder[j] + temp
            man1.append(temp)
        totaldag = ar_lengde[i - 1900] + totaldag
    for i in man1:
        if i % 7 == 0:
            teller = teller + 1
    print teller - 2

def nummer20():
    initial = 1
    total = 0
    for i in range(1 , 100):
        initial = initial*i
    initial = str(initial)
    for i in range(len(initial)):
        total = total + int(str(initial)[i])
    print total
                   
        
def nummer21():
    total = 0
    liste = []
    for i in range(10000):
        a = 0

def modul22a(liste , alfabet):
    for bokstav in range(len(alfabet)):
        liste = replace (liste , alfabet[bokstav] , " "+str(bokstav + 1))
    liste = liste[1: len(liste)]
    liste = split(liste , " ")
    return liste

def nummer22():
    fil = open("names.txt" , "r")
    alfabet = ["A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , \
               "I" , "J" , "K" , "L" , "M" , "N" , "O" , "P" , \
               "Q" , "R" , "S" , "T" , "U" , "V" , "W" , "X" , \
               "Y" , "Z"]
    i = 0
    maks = 0
    string = fil.readline()
    liste = split(string , ",")
    liste2 = []
    for i in range(len(liste)):
        liste[i] = liste[i][1 : len(liste[i]) - 1]
    for i in range(len(liste)):
        liste[i] = modul22a(liste[i] , alfabet)
        temp = len(liste[i]) - 1
        if temp > maks:
            maks = temp
    for i in range(maks):
        for j in range(len(liste)):
            if i <= len(liste[j]) - 1:
                tall = int(liste[j][0])
                for bokstav in range(26):
                    if tall == bokstav:
                        liste2.append(liste[i])
    print liste2[0 : 20]

def abundant(lengde):
    liste = []
    verdi = 0
    for i in range(2 , lengde):
        temp_liste = [1]
        for j in range(2 , int(i**0.5) + 1):
            verdi = 0
            if i % j is 0:
                temp_liste.append(j)
                if float(j) != i**0.5:
                    temp_liste.append(i/j)
        for j in range(len(temp_liste)):
            verdi = verdi + temp_liste[j]
        if verdi > i:
            liste.append(i)
    return liste

def abundantsum(lengde , alleliste):
    liste = abundant(lengde)
    liste3 = []
    teller = 0
    teller2 = 0
    teller3 = 0
    i = 0
    while i < len(liste)/2:
        for i in liste:
            print i
            for j in liste[i : len(liste) - 1]:
                if i + j > lengde:
                    break
                elif i + j in liste3:
                    x = 0
                else:
                    liste3.append(i + j)
        return liste3

def alletall(lengde):
    alle = 0
    alleliste = []
    for i in range(lengde + 1):
        alle = alle + i
        alleliste.append(i)
    return alle , alleliste

def nummer23():
    lengde = 28123
    alle , alleliste = alletall(lengde)
    liste3 = abundantsum(lengde , alleliste)


#Nummer5v3()
Nummer10v3(100000)
