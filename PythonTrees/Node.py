class Node:

    def __init__(self, data):
        self.data = data
        # a pair of square brackets denotes an empty list
        self.children = []

    def add_child(self, child):
        self.children.append(child)


