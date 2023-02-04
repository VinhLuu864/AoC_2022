import re

def manhattan_distance(x1, y1, x2, y2):
    return abs(y2 - y1) + abs(x2 - x1)

row = 2000000
row_occupied = set()
beacon_in_row = 0

file15 = open('Puzzle Inputs and Test Inputs/input15', 'r')
for line in file15:
    line = line.strip()
    coords = re.split('(-\d+|\d+)', line)
    coords = coords[1:9:2]
    coords = [int(x) for x in coords]
    coords.append(manhattan_distance(coords[0], coords[1], coords[2], coords[3]))

    if coords[3] == row and coords[2] not in row_occupied:
        row_occupied.add(coords[2])
        beacon_in_row += 1

# y2 - y1 and then +- x to get     
    left_edge = coords[0] - (coords[4] - abs(coords[1] - row))
    right_edge = coords[0] + (coords[4] -  abs(coords[1] - row))

    for i in range(left_edge, right_edge+1):
        if i not in row_occupied:
            row_occupied.add(i)

print(len(row_occupied) - beacon_in_row)


