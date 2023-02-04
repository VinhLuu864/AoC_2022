import re

def manhattan_distance(x1, y1, x2, y2):
    return abs(y2 - y1) + abs(x2 - x1)

def empty(x, y, sensors, beacons):
    for sensor in sensors:
        if manhattan_distance(x, y, sensor[0], sensor[1]) <= sensor[2]:
            return False
    for beacon in beacons:
        if x == beacon[0] and y == beacon[1]:
            return False
    return True


limit = 4000000
def traverse_borders(sensor_x, sensor_y, distance, sensors, beacon):
    if sensor_y - distance < 0:
        width = - (sensor_y - distance)
    else:
        width = 0

    #Traverse Top    
    top = sensor_y - distance - 1
    if top > 0:
        if empty(sensor_x, top, sensors, beacon):
            print("top" + str(top) + "x" + str(sensor_x))
            return True
    #Traverse Bottom
    bottom = sensor_y + distance + 1
    if bottom <= limit + 1:
        if empty(sensor_x, bottom, sensors, beacon):
            print("bot" + str(bottom) + "x" + str(sensor_x))
            return True
    #Traverse Left and right
    for y in range(max(0, sensor_y - distance), min(sensor_y + distance + 1, limit + 1)):
        left = sensor_x - width - 1 
        if left > 0:
            if empty(left, y, sensors, beacon):
                print("left" + str(left) + "y" + str(y))
                return True
        right = sensor_x + width + 1
        if right < limit + 1:
            if empty(right, y, sensors, beacon):
                print("right" + str(right) + "y" + str(y))
                return True
        if y < sensor_y:
            width += 1
        else:
            width -= 1

    return False


signal_list = []
beacon_list = []
file15 = open('input15', 'r')
for line in file15:
    line = line.strip()
    coords = re.split('(-\d+|\d+)', line)
    coords = coords[1:9:2]
    coords = [int(x) for x in coords]
    coords.append(manhattan_distance(coords[0], coords[1], coords[2], coords[3]))
    signal_list.append([coords[0], coords[1], coords[4]])
    beacon_list.append([coords[2], coords[3]])

for sensor in signal_list:
    print(sensor)
    if traverse_borders(sensor[0], sensor[1], sensor[2], signal_list, beacon_list):
        print('done')

print(3292963 * 4000000  + 3019123)