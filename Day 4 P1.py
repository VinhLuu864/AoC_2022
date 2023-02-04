import re
pairs = 0


file4 = open("Inputs/input4", 'r')
for line in file4:
    nums = re.split('\D', line.strip())
    
    #right range inside left
    if int(nums[0]) <= int(nums[2]) and int(nums[3]) <= int(nums[1]):
        pairs += 1
        continue
        
    #left range inside right
    if int(nums[0]) >= int(nums[2]) and int(nums[3]) >= int(nums[1]):
        pairs += 1
        continue
        
print(pairs)