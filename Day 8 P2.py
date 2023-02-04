with open('input8') as file8:
    forest = [[int(x) for x in line.strip()] for line in file8]

top, bottom = 0, len(forest) - 1
left, right = 0, len(forest[0]) - 1

#check each tree
highest_view = 1
for x in range(top+1, bottom):
    for y in range(left+1, right):
        tree = forest[x][y]
        view = 1

        #check up from tree
        counter = 0
        for treeup in range(x - 1, top - 1, -1):
            new_tree = forest[treeup][y]
            counter += 1
            if new_tree >= tree:
                break
            
        view *= counter
        
        #check down from tree
        counter = 0
        for treedown in range(x + 1, bottom + 1):
            new_tree = forest[treedown][y]
            counter += 1
            if new_tree >= tree:
                break
        view *= counter

        #check left from tree
        counter = 0
        for treeleft in range(y - 1, left - 1, -1):
            new_tree = forest[x][treeleft]
            counter += 1
            if new_tree >= tree:
                break
        view *= counter
        
        #check right from tree
        counter = 0
        for treeright in range(y + 1, right + 1):
            new_tree = forest[x][treeright]
            counter += 1
            if new_tree >= tree:
                break
        view *= counter

        if view > highest_view:
            highest_view = view
        
print(highest_view)