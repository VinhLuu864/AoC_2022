import numpy as np
file9 = open('Puzzle Inputs and Test Inputs/input9', 'r')       

head_coord = (0, 0)
knots = []

for i in range(10):
    knots.append((0,0))

tail_visited = set()
tail_visited.add((0,0))

for line in file9:
    direction = line.split()
    for i in range(int(direction[1])):
    #Analyze the line
    #For loop - move the head
        if direction[0] == 'U':
            knots[0] = (knots[0][0], knots[0][1] + 1)
        elif direction[0] == 'D':
            knots[0] = (knots[0][0], knots[0][1] - 1)
        elif direction[0] == 'L':
            knots[0] = (knots[0][0] - 1, knots[0][1])
        elif direction[0] == 'R':
            knots[0] = (knots[0][0] + 1, knots[0][1])

        #Check the distance of the tail. Move the tail if needed
        for i in range(1, len(knots)):
            x_off = knots[i-1][0] - knots[i][0]
            y_off = knots[i-1][1] - knots[i][1]
            if abs(x_off) > 1 or abs(y_off) > 1:
                knots[i] = (knots[i][0] + np.sign(x_off), knots[i][1] + np.sign(y_off))

        tail_visited.add(knots[9])

print(tail_visited)
print(len(tail_visited))