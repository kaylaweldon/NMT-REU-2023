from Node import Node
from Visualize import Visualize
from RandomTreeGenerator import RandomTreeGenerator
from Forest import Forest

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
rootNode = constructTree(mylist)

class Main:

    # Visualize the tree
    plt.figure(figsize=(6, 6))
    visualization = Visualize.visualizeTree(rootNode)
    plt.axis('off')
    plt.show()

    ### TESTS OF RANDOM TREES

    # create new random tree generator
    RandomTreeGenerator = RandomTreeGenerator()

    # generate random tree of max specified levels
    random_tree = RandomTreeGenerator.generate(4)
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


    ### TESTS OF FOREST GENERATION

    nice_forest = Forest()

    # generate forest of 5 trees each of max 6 levels
    nice_forest.generate_forest(4, 6)

    list_of_trees = nice_forest.__get_forest__()

    print(list_of_trees)


