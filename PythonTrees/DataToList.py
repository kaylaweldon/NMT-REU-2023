import pandas as pd

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
        if pd.notna(subcategory1) and subcategory1 not in found_category[1]:
            found_category[1].append(subcategory1)
        if pd.notna(subcategory2) and subcategory2 not in found_category[1]:
            found_category[1].append([subcategory2])
        if pd.notna(subcategory3) and subcategory3 not in found_category[1]:
            found_category[1].append([subcategory3])
    else:
        # If the category is not already in the list, add it with subcategories
        category_entry = [category, []]
        if pd.notna(subcategory1):
            category_entry[1].append(subcategory1)
        if pd.notna(subcategory2):
            category_entry[1].append([subcategory2])
        if pd.notna(subcategory3):
            category_entry[1].append([subcategory3])
        categories.append(category_entry)

for category_entry in categories:
    print(category_entry)



