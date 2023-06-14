from Node import Node
def constructTree(lst):
    if not lst: 
        return None

    rootVal = lst[0]
    root = Node(rootVal)

    for item in lst[1:]:
       # checks if item in list is a list
        if isinstance(item, list):
            child = constructTree(item)
            root.add_child(child)
        else:
            child = Node(item)
            root.add_child(child)
            
    return root

mylist = ["A", "B", ["C", "D"], "E"]
rootNode = constructTree(mylist)

