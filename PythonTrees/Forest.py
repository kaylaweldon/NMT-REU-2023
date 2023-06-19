from typing import Any


class Forest:

    from RandomTreeGenerator import RandomTreeGenerator
    import random

    # the list containing trees of the forest
    forest = []

    def generate_forest(self, number_of_trees, max_levels):

        # initialize a random tree generator
        RandomTreeGenerator = self.RandomTreeGenerator()

        # for each tree to generate
        for i in range(1, number_of_trees):

            # generate a tree of max levels 
            random_tree = RandomTreeGenerator.generate(max_levels)

            # add that tree to the forest
            self.forest.append(random_tree)
    
    
    def __get_forest__(self):
        return self.forest
    
    # I think sorting by number of nodes is better than level
    # since there won't be THAT much difference in levels
    # in the case of subcategories and such
    # Let's do a quicksort with this, it sorts from low to high number of nodes

    # TO DO: test this
    def sort_by_number_of_nodes(self, forest):

        if len(forest) == 1:
            return forest

        # choose first tree as pivot
        pivot = forest[0]
        number_of_nodes_in_pivot = self.number_of_nodes(pivot)

        # create three arrays
        low, same, high = [], [], []

        # sort each tree into low, high, or same,
        # depending on if it has more or less nodes than
        # the pivot element

        for tree in forest:

            number_of_nodes_in_tree = self.number_of_nodes(tree)

            if tree == pivot:
                continue

            if number_of_nodes_in_tree < number_of_nodes_in_pivot:

                low.append(tree)
            
            if number_of_nodes_in_tree > number_of_nodes_in_pivot:

                high.append(tree)
            
            else:
                same.append(tree)
        
        # sort the high and low arrays, 'same' does not need sorting

        low = self.sort_by_number_of_nodes(low)

        high = self.sort_by_number_of_nodes(high)

        # append the three sorted arrays together

        sorted_forest = low
            
        if len(same) > 0:

            for same_item in same:

                sorted_forest.append(same_item)

        if len(high) > 0:

            for high_item in high:

                sorted_forest.append(high_item)


        return sorted_forest
    
    # TO DO: test this
    def number_of_nodes(self, tree):

        # initialize nodes
        nodes = 0

        # for each node in the tree
        for node in list:

            # if the node is a subtree
            if isinstance(node, list):

                # count the nodes in that subtree, add to node count
                nodes += self.number_of_nodes(node)
            
            # otherwise is is a regular node to count
            else:
                nodes += 1
        
        # return ttotal number of nodes
        return nodes

    # TO DO: write this
    def number_of_levels(list):

        deepest_level = 0

        return None
    

    def normalize_forest(self):
        
        #normalize each tree
        for tree in self.forest:

            self.normalize_tree(tree)
            
        return None
    
    def normalize_tree(self, tree):
    
        # if leaf, return
        if len(tree) == 1:

            return tree
        
        # check if there is a list
        hasList = False

        for node in tree:
            if isinstance(node, list):
                hasList = True 
        
        # if there is no list, then all children are leaves
        if hasList == False:

            return tree
        
        # create three lists to store low, same, high

        low, same, high = [], [], []


        # Select pivot element as first child, for simplicity

        pivot = tree[1]

        # if it is a leaf, set children to zero
        if not isinstance(pivot, list):
            pivot_children = 0
        
        # else, count and normalize its children
        else:
            pivot_children = len(pivot) - 1
            pivot = self.normalize(pivot)

        # now we compare every other node to the pivot

        for node in tree:

            # skip the root node

            if node == tree[0]:

                low.append(node)

                continue

            # Elements that are smaller than the `pivot` go to

            # the `low` list. Elements that are larger than

            # `pivot` go to the `high` list. Elements that are

            # equal to `pivot` go to the `same` list.


            # set default children to zero
            node_children = 0

            # if the node is a list
            if isinstance(node, list):

                # access its number of children
                node_children = len(node) - 1

                # and normalize it
                node = self.normalize(node)

            # if it has less children than the pivot
            if node_children < pivot_children:

                low.append(node)

            # if equal
            elif node_children == pivot_children:

                same.append(node)

            # if greater
            elif node_children > pivot_children:

                high.append(node)


        # The final result combines the sorted `low` list

        # with the `same` list and the sorted `high` list

        low = self.normalize(low)

        high = self.normalize(high)

        if len(same) > 0:
            for same_item in same:
                low.append(same_item)
        if len(high) > 0:
            for high_item in high:
                low.append(high_item)

        return low 


    def __init__(self):
        self.forest = []

