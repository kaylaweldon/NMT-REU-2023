class RandomTreeGenerator:

    import random
    import string

    list_of_base_children = []

    def generate_list_of_siblings(self, min_groups, max_groups, max_in_each_group):

        number_of_groups = self.random.randrange(min_groups, max_groups)

        list_of_siblings = []
        for i in range(0, number_of_groups):
            list_of_siblings.append([])

        for group in list_of_siblings:
            for i in range(1, self.random.randrange(2, max_in_each_group)):
                group.append(self.generate_random_string(4))
        
        return list_of_siblings

    def create_tree(self, level, list_of_siblings):

        if level == 1:

            list_of_parents = []

            for i in range(len(list_of_siblings)):
                list_of_parents.append(self.generate_random_string(4))

            for j in range(len(list_of_siblings)):
                family = []
                family.append(list_of_parents[j])
                family.append(list_of_siblings[j])
                list_of_parents[j] = family
            
            final_tree = ['root']
            final_tree.append(list_of_parents)
            return final_tree

        elif level > 1:

            list_of_parents = self.generate_list_of_siblings(len(list_of_siblings), 5, 5)

            for i in range(len(list_of_siblings)):
                family = []
                family.append(list_of_parents[i][0])
                family.append(list_of_siblings[i])
                list_of_parents[i][0] = family
        
            return self.create_tree(level - 1, list_of_parents)

    def generate_random_string(self, length):
        # Get all the ASCII letters in lowercase and uppercase
        letters = self.string.ascii_letters + self.string.digits
        # Randomly choose characters from letters for the given length of the string
        random_string = ''.join(self.random.choice(letters) for i in range(length))
        return random_string
    
    def __init__(self, level):
        self.list_of_base_children = self.generate_list_of_siblings(3, level, 5)