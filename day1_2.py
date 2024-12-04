ls= []
left_column = []
right_column = [] 
value_difference = []

with open("day1.txt","r") as file: 
     for line in file:
          row = line.split() 
          if(len(row)) == 2:
               ls.append(row)
               
for i in range(len(ls)): 
     left_column.append(ls[i][0])
     right_column.append(ls[i][1])

similar_value = []

for i in range(len(left_column)): 
     count = 0
     similarity = 0 
     for j in range(len(right_column)): 
          if right_column[j] == left_column[i]: 
               count += 1 
     similarity += int(left_column[i])*count
     similar_value.append(similarity)

print(sum(similar_value))