file24 = open('Inputs/input24', 'r')

blizzards = []
first_line = file24.readline()
#Read the file into a 2d array
for line in file24:
    row = [x for x in line]
    if row[3] == '#':
        break
    blizzards.append(row[1:151])
    
height = len(blizzards)
length = len(blizzards[0])

start = (0, -1)
stop = (length, height - 1)
minutes = 1

#Rather than saving states, we know each blizzard moves once and loops so we can just
 #check a future blizzard we know will move into the position 
#We have 2 variables we can keep track of. The time (minutes) and our position (x, y). 
#We want to keep track of the minutes, and the posible positions for each step.
def steps():
    global start
    global stop
    global minutes

    positions = set([start])

    while True:
        currentPositions = set()
        for x, y in positions:
            for i, j in ((x,y), (x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if (i, j) == stop:
                    return minutes
                

            #Make sure in bounds and that blizzards will not reach (include wrapping)
                if 0 <= i < length and 0 <= j < height and \
                    blizzards[j][(i + minutes) % length] != '<' and \
                    blizzards[j][(i - minutes) % length] != '>' and \
                    blizzards[(j + minutes) % height][i] != '^' and \
                    blizzards[(j - minutes) % height][i] != 'v':
                        currentPositions.add((i, j))

        positions = currentPositions
        if not positions:
            positions.add(start)
        minutes += 1

#For part 2, we can just make minutes a global variable, and then adjust the start and stop points.
# This preserves the minutes we need to make between runs and we can just call the function consecutively. 

print(steps()) #First pass
start, stop = (length, height - 1), (0, -1)
print(steps()) #Second pass
start, stop = (0, -1), (length, height - 1)
print(steps()) #Third pass