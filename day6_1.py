"""
FIND WHERE IS GUARD, WHICH DIRECTION FACED, AND WALK THE ROWS/COLUMNS 
"""
grid = []
with open("day6.txt") as file:
    for line in file:
        line = line.strip()
        grid.append(line)
grid = [list(row) for row in grid]
grid.pop() #remove empty list at the end 

rows = len(grid)
cols = len(grid[0])
up = '^'


def get_pos(): 
    for r in range(rows): 
        for c in range(cols): 
            if grid[r][c] == up: 
                #print(r, c)
                return r, c 
            

def north(rowpos, colpos):
    for i in range(rows):  
        if i - rowpos == 0 and grid[rowpos-i][colpos] != "#": #if the security reach the end
            return rowpos-i, colpos
        if grid[rowpos-i][colpos] != '#': 
            grid[rowpos-i][colpos] = 'X' #marking the trails of the periods covered
        else: 
            rowpos = rowpos-i+1 #get new position before turning 
            a, b = east(rowpos, colpos) #turning right 
            return a, b
def east(rowpos, colpos):
    for i in range(cols): 
        if i + colpos == cols and grid[rowpos][colpos+i-1] != "#": 
            return rowpos, colpos + i
        if grid[rowpos][colpos+i] != '#':
            grid[rowpos][colpos+i] = 'X'
        else: 
            colpos = colpos+i-1 
            a, b = south(rowpos, colpos)
            return a, b
def south(rowpos, colpos):
    for i in range(rows): 
        if i + rowpos == rows and grid[rowpos+i-1][colpos] != "#":
            return rowpos+i, colpos
        if grid[rowpos+i][colpos] != '#':
            grid[rowpos+i][colpos] = 'X'
        else: 
            rowpos = rowpos+i-1 
            a, b = west(rowpos, colpos)
            return a, b
def west(rowpos, colpos):
    for i in range(cols): 
        if i - colpos == 0 and grid[rowpos][colpos-i] != "#":
            return rowpos, colpos -i
        if grid[rowpos][colpos-i] != '#':
            grid[rowpos][colpos-i] = 'X'
        else: 
            colpos = colpos-i+1 
            a, b = north(rowpos, colpos)
            return a, b

rowpos, colpos = get_pos() #position of guard 
a, b = int(rowpos), int(colpos)
north(a, b) 

og_grid = grid

ls_total = []
for i in grid: 
    ls_total.append(i.count("X"))
# print(sum(ls_total)+1) #for last period during exit 
# print(og_grid)

