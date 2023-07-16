import pandas as pd
import matplotlib.pyplot as plt
from Node import Node
from newListTree import Visualize

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
        if pd.notna(subcategory1) and [subcategory1] not in found_category:
            subcategory_entry = [subcategory1]
            if pd.notna(subcategory2):
                if pd.notna(subcategory3):
                    subcategory_entry.append([subcategory2, [subcategory3]])
                else:
                    subcategory_entry.append([subcategory2])
            found_category.append(subcategory_entry)

    else:
        # If the category is not already in the list, add it with subcategories
        category_entry = [category]
        if pd.notna(subcategory1):
            if pd.notna(subcategory2):
                if pd.notna(subcategory3):
                    category_entry.append([subcategory1, [subcategory2, [subcategory3]]])
                else:
                    category_entry.append([subcategory1, [subcategory2]])
            else:
                category_entry.append([subcategory1])
        categories.append(category_entry)
trees = []
for category_entry in categories:
    print(category_entry)
"""    trees.extend(category_entry)
    tree_visualizer = Visualize(trees)
    tree_visualizer.visualize_trees()"""

