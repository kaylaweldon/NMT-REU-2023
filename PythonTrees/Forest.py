from typing import Any


class Forest:

    from RandomTreeGenerator import RandomTreeGenerator
    import random

    # 
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
    
    
    # TO DO
    def __get_forest__(self):
        return self.forest
    
    # TO DO 
    # I think sorting by number of nodes is better than level
    # since there won't be THAT much difference in levels
    # in the case of subcategories and such
    def sort_by_number_of_levels(self):
        return None
    
    # TEST THIS
    def number_of_nodes(self, tree):

        nodes = 0

        for node in list:
            if isinstance(node, list):
                nodes += self.number_of_nodes(node)
            else:
                nodes += 1
        
        return nodes

    # TO DO
    def number_of_levels(list):

        deepest_level = 0

        return None
    
    # TO DO
    def sort_by_number_of_nodes(self):
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
        self.trees = []

