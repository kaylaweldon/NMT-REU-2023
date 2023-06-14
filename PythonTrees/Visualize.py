from Node import Node
import matplotlib.pyplot as plt

class Visualize:

    """ parameters: 
        node: the node being processed
        ax: axis to draw on
        x, y: the coordinates of the current node
        dx, dy: the spacing between the nodes
    """
    def visualizeTree(node, ax=None, x=0, y=0, dx=1, dy=1):
        # creates a new axis 
        if ax is None:
            ax = plt.gca()

        #draws the node on ax placing the node at (x, y)
        ax.text(x, y, str(node.data), ha='center', va='center',
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle'))

        #checks if current node has children
        num_children = len(node.children)
        if num_children == 0:
            return


        x0 = x - dx * (num_children - 1) / 2
        y0 = y - 1.5 * dy

        #iterates over each child of the current node.
        # for every child, calculates where  it will be plotted
        for i, child in enumerate(node.children):
            x1 = x0 + i * dx
            y1 = y0 - dy
            ax.plot([x, x1], [y, y1], '-k')
            Visualize.visualizeTree(child,ax, x1, y1, dx, dy)
 
    #depth first search traversal
    def DFS(node, depth = 0):
        print(' ' * depth + node.data)

        for child in node.children:
            child.DFS(depth + 1)