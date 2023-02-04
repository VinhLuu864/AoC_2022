file20 = open('Inputs/input20')
counter = 0
directions = {}
decKey = 811589153

#Defining a double linked list
class doubleLinkedList():
    def __init__(self, value, refer, next = None, prior = None):
        self.value = value
        self.next = next
        self.prior = prior
        self.refer = refer

#Make the first node
head = eval(file20.readline())
headNode = doubleLinkedList(head * decKey, 1)
length = 1
directions[length] = headNode

#loop to make the rest
priorNode = headNode
for line in file20:
    newNode = doubleLinkedList(eval(line) * decKey, length, None, priorNode)
    if eval(line) == 0:
        zeroNode = newNode
    priorNode.next = newNode
    priorNode = newNode
    length += 1
    directions[length] = newNode

#Link it circularly
newNode.next = directions[1]
directions[1].prior = newNode

#Test list is working as intended
#testNode = headNode
#for i in range(20):
#    print(testNode.value)
#    testNode = testNode.prior


#start looping and shifting items 
nextDir = directions[1].next
for mixes in range(0, 10):
    for i in range(1, length + 1):
        nodeToMove = directions[i]
        #connect next of prior node to prior of next node. This "pops" out the node we want to move
        nodeToMove.prior.next = nodeToMove.next
        nodeToMove.next.prior = nodeToMove.prior

        #travel the distance % 5000, -1 since were taking an element out 
        tempPointer = nodeToMove.prior
        for distance in range(0, nodeToMove.value % (length - 1)): #We subtract by 1 since were looping through a linked list wihtout the node we want to move. 
            tempPointer = tempPointer.next
          
        #Pointer lands on a node. Insert new node between here and next node.
        nodeToMove.prior = tempPointer
        nodeToMove.next = tempPointer.next
        nodeToMove.next.prior = nodeToMove
        nodeToMove.prior.next = nodeToMove

arr = []
counting = False
count = -1
head = directions[1]
while len(arr) < 3:
    head = head.next
    if head.value == 0:
        counting = True 
    if counting:
        count += 1
        if count == 1000 or count == 2000 or count == 3000:
            arr.append(head.value)

print(arr)
print(sum(arr))










