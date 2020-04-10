# Task 1. Reading the dataset

import pandas as pd

apps_with_duplicates = pd.read_csv('apps.csv')

# Drop duplicates
apps = apps_with_duplicates.drop_duplicates()

print(apps.columns)

# Print the total number of apps
print('Total number of apps in the dataset = ', apps.App.count())

# # Have a look at a random sample of 5 rows
n = 5
apps.sample(n)

print('\nThis is end of section 1\n')

# Task 2. Data Cleaning

# List of characters to remove
chars_to_remove = ['+', ',', 'M', '$']

# List of column names to clean
cols_to_clean = ['Installs', 'Size', 'Price']

# Loop for each column
for col in cols_to_clean:
    # Replace each character with an empty string
    for char in chars_to_remove:
        apps[col] = apps[col].str.replace(char, '')
    # Convert col to numeric
    apps[col] = pd.to_numeric(apps[col], errors='ignore')

print('\nThis is end of section 2\n')

# 3. Exploring app categories

# Print the total number of unique categories
num_categories = len(apps['Category'].unique())
print('Number of categories = ', num_categories)

# Count the number of apps in each 'Category' and sort them in descending order
num_apps_in_category = apps['Category'].value_counts().sort_values(ascending=False)

print(num_apps_in_category)

print('\nThis is end of section 3\n')

# 4. Distribution of app ratings
print(apps.columns)

# Average rating of apps
avg_app_rating = apps['Rating'].mean()
print('Average app rating = ', avg_app_rating)

print('\nThis is end of section 4\n')

# 5. Size and price of an app

print('\nThis is end of section 5\n')

# 6. Relation between app category and app price
# Select a few popular app categories
popular_app_cats = apps[apps.Category.isin(['GAME', 'FAMILY', 'PHOTOGRAPHY',
                                            'MEDICAL', 'TOOLS', 'FINANCE',
                                            'LIFESTYLE','BUSINESS'])]

print(popular_app_cats.columns)
print(popular_app_cats.head(3))
#
# # Apps whose Price is greater than 200
# # apps_above_200 = popular_app_cats[['Category', 'App', 'Price']][popular_app_cats['Price'] > 200]
# # print(apps_above_200)
#
# # 7. Filter out "junk" apps
#
apps_under_100 = popular_app_cats[popular_app_cats['Price'] < 100]
print(apps_under_100)