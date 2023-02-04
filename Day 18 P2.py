file18 = open('Inputs/input18', 'r')

cubes = {}
air = {}

#fill cubes
for line in file18:
    nums = [int(x) for x in line.split(",")]
    cubes[tuple(nums)] = 6

def surfaceHelper(dictionary):
    global air
    global cubes
    new = {}
    for nums in dictionary.keys():
        
    #-x face
        neg_x = (nums[0] - 1, nums[1], nums[2])
        if neg_x not in cubes and neg_x not in air:
            new[neg_x] = 1

    #+x face
        pos_x = (nums[0] + 1, nums[1], nums[2])
        if pos_x not in cubes and pos_x not in air:
            new[pos_x] = 1

    #-y face
        neg_y = (nums[0], nums[1] - 1, nums[2])
        if neg_y not in cubes and neg_y not in air:
            new[neg_y] = 1
    #+y face
        pos_y = (nums[0], nums[1] + 1, nums[2])
        if pos_y not in cubes and pos_y not in air:
            new[pos_y] = 1

    #-z face
        neg_z = (nums[0], nums[1], nums[2] - 1) 
        if neg_z not in cubes and neg_z not in air:
            new[neg_z] = 1

    #+z face
        pos_z = (nums[0], nums[1], nums[2] + 1)
        if pos_z not in cubes and pos_z not in air:
            new[pos_z] = 1

    air = air | new
    return 

surfaceHelper(cubes)
for i in range(7):
    surfaceHelper(air)
    #We repeat this X times in order to cover large crevaces.

def countCube(adjacent, check):
    count = 0
    for adj in adjacent:
        if adj in check:
            count += 1
    return count

#A air cube in a pocket will be surrounded on all 6 sides by either air or a cube. Thus, we can check the outside border and remove the air cubes which have 1 or more sides without a bordering air/cube
def remove():
    global air
    global cubes

    delete = []
    exposed_surface = 0
    removed = True
    while removed:
        removed = False
        for key in air.keys():
            nums = list(key)
            neg_x = (nums[0] - 1, nums[1], nums[2])
            pos_x = (nums[0] + 1, nums[1], nums[2])
            neg_y = (nums[0], nums[1] - 1, nums[2])
            pos_y = (nums[0], nums[1] + 1, nums[2])
            neg_z = (nums[0], nums[1], nums[2] - 1)
            pos_z = (nums[0], nums[1], nums[2] + 1)
            check = [neg_x, pos_x, neg_y, pos_y, neg_z, pos_z]

            #If its an open coord - just delete the air cube since its at a border, and continue with the loop
            #We also count how many cube sides are exposed when we remove this air cube
            inCubes = countCube(check, cubes)
            inAir = countCube(check, air)
            
            if inCubes + inAir < 6:
                removed = True
                exposed_surface += inCubes
                delete.append(key)

        for i in delete:
            del air[i]
        delete = []

    return exposed_surface

print(remove())
