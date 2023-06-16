class RandomTreeGenerator:

    import random
    import string

    list_of_base_children = []

    # these can be changed
    min_groups = 2
    max_groups = 7
    max_in_each_group = 5

    def generate_list_of_siblings(self, min_groups, max_groups, max_in_each_group):

        list_of_siblings = []

        # choose a number of groups to generate
        min_and_max_groups = [min_groups]
        
        for i in range(min_groups, max_groups):
            min_and_max_groups.append(i)

        number_of_groups = self.random.choice(min_and_max_groups)

        # append the above number of empty lists
        for i in range(0, number_of_groups):
            list_of_siblings.append([])

        # for each empty list in siblings
        for group in list_of_siblings:
            
            # this is just to choose a random number for upper bound
            upper_bound_choices = []
            for i in range(2, max_in_each_group):
                upper_bound_choices.append(i)

            # populate the sibling group with a random number of siblings
            for j in range(1, self.random.choice(upper_bound_choices)):

                group.append(self.generate_random_string(4))
        
        return list_of_siblings

    def create_tree(self, level, list_of_siblings):

        # if the last level
        if level <= 3:

            final_tree = ['root']

            for i in range(len(list_of_siblings)):
                final_tree.append(list_of_siblings[i])

            return final_tree
        
        # else (when not the last level)
        else:

            # generate a list of parents at least the length of the list of siblings
            list_of_parents = self.generate_list_of_siblings(len(list_of_siblings), self.max_groups, self.max_in_each_group)

            # append each sibling group to a parent
            for i in range(len(list_of_siblings)):

                list_of_parents[i].append(list_of_siblings[i])

            # recursive step on the next level
            return self.create_tree(level - 1, list_of_parents)

    def generate_random_string(self, length):

        # Get all the ASCII letters in lowercase and uppercase

        letters = self.string.ascii_letters + self.string.digits

        # Randomly choose characters from letters for the given length of the string

        random_string = ''.join(self.random.choice(letters) for i in range(length))

        return random_string
    
    def generate(self, max_levels):

        #handle three special cases

        if max_levels == 0:
            return None
        
        if max_levels == 1:

            return ['root']
        
        if max_levels == 2:

            final_tree = ['root']

            for i in range(0, self.random.randint(1,self.max_in_each_group)):

                final_tree.append(self.generate_random_string(4))
            
            return final_tree

        # otherwise

        # generate list of base children
        self.list_of_base_children = self.generate_list_of_siblings(self.min_groups, self.max_groups, self.max_in_each_group)

        # choose number levels to use within specified lange
        levels = self.random.randint(1, max_levels)

        # return a randomly generated tree
        return self.create_tree(levels - 1, self.list_of_base_children)

## using quicksort for normalizing the trees

    def normalize(self, nodes):

        # if leaf, return
        if len(nodes) == 1:

            return nodes
        
        # check if there is a list
        hasList = False

        for node in nodes:
            if isinstance(node, list):
                hasList = True 
        
        # if there is no list, then all children are leaves
        if hasList == False:

            return nodes
        
        # create three lists to store low, same, high

        low, same, high = [], [], []


        # Select pivot element as first child, for simplicity

        pivot = nodes[1]

        # if it is a leaf, set children to zero
        if not isinstance(pivot, list):
            pivot_children = 0
        
        # else, count and normalize its children
        else:
            pivot_children = len(pivot) - 1
            pivot = self.normalize(pivot)

        # now we compare every other node to the pivot

        for node in nodes:

            # skip the root node

            if node == nodes[0]:

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

        # initialize list of base children
        self.list_of_base_children = []


