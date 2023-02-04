file18 = open('Inputs/input18test.txt', 'r')

cubes = {}
for line in file18:
    nums = [int(x) for x in line.split(",")]
    cubes[tuple(nums)] = 6
    #-x face
    neg_x = (nums[0] - 1, nums[1], nums[2])
    if neg_x in cubes:
        cubes[neg_x] -= 1
        cubes[tuple(nums)] -= 1

    #+x face
    pos_x = (nums[0] + 1, nums[1], nums[2])
    if pos_x in cubes:
        cubes[pos_x] -= 1
        cubes[tuple(nums)] -= 1

    #-y face
    neg_y = (nums[0], nums[1] - 1, nums[2])
    if neg_y in cubes:
        cubes[neg_y] -= 1
        cubes[tuple(nums)] -= 1

    #+y face
    pos_y = (nums[0], nums[1] + 1, nums[2])
    if pos_y in cubes:
        cubes[pos_y] -= 1
        cubes[tuple(nums)] -= 1

    #-z face
    neg_z = (nums[0], nums[1], nums[2] - 1)
    if neg_z in cubes:
        cubes[neg_z] -= 1
        cubes[tuple(nums)] -= 1

    #+z face
    pos_z = (nums[0], nums[1], nums[2] + 1)
    if pos_z in cubes:
        cubes[pos_z] -= 1
        cubes[tuple(nums)] -= 1

total = 0
for i in cubes.keys():
    total += cubes[i]

print(total)

