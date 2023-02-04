import re

file16 = open('Puzzle Inputs and Test Inputs/input16test.txt', 'r')
valves = {}
connected = {}
for line in file16:
    valve = re.findall("[A-Z][A-Z]", line.strip())
    valves[valve[0]] = int(re.findall("\d+", line.strip())[0])
    connected[valve[0]] = valve[1:]
    
closed = [x for x in valves.keys()]
important = [x for x in closed if valves[x] >= 0]
opened = []
minutes = 30

#calculate the shortest path from start valve to end valve.
def shortestPath(start, end):
    path = []



    return path


while minutes > 0:






    