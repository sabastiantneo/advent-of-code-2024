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

left_column.sort() 
right_column.sort() 
     
for i in range(len(left_column)): 
     value_difference.append(abs(int(left_column[i])-int(right_column[i])))

sum_of_difference = sum(value_difference)


