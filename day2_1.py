ls = [] 

with open("day2.txt", "r") as file: 
    for line in file: 
        row = line.split() 
        ls.append(row)

sum_of_safe = 0 


for i in range(len(ls)): 
    if len(ls[i]) > 2: 
        safe = True 
        for j in range(len(ls[i])-1):
            if abs(int(ls[i][j])-int(ls[i][j+1])) > 3: 
                safe = False
                break 
        if safe: 
            if all(int(ls[i][j]) > int(ls[i][j+1]) for j in range(len(ls[i])-1)) or all(int(ls[i][j]) < int(ls[i][j+1]) for j in range(len(ls[i])-1)):
                    sum_of_safe += 1 