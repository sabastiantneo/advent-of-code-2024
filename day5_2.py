"""
append wrong answers and solve
"""

ls_s =[] 
ls_l=[] 


with open("day5_sequence.txt") as file: 
    for row in file: 
        x = row.strip().replace("|", ",")
        ls_s.append(x)

with open("day5_list.txt") as file: 
    for row in file: 
        x = row.strip().split(",")
        ls_l.append(x)

ls_incorrect = [] #incorrect list 

def check_sequence(a, b): 
    for pair in ls_s[:-1]: 
        y = pair.split(",")
        if a == y[0] and b == y[1] or a==b : 
            return True 
    return False 

def check_sequence_2(a, b): 
    for pair in ls_s[:-1]: 
        y = pair.split(",")
        if a == y[0] and b == y[1] or a==b : 
            return True 
        else:
           if a == y[1] and b == y[0]:
                b = y[1]
                a = y[0]
                return a, b
        
        
def find_middle(s): 
    return s[int(len(s)/2-0.5)]


valid = False
count = 0 
for string in ls_l[:-1]: 
    for keynumber in range(len(string)): 
        for j in range(keynumber, len(string)): 
            if check_sequence(string[keynumber], string[j]) == True: 
                valid = True 
            else: 
                valid = False
                break
        if valid == False:
            ls_incorrect.append(string)
            break
       
for string in ls_incorrect: 
    while True:
        for keynumber in range(len(string)): 
            for j in range(keynumber, len(string)): 
                if check_sequence(string[keynumber], string[j]) == True: 
                    valid = True 
                else: 
                    a, b =check_sequence_2(string[keynumber], string[j])
                    string[keynumber] = a 
                    string[j] = b   
        if j == len(string) and valid == True:
                break
        break      

    if valid == True:            
        count += int(find_middle(string))


print(count)

