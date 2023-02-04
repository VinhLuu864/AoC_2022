import re
outside = 0

file4 = open("Inputs/input4", 'r')
for line in file4:
    nums = re.split('\D', line.strip())
    #left range left value inside right range
    if int(nums[0]) >= int(nums[2]) and int(nums[0]) <= int(nums[3]):
        outside += 1
        continue
    #left range right value inside right range
    if int(nums[1]) >= int(nums[2]) and int(nums[1]) <= int(nums[3]):
        outside += 1
        continue
    #Right range right value inside left range
    if int(nums[2]) >= int(nums[0]) and int(nums[2]) <= int(nums[1]):
        outside += 1
        continue
    #Right range left value inside left range
    if int(nums[3]) >= int(nums[0]) and int(nums[3]) <= int(nums[1]):
        outside += 1
        continue   

print(outside)