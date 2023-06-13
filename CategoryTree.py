import pandas as pd
from anytree import Node, RenderTree

# read from excel file
df = pd.read_excel('SocorroPOI.xlsx')

# create dictionary to store trees
trees = {}

# iterate over rows of the file
for _, row in df.iterrows():
    # extract POI info
    category = row['category']
    subcategories = [row[subcat] for subcat in ['subcategory1', 'subcategory2', 'subcategory3'] if pd.notnull(row[subcat])]
    name = row['name']
    lat = row['latitude']
    lon = row['longitude']

    # create or retrieve tree
    if category not in trees:
        tree = Node(category)
        trees[category] = tree
    else:
        tree = trees[category]

    # create the subcategory nodes and link them in the tree
    parent_node = tree
    for subcategory in subcategories:
        existing_node = next((node for node in parent_node.children if node.name == subcategory), None)
        if existing_node:
            subcategory_node = existing_node
        else:
            subcategory_node = Node(subcategory, parent=parent_node)
        parent_node = subcategory_node

    # create POI node under the last category / subcategory node
    poi_node = Node(f"{name} ({lat}, {lon})", parent=parent_node)

# Save the category trees to a text file
with open('trees.txt', 'w', encoding= 'utf-8') as file:
    for category, root_node in trees.items():
        file.write(f"Category: {category}\n")
        for pre, _, node in RenderTree(root_node):
            file.write(f"{pre}{node.name}\n")
        file.write('\n')

print("Category trees have been saved to 'trees.txt'")
