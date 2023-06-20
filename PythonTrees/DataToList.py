import pandas as pd
import matplotlib.pyplot as plt
from Node import Node
from Visualize import Visualize

df = pd.read_excel('SocorroPOI.xlsx')

categories = []

for _, row in df.iterrows():
    category = row['category']
    subcategory1 = row['subcategory1']
    subcategory2 = row['subcategory2']
    subcategory3 = row['subcategory3']

    # Check if the category is already in the list
    found_category = None
    for entry in categories:
        if entry[0] == category:
            found_category = entry
            break

    # If the category is already in the list, check if the subcategory is not already present
    if found_category:
        # If not null and not already listed, add it to the found_category list
        if pd.notna(subcategory1) and subcategory1 not in found_category:
            if pd.notna(subcategory2):
                if pd.notna(subcategory3):
                    found_category.append([subcategory1, [subcategory2, subcategory3]])
                else:
                    found_category.append([subcategory1, [subcategory2]])
            else:
                found_category.append(subcategory1)

    else:
        # If the category is not already in the list, add it with subcategories
        category_entry = [category]
        if pd.notna(subcategory1):
            if pd.notna(subcategory2):
                if pd.notna(subcategory3):
                    category_entry.append([subcategory1, [subcategory2, subcategory3]])
                else:
                    category_entry.append([subcategory1, [subcategory2]])
            else:
                category_entry.append(subcategory1)
        categories.append(category_entry)
print(categories)


def constructTree(lst):
    if not lst: 
        return None

    rootVal = lst[0]
    root = Node(rootVal)

    for item in lst[1:]:
       # checks if item in list is a list
        if isinstance(item, list):
            child = constructTree(item)
            root.add_child(child)
        else:
            child = Node(item)
            root.add_child(child)
            
    return root


for category_entry in categories:
    print(category_entry)
    rootNode = constructTree(category_entry)
     # Visualize the tree
    plt.figure(figsize=(6, 6))
    visualization = Visualize.visualizeTree(rootNode)
    plt.axis('off')
    plt.show()




