""" 
READ THE FILE WITH THE LIST BEFORE THE FILE WITH TUPLES. 
FUNCTION TO READ THE LIST AND COMPARE WITH TUPLES. 
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


def check_sequence(a, b): 
    for pair in ls_s[:-1]: 
        y = pair.split(",")
        if a == y[0] and b == y[1] or a==b : 
            return True 
    return False
        
        
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
            break
        elif j == len(string) and valid == True:
                break
        
    if valid == True:            
        count += int(find_middle(string))

print(count)

