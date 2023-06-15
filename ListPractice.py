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

def addrandomchildren_withnames(list):
    if len(list) > 1 :
        for i in range(1,random.randrange(1, len(list))):
            list.append([])
            list[i].append(generate_random_string(4))

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
        if len(list[1]) > 1:
            for i in range(1, random.randrange(2, len(list[1]))):
                recursive_random(list, increment)
    else:
        return list

recursive_random(list, increment)
print(list)
