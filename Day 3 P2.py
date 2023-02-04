points = 0

file3 = open("Inputs/input3", 'r')
for line in file3:
    first = [line.strip(), file3.readline().strip(), file3.readline().strip()]
    
    for i in first[0]:
        if i in first[1] and i in first[2]:
            if i.isupper():
                points += ord(i) - 38
            else:
                points += ord(i) - 96
            break

print(points)