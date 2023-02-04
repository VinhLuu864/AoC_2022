points = 0

file3 = open("Inputs/input3", 'r')
for line in file3:
    line = line.strip()
    middle = len(line) // 2
    first = line[0:middle]
    second = line[middle:]
    for i in first:
        if i in second:
            if i.isupper():
                points += ord(i) - 38
            else:
                points += ord(i) - 96
            break

print(points)