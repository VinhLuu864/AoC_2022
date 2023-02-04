import numpy as np
file9 = open('Puzzle Inputs and Test Inputs/input9', 'r')       

head_coord = (0, 0)
tail_coord = (0, 0)

tail_visited = set()
tail_visited.add(tail_coord)

for line in file9:
    direction = line.split()
    for i in range(int(direction[1])):
    #Analyze the line
    #For loop - move the head
        if direction[0] == 'U':
            head_coord = (head_coord[0], head_coord[1] + 1)
        elif direction[0] == 'D':
            head_coord = (head_coord[0], head_coord[1] - 1)
        elif direction[0] == 'L':
            head_coord = (head_coord[0] - 1, head_coord[1])
        elif direction[0] == 'R':
            head_coord = (head_coord[0] + 1, head_coord[1])

        #Check the distance of the tail. Move the tail if needed
        x_off = head_coord[0] - tail_coord[0]
        y_off = head_coord[1] - tail_coord[1]

        if abs(x_off) > 1 or abs(y_off) > 1:
            tail_coord = (tail_coord[0] + np.sign(x_off), tail_coord[1] + np.sign(y_off))
            tail_visited.add(tail_coord)

print(tail_visited)
print(len(tail_visited))