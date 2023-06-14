from Node import Node
from Visualize import Visualize
import matplotlib.pyplot as plt
class Main:

    # Create nodes
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
    child6.add_child(child7)

    # Visualize the tree
    plt.figure(figsize=(6, 6))
    Visualize.visualizeTree(root)
    plt.axis('off')
    plt.show()