from Node import Node
class Main:

    # Create nodes
    root = Node('A')
    child1 = Node('B')
    child2 = Node('C')
    child3 = Node('D')
    child4 = Node('E')
    child5 = Node('F')
    child6 = Node('G')


    # Link nodes
    root.add_child(child1)
    root.add_child(child2)
    root.add_child(child3)
    root.add_child(child4)

    child1.add_child(child5)
    child2.add_child(child6)

    Node.DFS(root)
