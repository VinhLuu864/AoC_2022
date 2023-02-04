file14 = open('Puzzle Inputs and Test Inputs/input14', 'r')
walls = [line.strip().split("->") for line in file14]
grid = {}
global highest_y
highest_y = 0

for line in walls:
    for i in range(0, len(line)-1):
        left = [int(x) for x in line[i].strip().split(',')]
        right = [int(x) for x in line[i+1].strip().split(',')]

        #part 2 - extra bit
        if left[1] > highest_y:
            highest_y = left[1]
        if right[1] > highest_y:
            highest_y = right[1]


        if left[0] == right[0]:
            for i in range(min(left[1], right[1]) , max(left[1], right[1]) + 1):
                grid[(left[0], i)] = 'x'
        if left[1] == right[1]:
            for i in range(min(left[0], right[0]) , max(left[0], right[0]) + 1):
                grid[(i, left[1])] = 'x'


for i in range(-1000, 1001):
    pair = (i, highest_y+2)
    grid[pair] = 'x'

def sand(x0, y0):
    #stop loop if all options not available
    while True:
        #Check if falling into abyss - part 1
        #if y0 > 200:
            #return 1

        #Part 2
        if (499, 1) in grid and (500, 1) in grid and (501, 1) in grid:
            return 1

        #Fall Straight Down
        if (x0, y0+1) not in grid:
            y0 += 1
        #Fall Down Left
        elif (x0-1, y0+1) not in grid:
            x0 -= 1
            y0 += 1
        #Fall Down Right
        elif (x0+1, y0+1) not in grid:
            x0 += 1
            y0 += 1
        else:
            break

    grid[x0, y0] = 'sand'
    return (x0, y0)

count = 1
while True:
    next_sand = sand(500, 0)
    if next_sand == 1:
        break
    else:
        count += 1
print(count)