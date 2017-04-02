from string import ascii_uppercase
#new_str1 = "=getNotes(\"K%d\", GoogleClock())\n"
#new_str1 = "=IFERROR(VLOOKUP($G%d, $A$2:$H$200, COLUMN(H%d), FALSE), \"-\")\n"
new_str1 = "= INDIRECT(\"\'Raw MTC'!"
new_str2 = "\" &C2)"


new_file = open("getnotes.txt", "w")
out_str = ""
for c in ascii_uppercase:
    out_str += new_str1 + c + new_str2 + "\t"
new_file.write(out_str)
new_file.close()


    

