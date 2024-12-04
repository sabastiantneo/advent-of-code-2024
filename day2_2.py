ls = [] 

with open("day2.txt", "r") as file: 
    for line in file: 
        row = line.split() 
        ls.append(row)

sum_of_safe = 0 



for row in ls: 
    if len(row) > 2: 
        safe = True 
        strictly = False 
 
        #for sequences with a difference of 3 or higher 
        for i in range(len(row)-1): 
            if abs(int(row[i])- int(row[i+1])) > 3: 
                safe = False 
                break 
        
        if safe: 
            if all(int(row[i]) > int(row[i+1]) for i in range(len(row)-1)) or all(int(row[i]) < int(row[i+1]) for i in range(len(row)-1)): 
                sum_of_safe += 1 
                strictly = True 

        if not strictly:
            for skip in range(len(row)): 
                temp_list = row[:skip] + row[skip+1:] 
                temp_safe = True

                # Check if the modified row is valid
                for j in range(len(temp_list) - 1):
                    if abs(int(temp_list[j]) - int(temp_list[j+1])) > 3:
                        temp_safe = False
                        break

                # Check for strict monotonicity in the modified row
                if temp_safe:
                    is_increasing = all(int(temp_list[j]) < int(temp_list[j+1])for j in range(len(temp_list)-1))
                    is_decreasing = all(int(temp_list[j]) > int(temp_list[j+1])for j in range(len(temp_list)-1))
                    if is_increasing or is_decreasing:
                        sum_of_safe += 1
                        break  

print(sum_of_safe)
            
            

        

             