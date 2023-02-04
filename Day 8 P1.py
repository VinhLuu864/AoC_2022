with open('input8') as file8:
    forest = [[int(x) for x in line.strip()] for line in file8]

#forest = [[3,0,3,7,3], [2,5,5,1,2], [6,5,3,3,2], [3,3,5,4,9], [3,5,3,9,0]]

top, bottom = 0, len(forest) - 1
left, right = 0, len(forest[0])-1

#we use this set to note which trees were already counted.
forest_set = set()

#check down
for y in range(left, right+1):
    counter = -1
    for x in range(top, bottom+1):
        current = forest[x][y]
        if counter == 9:
            break
        elif current > counter:
            forest_set.add((x, y))
            counter = current


#check up
for y in range(left, right+1):
    counter = -1
    for x in range(bottom, top-1, -1):
        current = forest[x][y]
        if counter == 9:
            break
        elif current > counter:
            if (x, y) not in forest_set:
                forest_set.add((x, y))
            counter = current


#check left
for x in range(top, bottom+1):
    counter = -1
    for y in range(left, right+1):
        current = forest[x][y]
        if counter == 9:
            break
        elif current > counter:
            if (x, y) not in forest_set:
                forest_set.add((x, y))
            counter = current

#check right
for x in range(top, bottom+1):
    counter = -1
    for y in range(right, left, -1):
        current = forest[x][y]
        if counter == 9:
            break
        elif current > counter:
            if (x, y) not in forest_set:
                forest_set.add((x, y))
            counter = current
            
print(len(forest_set))