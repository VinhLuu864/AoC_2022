highest_calories = []
temp = []

file = open("Inputs/input", 'r')
for line in file:
    if line.strip() == '':
        highest_calories.append(sum(temp))
        temp = []
    else:
        temp.append(int(line))

#highest_calories = highest_calories.sort()
highest_calories.sort()
print(sum(highest_calories[len(highest_calories)-3:len(highest_calories)]))