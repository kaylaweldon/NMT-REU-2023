from Node import Node
from Visualize import Visualize
from RandomTreeGenerator import RandomTreeGenerator

import matplotlib.pyplot as plt

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

mylist = ['A', ['B', 'E', 'F', ['H', 'I']], 'C', 'D']
mylist2 = ['active life', ['swimming pools', 'NMT Swimming Pool ', 'Sedillo Park Swimming Pool'], ['fitness & instructions',  ['gyms', 'NMT Gym']],  ['golf', 'NMT Golf Course']]
rootNode = constructTree(mylist2)

class Main:

    # Visualize the tree
    plt.figure(figsize=(6, 6))
    visualization = Visualize.visualizeTree(rootNode)
    plt.axis('off')
    plt.show()

    """ # Create nodes
    root = Node(1)
    child1 = Node(2)
    child2 = Node(3)
    child3 = Node(4)
    child4 = Node(5)
    child5 = Node(6)
    child6 = Node(7)
    child7 = Node(8)

    # Link nodes together
    root.add_child(child1)
    root.add_child(child2)
    root.add_child(child3)
    root.add_child(child4)
    child1.add_child(child5)
    child1.add_child(child6)
    child6.add_child(child7)"""

    ### TESTS OF RANDOM TREES

    # create new random tree generator
    RandomTreeGenerator = RandomTreeGenerator()

    # generate random tree of max specified levels
    random_tree = RandomTreeGenerator.generate(2)
    random_tree_nodes = constructTree(random_tree)

    print(random_tree)

    plt.figure(figsize=(6, 6))
    visualization = Visualize.visualizeTree(random_tree_nodes)
    plt.axis('off')
    plt.show()

    random_tree_normalized = RandomTreeGenerator.normalize(random_tree)
    random_tree_nodes = constructTree(random_tree_normalized)

    plt.figure(figsize=(6, 6))
    visualization = Visualize.visualizeTree(random_tree_nodes)
    plt.axis('off')
    plt.show()

    print(random_tree_normalized)

