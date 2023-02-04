import re

file19 = open('Inputs/input19', 'r')
blueprints = {}
for line in file19:
    nums = re.findall('[\d]+', line)
    nums = [int(x) for x in nums]
    blueprints[nums[0]] = nums[1:]
    
def helper(costs):
    bots = [1, 0, 0, 0]
    resources = [0, 0, 0, 0]

    for _ in range(0, 24):
        #every minute we add 1 resource
        for i in resources:
            resources









    return geode