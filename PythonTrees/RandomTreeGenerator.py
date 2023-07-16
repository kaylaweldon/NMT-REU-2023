class RandomTreeGenerator:

    import random
    import string

    list_of_base_children = []

    def create_tree(self, max_levels, list_of_siblings):

        final_tree = [self.generate_random_string(1)]

        # if the last level
        if max_levels <= 2:

            for i in range(len(list_of_siblings)):

                final_tree.append(list_of_siblings[i])

            return final_tree
        
        for sibling in list_of_siblings:

            list_of_children = self.generate(self.random.randint(0,max_levels), self.max_fan)
            
            sibling.append(list_of_children)
        
            final_tree.append(sibling)

        return final_tree

    def generate_list_of_siblings(self, max_fan):

        list_of_siblings = []
        
        number_of_siblings = self.random.randint(0, max_fan + 1)

        # append the above number of empty lists
        for i in range(0, number_of_siblings):
            list_of_siblings.append([])

        # for each empty list in siblings
        for group in list_of_siblings:

            group.append(self.generate_random_string(1))
        
        return list_of_siblings

    def generate_random_string(self, length):

        # Get all the ASCII letters in lowercase and uppercase

        letters = self.string.ascii_letters #+ self.string.digits

        # Randomly choose characters from letters for the given length of the string

        random_string = ''.join(self.random.choice(letters) for i in range(length))

        return random_string
    
    def generate(self, max_levels, max_fan):

        self.max_fan = max_fan

        #handle three special cases

        #if max_levels == 0:
           # return 
        
        if max_levels <= 1:

            return [self.generate_random_string(1)]
        
        if max_levels == 2:

            final_tree = [self.generate_random_string(1)]

            for i in range(0, self.random.randint(1,self.max_fan)):

                final_tree.append([self.generate_random_string(1)])
            
            return final_tree

        # otherwise

        # generate list of base children
        self.list_of_base_children = self.generate_list_of_siblings(self.max_fan)


        # return a randomly generated tree
        return self.create_tree(max_levels - 1, self.list_of_base_children)

    def __init__(self):

        # initialize list of base children
        self.list_of_base_children = []
        self.max_fan = 0

    def main(self):

        print(self.generate(6, 3))

if __name__ == '__main__':
    RandomTreeGenerator().main()

