#Writer2

import math, datetime, time


class Pattern:
    
    def __init__(self):

        self.marks = {"Offset" : 10, "Layer" : 1, "Width" : [0, 0], 
                "Dose" : 0, "Length" : [0, 80, 0.20], "Top Left" : [0, 0], 
                "Bottom Right" : [0, 0]
                }

        self.zones = {"Width" : 0, "lambda" : 0, "g" : 0, "b" : 0, 
                        "Radius" : 0, "X" : [], "Y" : [], "Seperators" : [],
                        "Layer" : 0, "Dose" : 0, "Position" : [0, 0]
                }

        self.output = {"Filename" : "test", "Extension" : "asc", 
                }

        self.parameters = {"Width" : 0, "lambda" : 0, "g" : 0, "b" : 0,
                        "Radius" : 0, "Layer" : 0, "Dose" : 0, 
                        "Position" : [0, 0], "Sub Lines" : 1
                        }
        self._parameters = {"r_in" : 0, "r_out" : 0, "n_lines" : 0, 
                "dr" : 0, "d_angle" : 0, "Condition" : 0, "f" : 0,
                "Radius Breakpoint" : [], "Seperators" : [], "Widths" : [], 
                "Angle Offset" : 0

                }

        self._data = {
            "circle_pos" : [0, 0], "file" : None, "started" : False
            }

    
    def Gen_Zones(self):
        n = 1
        radii = []
        f, radius, position, _lambda = self._Get_Parameters()
        self._parameters["r_out"] = 0
        while True:
            self._Update_Coeffs(n)
            if self._parameters["r_in"] > self.parameters["Radius"]:
                break
            if self._parameters["r_out"] > self.parameters["Radius"]:
               self._parameters["r_out"] = self.parameters["Radius"]
            r_in = self._parameters["r_in"]
            r_out = self._parameters["r_out"]
            radii.append(r_in)
            radii.append(r_out)
            n += 2
        self._Zones_Output(radii)


    def Test_Pattern(self, width, height, lines, y0):
        x = [0, width]
        y = [0, 0]
        line_width = self.parameters["Width"]
        if self.parameters["Width"] <= 0.01:
            line_width = 0.01
        orig_dose = self.parameters["Dose"]
        for i in range(lines):
            self.parameters["Dose"] =  orig_dose*(float(i + 1)/lines)
            y = [height*(float(i)/lines) + y0 for j in y]
            self._Sub_Lines(0, line_width, x, y)
        self.parameters["Dose"] = orig_dose
    
    def Test_Pattern2(self, width, height, lines, y0):
        x = [0, width]
        y = [0, 0]
        line_width = self.parameters["Width"]
        if self.parameters["Width"] <= 0.03:
            raise Exception("Too thin line moron.")
        orig_dose = self.parameters["Dose"]
        for i in range(lines):
            self.parameters["Dose"] =  orig_dose*(float(i + 1)/lines)
            y = [height*(float(i)/lines) + y0 for j in y]
            new_width = line_width - 0.02
            self._Support_Output(x, y, new_width)
            y = [i + 0.5*line_width - 0.005 for i in y]
            self._Support_Output(x, y, 0)
            y = [i - line_width + 0.01 for i in y]
            self._Support_Output(x, y, 0)
        self.parameters["Dose"] = orig_dose

    def _Zones_Output(self, radii):
        lay = self.parameters["Layer"]
        dose = self.parameters["Dose"]
        pos = self.parameters["Position"]
        node_attribute = 0
        node_type = 2
        newstring = ""
        i = 1
        while True:
            width = radii[i + 1] - radii[i]
            newstring += "F %.1f %i %.4f \n" % (dose, lay, width)
            radius = (radii[i + 1] + radii[i])/2
            data = (node_type, node_attribute, pos[0], pos[1], radius)
            newstring += "%.0f, %.0f, %.4f, %.4f, %.4f\n#\n" % data
            i += 2
            if i + 1 >= len(radii):
                break
        newstring += "#\n"
        self._data["file"].write(newstring)


        
    def Gen_Support_Pattern(self):
        self._Support_Breakpoints()
        self._Support_Coords()
        file_name =  self.output["Filename"] + "." + self.output["Extension"]
        print "Support data written to " + file_name


    def Marks(self):
        lay = self.marks["Layer"]
        dose = self.marks ["Dose"]
        Cor = [self.marks["Top Left"], self.marks["Bottom Right"]]
        Cor.append([self.marks["Top Left"][0], self.marks["Bottom Right"][1]])
        Cor.append([self.marks["Bottom Right"][0], self.marks["Top Left"][1]])
        newstring = ""
        for i in range(len(Cor)):
            center = Cor[i][:]
            data = self._Mark_Coords(center)
            wid = self.marks["Width"][0]
            for j in range(6):
                if j > 3:
                    wid = self.marks["Width"][1]
                #FBMS:
                #newstring += "F %.1f %i %.1f \n" % (dose, lay, wid)
                #newstring += "%.0f, %.0f, %.4f, %.4f, %.0f\n" % data[2*j]
                #newstring += "%.0f, %.0f, %.4f, %.4f, %.0f\n#\n" % data[2*j + 1]

                #Line-Write:
                newstring += "L %.1f %i %.1f \n" % (dose, lay, wid)
                newstring += "%.4f %.4f\n" % data[2*j]
                newstring += "%.4f %.4f\n#\n" % data[2*j + 1]
        self._data["file"].write(newstring)


    def GenFile(self, name = ""):
        date = datetime.date.today()
        dateS = date.strftime("%d_%m_%y")
        radi = str(self.parameters["Radius"])
        if radi == "0":
            radi = str(self.parameters["Radius"]) + "_micro"
        self.output["Filename"] = name + "__" + radi + "__" + dateS
        filename = self.output["Filename"] + "." + self.output["Extension"]
        self._data["file"] = open(filename, "w")


    def _Support_Breakpoints(self):
        self._parameters["Widths"].append(self.parameters["Width"])
        n = 1
        j = 2
        f, radius, position, _lambda = self._Get_Parameters()
        while True:
            self._parameters["n_lines"] = 2**(j/2 + 1)
            self._Update_Coeffs(n)
            if self._parameters["r_out"] > self.parameters["Radius"]:
                break
            if self._parameters["Condition"] > 30:
                check = self._Support_To_Thick()
                if check:
                    break
                j += 2
            n += 2
        while self._parameters["r_out"] < self.parameters["Radius"]:
            self._parameters["n_lines"] = 2**(j/2 + 1)
            self._Update_Coeffs(n)
            rad = self._parameters["r_out"]
            wid = self._parameters["Widths"][-1]
            if self._parameters["Condition"] > 30:
                self._parameters["Radius Breakpoint"].append(rad)
                self._parameters["Widths"].append(wid / 2)
                j += 2
            n += 2


    def _Support_Coords(self):
        n = 1
        j = 2
        f, radius, position, _lambda = self._Get_Parameters()
        self._parameters["r_out"] = 0
        self._Support_Cross()
        self._parameters["Angle Offset"] = math.pi/2
        while True:
            self._parameters["n_lines"] = 2**(j/2 + 1)
            self._Update_Coeffs(n)
            if self._parameters["r_out"] > self.parameters["Radius"]:
                break
            if self._parameters["Condition"] > 30:
                angles = self._Support_Angles()
                for angle in angles:
                    self._Support_Write(angle)
                j += 2
            n += 2


    def _Get_Parameters(self):
        g = self.parameters["g"]*10**6
        b = self.parameters["b"]*10**6
        f = 1/( (1/g) + (1/b) )
        self._parameters["f"] = f
        radius = self.parameters["Radius"]
        position = self.parameters["Position"]
        _lambda = self.parameters["lambda"]*10**6
        return f, radius, position, _lambda


    def _Support_Cross(self):
        rad = self.parameters["Radius"]
        angle = 0
        for i in range(4):
            angle += math.pi/2
            self._Support_Write(angle)


    def _Update_Coeffs(self, n):
        _lambda = self.parameters["lambda"]*10**6
        f = self._parameters["f"]
        n_lines = self._parameters["n_lines"]
        r_out = (n*_lambda*f)**0.5
        r_in = ((n-1)*_lambda*f)**0.5
        dr = abs(r_out - r_in)
        if n_lines != 0:
            length = r_out*2*math.pi/n_lines
            self._parameters["Condition"] = length / dr
        self._parameters["dr"] = dr
        self._parameters["r_out"] = r_out
        self._parameters["r_in"] = r_in

    def _Support_To_Thick(self):
        wid = self._parameters["Widths"][-1]
        rad = self._parameters["r_out"]
        n_lines = self._parameters["n_lines"]
        circum = rad*2*math.pi
        tot_lines = n_lines*2 - 2
        cover = wid*tot_lines
        if cover * 4 >= circum:
            return True
        return False


    def _Support_Angles(self):
        n_lines = self._parameters["n_lines"]
        d_angle = self._parameters["d_angle"]
        self._parameters["Angle Offset"] *= 0.5
        self._parameters["d_angle"] = 2*math.pi/n_lines
        d_angle = self._parameters["d_angle"]
        offset = self._parameters["Angle Offset"]
        angle_list = [offset + d_angle*i for i in range(n_lines)]
        return angle_list


    def _Support_Output(self, x, y, width):
        lay = self.parameters["Layer"]
        dose = self.parameters["Dose"]
        pos = self.parameters["Position"]
        radius = 0
        node_attribute = 0
        node_types = (0, 1)
        #FBMS mode
        #newstring = "F %.1f %i %.3f \n" % (dose, lay, width)
        #Line-Write-Mode
        newstring = "L %.1f %i %.3f \n" % (dose, lay, width)
        for i in range(len(x)):
            new_x = x[i] + pos[0]
            new_y = y[i] + pos[1]
            #using FBMS mode
            #data = (node_types[i], node_attribute, new_x, new_y, radius)
            #newstring += "%.0f, %.0f, %.4f, %.4f, %.0f\n" % data

            #Using line-write-mode
            data = (new_x, new_y)
            newstring += "%.4f %.4f\n" % data
        newstring += "#\n"
        self._data["file"].write(newstring)

    def _Support_Line(self, inner_r, outer_r, angle, width):
        x = []
        y = []
        x.append(inner_r * math.cos(angle))
        x.append(outer_r * math.cos(angle))
        y.append(inner_r* math.sin(angle))
        y.append(outer_r * math.sin(angle))
        x = [i - (i % 0.0032) for i in x]
        y = [i - (i % 0.0032) for i in y]
        if outer_r == self.parameters["Radius"]:
            if self.parameters["Sub Lines"] > 1:
                self._Sub_Lines(angle, width, x, y)
            else:
                self._Support_Output(x, y, width)
        else:
            self._Support_Output(x, y, width)


    def _Sub_Lines(self, angle, width, x, y):
        sub_lines = self.parameters["Sub Lines"]
        factor = width*(sub_lines - 1)/(sub_lines * 2)
        for i in range(2):
            x[i] -= factor*math.sin(angle)
            y[i] += factor*math.cos(angle)
        new_x = [0, 0]
        new_y = [0, 0]
        for i in range(sub_lines):
            for j in range(2):
                new_x[j] = x[j] + width * (float(i) / sub_lines) * math.sin(angle)
                new_y[j] = y[j] - width * (float(i) / sub_lines) * math.cos(angle)
            new_width = width / sub_lines
            if new_width <= 0.01:
                new_width = 0.0
            self._Support_Output(new_x, new_y, new_width)


    def _Support_Write(self, angle):
        b_point = self._parameters["Radius Breakpoint"]
        last_rad = self._parameters["r_out"]
        i = 0
        radius = self.parameters["Radius"]
        width = self.parameters["Width"]
        for j in range(len(b_point)):
            if last_rad >= b_point[j]:
                i = j + 1
        while True:
            width = self._parameters["Widths"][i]
            if i == len(b_point):
                self._Support_Line(last_rad, radius, angle, width)
                break
            self._Support_Line(last_rad, b_point[i], angle, width)
            last_rad = b_point[i]
            i += 1


    def _Mark_Coords(self, center):
        offset = self.marks["Offset"]
        length = self.marks["Length"]
        radius = 0
        node_attrib = 0
        data = []
        for i in range(2):
            fac = (-1)**i
            for j in range(2):
                for k in range(2):
                    newcor = center[:]
                    newlen = length[0]**k
                    newcor[j] += offset*k*fac + offset*newlen*((-1)**k)*fac
                    x = newcor[0]
                    x = x - ( x % 0.0032)
                    y = newcor[1]
                    y = y - ( y % 0.0032)                    
                    node_type = k
                    #FBMS
                    #newdata = (node_type, node_attrib, x, y, radius)
                    #Line Write:
                    newdata = (x, y)
                    data.append(newdata)
        for i in range(2):
            for j in range(2):
                newcor = center[:]
                newcor[i] += offset*length[1]*(2*j - 1)
                x = newcor[0]
                x = x - ( x % 0.0032)
                y = newcor[1]
                y = y - ( y % 0.0032)                    
                node_type = j
                #FBMS
                #newdata = (node_type, node_attrib, x, y, radius)
                #Line Write:
                newdata = (x, y)
                data.append(newdata)
        return data



