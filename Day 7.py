file7 = open('Inputs/input7', 'r')

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Tree:
    def __init__(self, name, size, contained):
        self.children = []
        self.name = name
        self.size = size
        self.contained = contained #keep track of which directory this node is in.

root = Tree('/', 0, None)
rootPointer = root
currDir = root

for line in file7:
    line = line.strip().split(" ")
    print(line)
    if line[0] == '$':
        #$ cd /
        if line[1] == 'cd':
            if line[2] == "/":
                currDir = rootPointer
            elif line[2] == ".." and currDir != root:
                currDir = currDir.contained
            else:
                for i in currDir.children:
                    if i.name == line[2]:
                        nextDir = i
                currDir = nextDir

    #$ ls - We can skip this command for now.
        if line[1] == 'ls':
            continue
    # dir, name
    elif line[0] == 'dir':
        newNode = Tree(line[1], 0, currDir)
        currDir.children.append(newNode)
    # number, file name
    else:
        newNode = File(line[1], eval(line[0]))
        currDir.children.append(newNode)

def helper(head):
    for i in head.children:
        if isinstance(i, Tree):
            helper(i)
            head.size += i.size
        else:
            head.size += i.size
    return

helper(root)

count = []
count.append(root.size)
def counter(head):
    for i in head.children:
        if isinstance(i, Tree):
            count.append(i.size)
            counter(i)
    return

counter(root)
print(max(count) - 30000000) #40528671 is total used storage (from root)
print(70000000 - 40528671) #29471329 free space
print(30000000 - 29471329) #We need 528671 free space
new_count = [x for x in count if x > 528671]
print(min(new_count))


