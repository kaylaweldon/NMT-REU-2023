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


def addNchildren(list):
    for i in range(1,random.randrange(1,4)):
        list.append([])
        list[i].append("child")

addNchildren(list_7[2][1])
print(list_7)



