from Node import Node
from Visualize import Visualize
from ete3 import Tree

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

#t = Tree('A', ('B', 'E', 'F', ('H', 'I')), 'C', 'D')
t = Tree( "((a,b),c);" )

t.render("tree.png", w=183, units="mm")

