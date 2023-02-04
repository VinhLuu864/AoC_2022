file5 = open("input5", 'r')
lines = file5.readlines()
number_of_crates = len(lines[0]) // 4

#separate
crate_lines = lines[:lines.index('\n') - 1]
move_lines = lines[lines.index('\n') + 1:]

#trim off newline
for i in range(0, len(crate_lines)):
    crate_lines[i] = crate_lines[i][:-1]

#set up list of lists
stacks = []
stack_num = 0
for x in range(number_of_crates):
    temp = []
    for i in range(len(crate_lines)-1,-1,-1):
        temp.append(crate_lines[i][stack_num * 4 + 1])
    temp[:] = [x for x in temp if x != ' ']
    stacks.append(temp)
    stack_num += 1
    
#deal with move lines
for line in move_lines:
    temp = []
    number, source, target = [int(line) for line in line.strip().split() if line.isdigit()]
    for i in range(number):
        if not stacks[source-1]:
            continue
        temp.append(stacks[source-1].pop())
    stacks[target-1] = stacks[target-1] + temp[::-1]

print(stacks)