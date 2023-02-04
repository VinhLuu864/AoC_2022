file25 = open("Inputs/input25", 'r')

nums = {'2': 2, '1': 1, '0': 0, '-':-1, '=':-2}
letters = {0:'0', 1:'1', 2:'2', 3:'=', 4:'-'}
numbers = []

#2 options - Convert to decimal and then convert back
#Or just implement the math in base 5

for line in file25:
    line = line.strip()
    place, number = 1, 0
    for i in line[::-1]:
        number += (nums[i] * place)
        place *= 5
    numbers.append(number)
    place, number = 1, 0

print(numbers)
convert = sum(numbers)
#We need 30223327868980 as a snafu number
final_number = ""
while convert > 0:
    #To convert, we mod 5 to find the least significant digit (Deals with carrying as well).
    #We add by 2 to deal with any carrying that may be required, since the normal range for numbers goes from -2 to 2, meaning 8s and 9s needs to be carried over.
    
    final_number = letters[convert % 5] + final_number
    convert = (2 + convert) // 5
    print(convert, letters[convert%5])

print(final_number)