class Node:

    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    #depth first search traversal
    def DFS(node, depth = 0):
        print(' ' * depth + node.data)

        for child in node.children:
            child.DFS(depth + 1)

