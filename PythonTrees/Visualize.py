from Node import Node
import matplotlib.pyplot as plt

class Visualize:

    def visualizeTree(node, ax=None, x=0, y=0, dx=1, dy=1):
        if ax is None:
            ax = plt.gca()

        ax.text(x, y, str(node.data), ha='center', va='center',
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle'))

        num_children = len(node.children)
        if num_children == 0:
            return

        x0 = x - dx * (num_children - 1) / 2
        y0 = y - 1.5 * dy

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