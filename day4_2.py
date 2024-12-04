'''
A MUST BE IN THE MIDDLE, [i]j. [i-1][j-1] & [i+1][j+1]/[i-1][j+1] & [i+1][j-1] MUST NOT EQUAL. MUST HAVE 2'S' 2'M' FOR DAI  
'''
#COUNT THE A 
text_list = []


with open("day4.txt") as file: 
    for line in file: 
        row = line.split()
        text_list.extend(row)

row_n = len(text_list)
col_n = len(text_list[0])
is_a = False
count = 0

def check_char(ls): 
    for i in ls:
        if i == "X": 
            return False
    if ls.count("M") != 2 or ls.count("S") != 2: 
        return False
    if ls[0] == ls[3] or ls[1] == ls[2]:
        return False
    return True

for i in range(1, row_n -1): #DO NOT ACCOUNT FOR TOP AND BOTTOM ROW
    for j in range(1, col_n -1): #DO NOT ACCOUNT FOR LEFT AND RIGHT MOST
        if text_list[i][j] == "A": 
            is_a = True
            dia_ls =[]
            dia_ls.extend((text_list[i-1][j-1], text_list[i-1][j+1], text_list[i+1][j-1], text_list[i+1][j+1]))
            if check_char(dia_ls): 
                count += 1
                
print(count)
