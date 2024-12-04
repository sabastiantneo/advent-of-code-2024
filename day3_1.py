import re
ls = []
ls1 = [] 
with open("day3.txt") as file: 
    for line in file: 
        eqn = re.findall(r"mul\(\d+,\d+\)", line)
        ls.extend(eqn)

for i in ls: 
    x = re.search(r"\d+,", i)
    x = x.group()
    x = x.replace(",", "")
    y = re.search(r",\d+", i)
    y = y.group()
    y = y.replace(",", "")
    ls1.append(int(x)*int(y))
print(sum(ls1))