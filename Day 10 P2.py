def helper(register, cycle):
    sprite = list(range(register-1, register+2, 1))
    if cycle in sprite:
        return '#'
    else:
        return '.'


with open('input10') as file:
    cycle = 0
    register = 1
    screen = ['.'] * 240

    for instruction in file:
        instruction = instruction.strip()

        print((cycle)%40, register)
        
        if instruction == 'noop':
            screen[cycle] = helper(register, (cycle) % 40)
            cycle += 1
            

        else:
            
            screen[cycle] = helper(register, (cycle) % 40)
            cycle += 1
            screen[cycle] = helper(register, (cycle) % 40)
            cycle += 1
           
            register += int(instruction.split(' ')[1])


print(screen)


