class RandomTreeGenerator:

    import random
    import string

    list_of_base_children = []

    def create_tree(self, max_levels, list_of_siblings):

        # if the last level
        if max_levels <= 2:

            return list_of_siblings
        
        for siblingIndex in range(0, len(list_of_siblings)):

            subtree_rooted_at_sibling = self.generate_actual(max_levels - 1, self.max_fan, list_of_siblings[siblingIndex])
            
            list_of_siblings[siblingIndex] = subtree_rooted_at_sibling

        return list_of_siblings

    def generate_list_of_siblings(self, max_fan):

        list_of_siblings = []
        
        number_of_siblings = self.random.randint(0, max_fan)

        # append the above number of empty lists
        for i in range(0, number_of_siblings):
            list_of_siblings.append([self.generate_random_string(1)])
        
        return list_of_siblings

    def generate_random_string(self, length):

        # Get all the ASCII letters in lowercase and uppercase

        letters = self.string.ascii_letters #+ self.string.digits

        # Randomly choose characters from letters for the given length of the string

        random_string = ''.join(self.random.choice(letters) for i in range(length))

        return random_string
    
    def generate_actual(self, max_levels, max_fan, root):

        self.max_fan = max_fan

        #handle three special cases
        
        if max_levels <= 1:

            return root
        
        if max_levels == 2:

            final_tree = [self.generate_random_string(1)]

            for i in range(0, self.random.randint(1,self.max_fan)):

                root.append([self.generate_random_string(1)])
            
            return root

        # otherwise

        # generate list of base children
        list_of_base_children = self.generate_list_of_siblings(self.max_fan)

        children_to_append = self.create_tree(max_levels - 1, list_of_base_children)

        for child in children_to_append:
            root.append(child)

        return root

    def generate(self, max_levels, max_fan):

        max_levels_to_be_passed = self.random.randint(0, max_levels)

        return self.generate_actual(max_levels_to_be_passed, max_fan, ['root'])

    def __init__(self):

        self.max_fan = 0

    def main(self):

        print(self.generate(10, 6, ['root']))

if __name__ == '__main__':
    RandomTreeGenerator().main()