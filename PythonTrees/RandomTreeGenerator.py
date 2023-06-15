import random
import string

def generate_list_of_siblings(min_groups, max_groups, max_in_each_group):

    number_of_groups = random.randrange(min_groups, max_groups)

    list_of_siblings = []
    for i in range(0, number_of_groups):
        list_of_siblings.append([])

    for group in list_of_siblings:
        for i in range(1, random.randrange(2, max_in_each_group)):
            group.append(generate_random_string(4))
    
    return list_of_siblings

def create_tree(level, list_of_siblings):

    if level == 1:

        list_of_parents = []

        for i in range(len(list_of_siblings)):
            list_of_parents.append(generate_random_string(4))

        for j in range(len(list_of_siblings)):
            family = []
            family.append(list_of_parents[j])
            family.append(list_of_siblings[j])
            list_of_parents[j] = family
        
        final_tree = ['root']
        final_tree.append(list_of_parents)
        return final_tree

    elif level > 1:

        list_of_parents = generate_list_of_siblings(len(list_of_siblings), 5, 5)

        for i in range(len(list_of_siblings)):
            family = []
            family.append(list_of_parents[i][0])
            family.append(list_of_siblings[i])
            list_of_parents[i][0] = family
    
        return create_tree(level - 1, list_of_parents)

def generate_random_string(length):
    # Get all the ASCII letters in lowercase and uppercase
    letters = string.ascii_letters + string.digits
    # Randomly choose characters from letters for the given length of the string
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

list_of_base_children = generate_list_of_siblings(3, 5, 5)

final_tree = create_tree(5, list_of_base_children)

print(final_tree)