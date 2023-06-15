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
rootNode = constructTree(mylist)

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

    RandomTreeGenerator = RandomTreeGenerator(4)

    random_tree = RandomTreeGenerator.create_tree(4, RandomTreeGenerator.list_of_base_children)
    random_tree_nodes = constructTree(random_tree)

    print(random_tree)

    plt.figure(figsize=(6, 6))
    visualization = Visualize.visualizeTree(random_tree_nodes)
    plt.axis('off')
    plt.show()


['root', [  
            [
            'LBYC', [
                [
                    'WFxt', [
                                [
                                    '6v2P', [
                                        [
                                            'eYsC', 
                                                ['7aKP', 'IXFe']
                                            ], 'QZ3U', 'Q1hb'
                                        ]
                                 
                                 ], 'XtmD', '4jhZ'
                             ]
                    ]
                ]
             ],
             ['SgBz', [['GSlH', [['y6wm', [['mxMH', ['Nuwp', 'yD5J']], '85re', 'tyAT']]]]]], ['ah1d', [['U8WP', [['VxX6', [['Dr6v', ['w4gL']], 'a6zP']]]], 'kZrn']], ['wW43', [['zVNH', [['GvDl', ['0BJt', 'bOyv']]]], 'aIq8']]
          ]]

