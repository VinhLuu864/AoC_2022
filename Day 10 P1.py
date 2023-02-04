with open('input10') as file:
    counter = 0
    register = 1
    cycles = []

    for instruction in file:
        instruction = instruction.strip()
        print(instruction)
        if (counter - 20) % 40 == 0:
            cycles.append(register)
        if instruction == 'noop':
            counter += 1
        else:
            counter += 1
            if (counter - 20) % 40 == 0:
                cycles.append(register)
            counter += 1
            register += int(instruction.split(' ')[1])

sum = 0
sum_count = 0
for i in range(20, 260, 40):
    sum += i * cycles[sum_count]
    sum_count += 1

print(sum)
    


