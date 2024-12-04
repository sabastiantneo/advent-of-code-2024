import re
text_list = []

with open("day4.txt") as file: 
    for line in file: 
        row = line.split()
        text_list.extend(row)


"""DID WORK IN THE END"""
count = 0 
#check for horizontal
for row in text_list: 
    h_count = re.findall(r"XMAS", row)
    h_count_re = re.findall(r"SAMX", row)  #for 9-3 and 3-9 
    count += (len(h_count + h_count_re))
    
#check for vertical 
for i in range(len(text_list)-3): 
    for j in range(len(text_list[i])): 
        if text_list[i][j] == "X" and text_list[i+1][j] == "M" and text_list[i+2][j] == "A" and text_list[i+3][j] == "S":
            count += 1 #for 12 - 6
        if text_list[i][j] == "S" and text_list[i+1][j] == "A" and text_list[i+2][j] == "M" and text_list[i+3][j] == "X":
            count += 1 #for 6 -12 
    #check for diagonal left
    for j in range(len(text_list[i])-3):    
        if text_list[i][j] == "X" and text_list[i+1][j+1] == "M" and text_list[i+2][j+2] == "A" and text_list[i+3][j+3] == "S":
            count += 1 #for 10 - 4
        if text_list[i][j] == "S" and text_list[i+1][j+1] == "A" and text_list[i+2][j+2] == "M" and text_list[i+3][j+3] == "X":
            count += 1 #for 4 - 10 
    #check for diagonal right 
        if text_list[i][j+3] == "X" and text_list[i+1][j+2] == "M" and text_list[i+2][j+1] == "A" and text_list[i+3][j] == "S":
            count += 1  # for 2 - 8 
        if text_list[i][j+3] == "S" and text_list[i+1][j+2] == "A" and text_list[i+2][j+1] == "M" and text_list[i+3][j] == "X":
            count += 1 # for 8 - 2 

print(count)
