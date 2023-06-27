from typing import Any
from collections import deque


class Forest:

    from RandomTreeGenerator import RandomTreeGenerator
    import random

    # the list containing trees of the forest
    forest = []

    partitioned_forest = []


    def __get_forest__(self):
        return self.forest
    

    def generate_forest(self, number_of_trees, max_levels):

        # initialize a random tree generator
        RandomTreeGenerator = self.RandomTreeGenerator()

        # for each tree to generate
        for i in range(1, number_of_trees):

            # generate a tree of max levels 
            random_tree = RandomTreeGenerator.generate(max_levels)

            # add that tree to the forest
            self.forest.append(random_tree)
    
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
    def partition_forest(self, k):

        # sort the forest
        self.forest = self.sort_by_number_of_nodes(self.forest)

        # if k is too big there is nothing to be done
        if k >= len(self.forest) + 1:
            return

        # otherwise
        # calculate number of groups needed
        # in order to have k trees in each group

        number_of_groups = len(self.forest) // k

        # counter to keep track of where we are in the forest list
        index_in_forest = 0

        # for each group there is to do
        for i in range (1, number_of_groups):
            
            # create a group for the k or more trees
            group = []
            
            # append k trees to the group
            for tree in range(1, k):

                group.append(self.forest[index_in_forest])
    
                # increase counter
                index_in_forest += 1

            # to take care of the leftover trees
            
            # TO DO: double check these indices! They probably don't work!

            if (len(self.forest) - index_in_forest + 1) < k:

                # append all leftover trees to the last group

                while (index_in_forest != len(self.forest) - 1):

                    group.append(self.forest[index_in_forest])

                    index_in_forest += 1

            # add the group to the partitioned forest

            self.partitioned_forest.append(group)

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
    
    # achieve the canonical number of a tree

    def canonize_tree(self, tree):

        # if leaf, it is already sorted

        if len(tree) == 1:

            canonical_number = "10"

            return canonical_number
        
        # otherwise make an array to store
        # the canonical numbers of each child

        canonical_numbers_to_sort = []

        # and then canonize each child
        # while simulateously identifying the 
        # longest canonical number

        longest_number_length = 0

        for child in tree:

            # skip over the root name
            if child == tree[0]:
                continue
            
            # request canonical number, recursively
            child_canonical_number = self.canonize_tree(child)

            # append the canonical number to the array
            canonical_numbers_to_sort.append(child_canonical_number)

            # compare to longest_number
            if len(child_canonical_number) > longest_number_length:

                longest_number_length = len(child_canonical_number)

        # sort the numbers of children lexiographically
        # meaning high to low

        # first pad each with leading zeroes so all are the same length
        for number in canonical_numbers_to_sort:

            # use zfill to pad the beginning of the string with zeroes
            number = number.zfill(longest_number_length)
        
        # sort the canonical numbers
        canonical_numbers = self.sort_canonical_numbers(canonical_numbers_to_sort , 0, longest_number_length)

        # append them to be one big number, wrap with 1 and 0

        canonical_number = "1"

        for number in canonical_numbers:

            canonical_number += number
        
        canonical_number += "0"

        return canonical_number


    def sort_canonical_numbers(self, canonical_numbers_to_sort, index, max_length):

        # if there is nothing to sort
        if len(canonical_numbers_to_sort) < 2 or index > max_length - 1:

            # return the list
            return canonical_numbers_to_sort

        # otherwise put numbers into two bins based on their significant digit

        # for ones
        high = []

        # for zeroes
        low = []

        for number in canonical_numbers_to_sort:

            if number[index] == "1":

                high.append(number)
            
            else:

                low.append(number)
        
        # sort each bin according to the digit at the next index
        high = self.sort_canonical_numbers(high, index + 1, max_length)

        low = self.sort_canonical_numbers(low, index + 1, max_length)

        # let's now remove the leading zeroes for each number
        # because we won't need them anymore

        # for high
        for item in range(0, len(high)):

            index = 0

            while (high[item][index] != "1"):

                index += 1
            
            high[item] = high[item][index:]

        # and low
        for item in range(0, len(low)):

            index = 0

            while (low[item][index] != "1"):

                index += 1

            low[item] = low[item][index:]
        
        # append each item in low to the high bin

        for number in low:

            high.append(number)
        
        return high
    

    def is_subtree(self, tree1, tree2):

        # if the trees are isomorphic then return true
        if self.canonize_tree(tree1) == self.canonize_tree(tree2):
            return True

        # treat the smaller one as the potential subtree
        if self.number_of_nodes(tree1) > self.number_of_nodes(tree2):

            subTree = tree2
            mainTree = tree1

        else:
            subTree = tree1
            mainTree = tree2

        # TO DO BEFORE, very IMPORTANT: NORMALIZE THE ACTUAL TREES
        # USING CANONICAL NUMBERS SCHEME!

        return self.test_subtree(subTree, mainTree)

    
    def test_subtree(self, subTree, mainTree):

        # if the trees are isomorphic return true
        if self.canonize_tree(subTree) == self.canonize_tree(mainTree):
            return True
        
        # if there are sufficiently little nodes, it is already true
        if self.number_of_nodes(subTree) <= 2:
            return True
        
        # create a matrix for keeping track of successful pathways
        successMatrix = []

        # for each subChild from biggest to smallest node size
        for subChild in subTree:

            successMatrix.append(subChild)

            # create a queue for possibilities to check
            possibilitiesQueue = deque()

            # for each mainChild from biggest to smallest node size
            for mainChild in mainTree:

                # if a subtree is remotely possible,
                # i.e. if mainChild is of sufficient degree
                # TO DO: and of sufficient total levels (finish level counter method above)
                if len(mainChild) >= len(subChild) \
                and self.number_of_nodes(mainChild) >= self.number_of_nodes(subChild):

                    # add the mainChild to the possibilities queue (deque, really)
                    # we are adding in this way to they are ordered such that the
                    # possibilities with the greatest number of nodes are at the front
                    # (right) of the queue
                    possibilitiesQueue.appendleft(mainChild)
            
            # if the queue is empty then there were no possible routes
            # so we return false
            if not possibilitiesQueue.bool():
                return False
            
            # while there are still items in the queue
            while possibilitiesQueue.bool():

                # grab the largest child from the queue
                possibility = possibilitiesQueue.pop()

                # recursive step, check if it is indeed a successful route
                if self.test_subtree(subChild, possibility):

                    successMatrix[len(successMatrix) - 1].append(possibility)
            
        if self.test_success_matrix(successMatrix):
            return True
    
    # TO DO: write method to test if a successful combination exists
    # within a success matrix
    def test_success_matrix(successMatrix):
        return False


    # our first attempt at normalization, not good don't use
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


    def main(self):

        practice_list = ['root', ['xvae', 'L7h1'], ['N2Di', '7iCo'], ['5g5d', 'elPP', '5Q0K']]

        # testing canonical number sorter

        canonical_numbers_to_sort = ["10","110100"]

        longest_number_length = 6

        # first pad each with leading zeroes so all are the same length

        for i in range(0, len(canonical_numbers_to_sort)):
            
            number = canonical_numbers_to_sort[i]
            # use zfill to pad the beginning of the string with zeroes
            canonical_numbers_to_sort[i] = number.zfill(longest_number_length)
        
        canonical_numbers = self.sort_canonical_numbers(canonical_numbers_to_sort , 0, longest_number_length)

        print(canonical_numbers)

        print("hello world")

        # testing canonical number generator

        tree1 = ["hello"]
        tree2 = ["hello", ["world"]]
        tree3 = ["hello", ["world"], ["we're"], ["back"]]
        tree4 = ["hello", ["world"], ["did", ["you"], ["miss", ["me"]]]]

        print(self.canonize_tree(tree1))
        print(self.canonize_tree(tree2))
        print(self.canonize_tree(tree3))
        print(self.canonize_tree(tree4))







if __name__ == '__main__':
    Forest().main()