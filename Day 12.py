file12 = open('input12', 'r')
data = file12.readlines()
#map the letter dictionary
letter_values = dict() # Coordinate : Letter
lowercase = 'abcdefghijklmnopqrstuvwxyz'
shortest_path = dict() # Coordinate : Coordinate

for letter in zip(lowercase, range(1, 27)):
    letter_values[letter[0]] = letter[1]

letter_values['S'] = 0
letter_values['E'] = 27

#Parse the file and map coordinates to values
x0 = -1
elevation_map = dict()
for line in data:
    y0 = 0
    x0 += 1
    for i in line.strip():
        elevation_map[(x0, y0)] = letter_values[i]
        y0 += 1

start = [x for x, y in elevation_map.items() if y == 0][0]
end = [x for x, y in elevation_map.items() if y == 27][0]

#adjust the S and E to be a and z
elevation_map[start] = 1
elevation_map[end] = 26

#neighbors
def neighbors(x0, y0):
    candidates = [(x0 - 1, y0), (x0 + 1, y0), (x0, y0 - 1), (x0, y0 + 1)]
    return [x for x in candidates if x in elevation_map]

#djikstra
distance_from_end = {end: 0}
path_back = [end]
while path_back:
    point1 = path_back.pop(0)
    p1height = elevation_map[point1]
    next_to = neighbors(point1[0], point1[1])
    for point2 in next_to:
        if point2 not in distance_from_end and elevation_map[point1] - elevation_map[point2] <= 1:
            path_back.append(point2)
            distance_from_end[point2] = distance_from_end[point1] + 1

print("Part 1: Distance from start to end is: " + str(distance_from_end[start]))

short_dist = sorted(distance_from_end[p] for p in distance_from_end if elevation_map[p] == 1)[0]
print("Part 2: Distance from start to any a is: " + str(short_dist))