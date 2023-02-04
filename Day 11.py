import re

class Monkey:
    def __init__(self, items, operation, operation_num, test_condition, testF, testT):
        self.items = items
        self.operation = operation
        self.operation_num = operation_num
        self.test_condition = test_condition
        self.testF = testF
        self.testT = testT
        self.inspected = 0

counter_obj = 0
object_dict = {}
with open('input11') as file11:
    while True:
        file11.readline()
        items = re.split('[:,]', file11.readline().strip())[1:]
        opLine = file11.readline().strip().split()
        operation, operation_num = opLine[4], opLine[5]
        test_condition = int(file11.readline().strip().split()[3])
        testT = int(file11.readline().strip().split()[5])
        testF = int(file11.readline().strip().split()[5])

        #set up an object with this stuff before the next cycle
        object_dict[counter_obj] = Monkey(items, operation, operation_num, test_condition, testF, testT)
        counter_obj += 1

        if not file11.readline():
            break

#Find GCD
gcd = 1
for key in object_dict.keys():
    gcd *= int(object_dict[key].test_condition)
 

for cycle in range(10000):
    for key in object_dict.keys():
        while object_dict[key].items:
            #Operation stuff
            item = object_dict[key].items.pop(0)
            object_dict[key].inspected += 1

            if object_dict[key].operation_num == 'old':
                new_val = (int(item) * (int(item)))
            elif object_dict[key].operation == '+':
                new_val = (int(item) + int(object_dict[key].operation_num))
            elif object_dict[key].operation == '*':
                new_val = (int(item) * int(object_dict[key].operation_num)) 
            #Test
            if new_val % int(object_dict[key].test_condition) == 0:
                object_dict[object_dict[key].testT].items.append(new_val % gcd)
            else:
                object_dict[object_dict[key].testF].items.append(new_val % gcd)
              
for key in object_dict.keys():
    print(object_dict[key].inspected)   