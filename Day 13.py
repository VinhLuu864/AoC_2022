import itertools


file13 = open('Puzzle Inputs and Test Inputs/input13', 'r')

def compare(first, second):
    if type(first) == type(second) == int:
        if first < second:
            return 1
        if first > second:
            return -1
        else:
            return 0

    elif type(first) == type(second) == list:
        n, m = len(first), len(second)
        compared = 0
        for i in range(min(n, m)):
            compared = compare(first[i], second[i])
            if compared:
                break
        if compared == 0:
            if n < m:
                return 1
            elif n > m:
                return -1
            else:
                return 0

    elif type(first) == int:
        compared = compare([first], second)
    else:
        compared = compare(first, [second])
    return compared

#start loop - get the pairs out of the file - Part 1
"""pairs = []
counter = 0
for line in file13:
    first_line = line
    second_line = file13.readline()
    file13.readline()
    counter += 1

    if first_line and second_line:
        num = compare(eval(first_line), eval(second_line))
        if num == 1:
            pairs.append(counter)
"""

#start loop - get the pairs in order - Part 2
first_breakpoint = [[2]]
second_breakpoint = [[6]]
index1 = 1
index2 = 2
for line in file13:
    if line.strip():
        num = compare(eval(line), first_breakpoint)
        num2 = compare(eval(line), second_breakpoint)
        if num == 1:
            index1 += 1
        if num2 == 1:
            index2 += 1

print(index1, index2)