"""
this is just to practice different ways of creating lists
"""
import string
import random

# Method 1
# create two seperate lists
list_1 = ["a","b","c"]
list_2 = ["cde"]

# create empty list
list_3 = []

# append each to empty list
list_3.append(list_1)
list_3.append(list_2)

print(list_3)


# Method 2
# using list initizaliation
list_4 = [list_1,list_2]

print(list_4)

# Method 3
# using for loops
# I think we can use this for creating random lists

list_5 = []

for i in range(2):
    list_5.append([])
    for j in range(3):
        list_5[i].append(j)

print(list_5)

# let's try to make a list of lists of lists
list_6 = []
list_6.append('root')

for i in range(1,3):
    # two children
    list_6.append([])

    for j in range(2):
        #two children
        list_6[i].append([])
        list_6[i][j].append(j)

print(list_6)

# this is seeming like it will be easier to do from the bottom up
# can we do this recursively?

list_7 = []
list_7.append('root')

# it is important to make the range from (1,3) so 
# it does not try to append to the string of the name of the node
for i in range(1,3):
    # two children
    list_7.append([])
    list_7[i].append("child %d" % i) # apparently this is how you can format a string

    #for ease of writing, call child list_7
    child = list_7[i]

    for j in range(1,3):
        #two grandchildren
        child.append([])
        grandchild = child[j]
        grandchild.append(j)

print(list_7)

# function to add three children to any list
def add3children(list):
    for i in range(1,3):
        list.append([])
        list[i].append("great-grand-child %d" % i)

add3children(list_7[1][1])
print(list_7)


def addrandomchildren(list):
    for i in range(1,random.randrange(1,4)):
        list.append([])
        list[i].append("child")

addrandomchildren(list_7[2][1])
print(list_7)

#let's try adding an element of random names for things

#size of string
N = 3

# using random.choices()
# generating random strings
res = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=N))

print("The generated random string : " + str(res))

# lets just make a function for this

def generate_random_string(length):
    # Get all the ASCII letters in lowercase and uppercase
    letters = string.ascii_letters + string.digits
    # Randomly choose characters from letters for the given length of the string
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

# now lets add this as an element of our add random number of children function
"""
def addrandomchildren_withnames(list):
        list.append([])
        if len(list) > 1:
            for i in range(1,random.randrange(1, 4)):
                list[len(list) - 1].append(generate_random_string(4))

# let's make a new list cause this is getting messy with list_7 :/

list_8 = ['root']

addrandomchildren_withnames(list_8)

print(list_8)

for i in range(1,len(list_8)):
    addrandomchildren_withnames(list_8[i])

print(list_8)

# okay, this is looking good, but we're only doing 2 or 3 levels here.
# we need to have an arbitrary amount of levels

final_list = []
final_list.append('root')

mid_list = []
mid_list.append(generate_random_string(4))

# for a random amount of levels, let's say between 1 and 5
# this doesn't exactly work how i want it to. we need something recursive,
# but with a limit
for i in range(1, random.randrange(1,5)):
    level_list = []
    level_list.append(generate_random_string(4))
    level_list.append([])
    addrandomchildren_withnames(level_list[1])
    mid_list.append(level_list)

final_list.append(mid_list)
print(final_list)

# testing a recursive random list generator function

list = []
list.append('root')
increment = 0
max = 20

def recursive_random(list, increment):
    list.append([])
    list[1].append(generate_random_string(4))
    addrandomchildren_withnames(list[1])
    increment += 1
    if increment < max:
        if len(list[1]) > 2:
            for i in range(1, random.randrange(2, len(list[1]))):
                recursive_random(list[1], increment)
    else:
        return list

recursive_random(list, increment)
print(list)

# maybe generate a list of siblings at the bottom node

def generate_list_of_siblings(min_groups, max_groups, max_in_each_group):

    number_of_groups = random.randrange(min_groups, max_groups)

    list_of_siblings = []
    for i in range(0, number_of_groups):
        list_of_siblings.append([])

    for group in list_of_siblings:
        for i in range(1, random.randrange(2, max_in_each_group)):
            group.append(generate_random_string(4))
    
    return list_of_siblings

list_of_siblings = generate_list_of_siblings(1,5,5)
print(list_of_siblings)

list_of_parents = generate_list_of_siblings(len(list_of_siblings), 5, 5)
print(list_of_parents)

family = []
family.append(list_of_parents[1][0][0])
family.append(list_of_siblings[0])

list_of_parents[1][0] = family

print(list_of_parents)




def create_tree(level, list_of_siblings):

    if level == 1:

        list_of_parents = []

        for i in range(len(list_of_siblings), 5):
            list_of_parents.append(generate_random_string(4))

        for j in range(len(list_of_siblings)):
            family = []
            family.append(list_of_parents[j])
            family.append(list_of_siblings[j])
            list_of_parents[j] = family
        
        final_tree = ['root']
        final_tree.append(list_of_parents)
        return final_tree

    if level > 2:

        list_of_parents = generate_list_of_siblings(len(list_of_siblings), 5, 5)

        for i in range(len(list_of_siblings)):
            family = []
            family.append(list_of_parents[i][0])
            family.append(list_of_siblings[i])
            list_of_parents[i][0] = family
    
        create_tree(level - 1, list_of_parents)



final_tree = create_tree(5, list_of_parents)

print(final_tree)
"""

from random import randint

## QUICKSORT for normalizing the trees

def quicksort(nodes):

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
        pivot = quicksort(pivot)

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
            node = quicksort(node)

        if node_children < pivot_children:

            low.append(node)

        elif node_children == pivot_children:

            same.append(node)

        elif node_children > pivot_children:

            high.append(node)


    # The final result combines the sorted `low` list

    # with the `same` list and the sorted `high` list

    low = quicksort(low)
    high = quicksort(high)

    if len(same) > 0:
        for same_item in same:
            low.append(same_item)
    if len(high) > 0:
        for high_item in high:
            low.append(high_item)

    return low 

# cool let's try this out!

mylist = ['A', ['B', 'E', 'F', ['H', 'I']], 'C', 'D']

mylist2 = ['A', ['B', 'E', 'F', ['H', ['I', 'K'], 'G']], 'C', ['D', 'J']]

mylist3 = ['A', ['L', ['M', ['N', 'O'], 'P'], 'Q'], ['B', 'E', 'F', ['H', ['I', 'K'], 'G']], 'C', ['D', 'J']]

sorted = quicksort(mylist)

sorted2 = quicksort(mylist2)

sorted3 = quicksort(mylist3)


print(sorted)
print(sorted2)
print(sorted3)