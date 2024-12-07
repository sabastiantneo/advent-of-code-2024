from itertools import product 

ls_evaluate = [] 
with open("day7.txt") as file: 
    for line in file: 
        ls_evaluate.append(line.replace(":", "").split())
ls_evaluate.pop()

ls_sum = [] 
for row in ls_evaluate: 
    operators = list(product(["+","*"],repeat=len(row)-2))
    for combi in range(len(operators)): 
        count = int(row[1])
        for j in range(2, len(row)): 
            if operators[combi][j-2] == "+": 
                count += int(row[j])
            if operators[combi][j-2] == "*": 
                count *= int(row[j])
        if count == int(row[0]): 
            ls_sum.append(count)
            break

print(sum(ls_sum))
         
        

    

