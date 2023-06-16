class RandomTreeGenerator:

    import random
    import string

    list_of_base_children = []
    min_groups = 1
    max_groups = 5
    max_in_each_group = 4

    def generate_list_of_siblings(self, min_groups, max_groups, max_in_each_group):

        min_and_max_groups = [min_groups]
        
        for i in range(min_groups, max_groups):
            min_and_max_groups.append(i)

        number_of_groups = self.random.choice(min_and_max_groups)

        list_of_siblings = []
        for i in range(0, number_of_groups):
            list_of_siblings.append([])

        for group in list_of_siblings:

            all_members = []
            for i in range(2, max_in_each_group):
                all_members.append(i)

            for j in range(1, self.random.choice(all_members)):
                group.append(self.generate_random_string(4))
        
        return list_of_siblings

    def create_tree(self, level, list_of_siblings):

        if level == 1:

            list_of_parents = []

            for i in range(len(list_of_siblings)):
                list_of_parents.append(self.generate_random_string(4))

            for j in range(len(list_of_siblings)):
                """
                family = []
                family.append(list_of_parents[j])
                family.append(list_of_siblings[j])"""
                list_of_parents.insert(j+1, list_of_siblings[j])
            
            final_tree = ['root']

            for item in list_of_parents:
                final_tree.append(item)

            return final_tree

        elif level > 1:

            list_of_parents = self.generate_list_of_siblings(len(list_of_siblings), level, self.max_in_each_group)

            for i in range(len(list_of_siblings)):
                """
                family = []
                family.append(list_of_parents[i][0])
                family.append(list_of_siblings[i])
                list_of_parents[i][0] = family
                """
                #for item in list_of_siblings[i]:
                list_of_parents[i].append(list_of_siblings[i])
        
            return self.create_tree(level - 1, list_of_parents)

    def generate_random_string(self, length):
        # Get all the ASCII letters in lowercase and uppercase
        letters = self.string.ascii_letters + self.string.digits
        # Randomly choose characters from letters for the given length of the string
        random_string = ''.join(self.random.choice(letters) for i in range(length))
        return random_string
    
    def generate(self, max_levels):
        self.list_of_base_children = self.generate_list_of_siblings(self.min_groups, self.max_groups, self.max_in_each_group)
        levels = self.random.randint(2, max_levels)
        return self.create_tree(levels, self.list_of_base_children)

## using quicksort for normalizing the trees

    def normalize(self, nodes):

        # If the input array contains fewer than two elements,
        # then return it as the result of the function

        # if leaf
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
        # We're assuming they'll be random lists anyways
        # but of course not the root node

        pivot = nodes[1]

        # if it is a leaf, set children to zero
        if not isinstance(pivot, list):
            pivot_children = 0
        
        else:
            pivot_children = len(pivot) - 1
            pivot = self.normalize(pivot)

        for node in nodes:

            if node == nodes[0]:
                low.append(node)
                continue

            # Elements that are smaller than the `pivot` go to

            # the `low` list. Elements that are larger than

            # `pivot` go to the `high` list. Elements that are

            # equal to `pivot` go to the `same` list.

            node_children = 0

            # if the node is a list
            if isinstance(node, list):

                # access its number of children
                node_children = len(node) - 1

                # we need to sort that subtree as well
                node = self.normalize(node)

            if node_children < pivot_children:

                low.append(node)

            elif node_children == pivot_children:

                same.append(node)

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
        self.list_of_base_children = []


