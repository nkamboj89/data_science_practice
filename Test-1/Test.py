# # Define count_entries()
# import pandas as pd
#
# #
# # tweets_df = pd.read_csv('tweets.csv')
# #
# # def count_entries(tweets_df, col_name='lang'):
# #     """Return a dictionary with counts of
# #     occurrences as value for each key."""
# #
# #     # Initialize an empty dictionary: cols_count
# #     cols_count = {}
# #
# #     # Extract column from DataFrame: col
# #     col = tweets_df[col_name]
# #
# #     # Iterate over the column in DataFrame
# #     for entry in col:
# #
# #         # If entry is in cols_count, add 1
# #         if entry in cols_count.keys():
# #             cols_count[entry] = cols_count[entry] + 1
# #
# #         # Else add the entry to cols_count, set the value to 1
# #         else:
# #             cols_count[entry] = 1
# #
# #     # Return the cols_count dictionary
# #     return cols_count
# #
# #
# # # Call count_entries(): result1
# # result1 = count_entries(tweets_df)
# #
# # # Call count_entries(): result2
# # result2 = count_entries(tweets_df, col_name='source')
# #
# # # Print result1 and result2
# # print(result1)
# # print(result2)
# #
# #
# #
# # # 04/08
# # # def sqrt(x):
# # #     try:
# # #         return x ** (0.5)
# # #     except TypeError:
# # #         print('pass int or float number')
# # #
# # # def sqrt_1(x):
# # #     if x < 0:
# # #         raise ValueError('X must be positive number')
# # #     try:
# # #         return x ** (0.5)
# # #     except TypeError:
# # #         print('pass int or float number')
# # #
# # # print(sqrt_1(-1))
# #
# # test_df = pd.DataFrame({
# #     'fruits' : ['Mango', 'Orange', 'Banana', 'Mango', 'Apple', 'Mango'],
# #     'Vegetables' : ['Onion', 'xxx', 'xxx', 'xxx', 'xxx', 'xxx']
# # })
# #
# # blank_list = []
# # for word in test_df['fruits']:
# #     if word[0:2] == 'Ma':
# #         blank_list.append(word)
# # print('\nFor Function\n')
# # print(blank_list)
# #
# # result4 = filter(lambda word: word[0:2] == 'Ma', test_df['fruits'])
# # test_result = list(result4)
# # print('\nLambda Function\n')
# # print(test_result)
# #
# #
# # print(tweets_df.columns.values)
# #
# # test_result = lambda x: x[0:2] == 'RT', tweets_df['text']
# # test_list = list(test_result)
# #
# # for tweet in test_list:
# #     print(tweet)
# #
# #
# # # tweet_list = []
# # # for tweet in tweets_df['text']:
# # #     if tweet[0:2] == 'RT':
# # #         tweet_list.append(tweet)
# # #     else:
# # #         return 1
# #
# # # print(tweet_list)
# # #
# # # print(tweets_df['text'][0:2])
# # # print(test_df['fruits'][0:2])
# #
# #
# #
# # def count_entries(x, col_name='lang'):
# #     """Return a dictionary with counts of
# #         occurrences as value for each key."""
# #     #Adding ValueError with raise
# #     if col_name not in x.columns:
# #         raise ValueError ('The DF does not have col :' + col_name)
# #     # Initialize an empty dictionary: cols_count
# #     cols_count = {}
# #
# #     #Add try block
# #     try:
# #         # Extract column from DataFrame: col
# #         col = x[col_name]
# #
# #         # Iterate over the column in dataframe
# #         for entry in col:
# #
# #             # If entry is in cols_count, add 1
# #             if entry in cols_count.keys():
# #                 cols_count[entry] += 1
# #
# #             # Else add the entry to cols_count, set the value to 1
# #             else:
# #                 cols_count[entry] = 1
# #         # Return the cols_count dictionary
# #         return cols_count
# #
# #     #Add except block
# #     except:
# #         print('The DataFrame does not have a ' + col_name + ' column.')
# #
# # # Call count_entries(): result1
# # result1 = count_entries(tweets_df, 'lang')
# #
# # # Print result1
# # print(result1)
#
#
# testdf = pd.DataFrame({
#     'fruits': ['Mango', 'Orange', 'Banana', 'Mango', 'Apple', 'Mango'],
#     'vegetables': ['Onion', 'xxx', 'xxx', 'xxx', 'xxx', 'xxx'],
#     'price': ['1', '2', '3', '4', '5', '6']})
#
# print(testdf)
#
# testdf["price"] = pd.to_numeric(testdf["price"])
#
# testdf['fruits'] = testdf['fruits'].str.replace('a', 'A')
#
# print(testdf)
#
# testdf['fruits'] = testdf['fruits'].str.upper()
#
# print(testdf)
#
# unique_cat = print(testdf['fruits'].unique())
#
# num_uniq_cat = print(len(testdf['fruits'].unique()))
#
# # Count the number of apps in each 'Category' and sort them in descending order
# num_of_fruits_in_cat = testdf['fruits'].value_counts().sort_values(ascending=False)
# print(num_of_fruits_in_cat)
#
# df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar'],
#                    'B': [1, 2, 3, 4, 5, 6],
#                    'C': [2.0, 5., 8., 1., 2., 9.]})
# print(df)
#
# grouped = df.groupby('A').filter(lambda x: len(x) > 2).reset_index()
#
# print(grouped)
#
# # import matplotlib.pyplot as plt
# # import random
# # x = [random.randrange(1, 10, 1) for i in range(10)]
# # y = random.sample(range(1, 11, 1), 10)
# # print(x, y)
# #
# # plt.plot(x, y)
# # plt.show()
#
# from functools import reduce
#
# product = [1, 2, 5, 10]
# result = reduce(lambda x, y: x * y, product)
# print('Result:')
# print(result)
#
# add_sq = (lambda x, y: x ** 2 + y ** 2)
# print('add_sq:')
# print(add_sq(5, 4))
#
# x = ['uer', 'gee', 'se', 'aeee']
# n_v = map(lambda w: w.count('e'), x)
# print('n_v: ')
# print(list(n_v))
#
# #
# import pandas as pd
#
# apps_with_duplicates = pd.read_csv(
#     '/Users/nitesh/Desktop/OneDrive - Cal State LA/data_science_practice/Test-1/The Android App Market on Google Play/datasets/apps.csv')
# apps = apps_with_duplicates.drop_duplicates()
#
# # Count the number of apps in each 'Category' and sort them in descending order
# num_apps_in_category = apps['Category'].value_counts().sort_values(ascending=False)
#
# print(num_apps_in_category)
#
# print(apps.head(3))
#
# # Subset for categories with at least 250 apps
# large_categories = apps.groupby('Category').filter(lambda x: len(x) >= 250).reset_index()
#
# print(large_categories)
#
# df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'bar'],
#                     'value': [1, 2, 3, 5]})
#
# df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
#                     'value': [5, 6, 7, 8]})
#
# new_df = pd.merge(df1, df2, on='value')
#
# print(new_df)
#
# # Load user_reviews.csv
# reviews_df = pd.read_csv(
#     '/Users/nitesh/Desktop/OneDrive - Cal State LA/data_science_practice/Test-1/The Android App Market on Google Play/datasets/user_reviews.csv')
#
# print(reviews_df.columns)
# print('\n')
# print(reviews_df.head(3))
# print('\n')
# # Join and merge the two dataframe
# merged_df = pd.merge(apps, reviews_df, on='App', how="inner")
#
# print(merged_df.head(3))
# print('\n')
# # Drop NA values from Sentiment and Translated_Review columns
# merged_df = merged_df.dropna(subset=['Sentiment', 'Translated_Review'])
#
# print(merged_df.head(3))
#
# d = {
#     'one': 1,
#     'two': 2,
#     'three': 3,
#     'four': 4
# }
#
# print(d['three'])
#
# s = "$>$Python"
#
# import numpy as np
#
# z = np.array([[1, 2, 3],
#               [4, 5, 6]])
# print(z[0][0])
#
#
#
# name = 'classification'
#
# print(name.count('s'))
#
# a = np.array([1,2,3])
# b = np.array([4,5,6])
#
# c = np.transpose((a, b))
# print(c)
#
# x = np.array([1, 2, 3, 0 , 5])
# bool_x = x == 3
# print(bool_x)
#
# x = [1, 2, 3]
# x.remove(3)
# print(x)
#
# x = ['a', 'b', 'c', 'a', 'e']
# print(x.count('a'))
#
# dict_gen = {num: num * 2 for num in range(5)}
#
# print(dict_gen)
#
# def po(x, y):
#     return x, y
# print(po(0, 1))
#
# d = {
#     'one': 1,
#     'two': 2,
#     'three': 3,
#     'four': 4
# }
#
# d[['one']['three']]

# class Dog:
#     def __init__(self):
#         pass
#
#     def bark(self):
#         return "bark bark bark bark bark bark..."
#
#
# d = Dog()
# d.bark()
#
# d = {
#     'apple': 1,
#     'banana': 2,
#     'coconut': 3
# }
# d.pop('coconut')
# print(d)
#
#
# flash1 = ['jay garrick', 'barry allen', 'wally west', 'bart allen']
# for p in flash1:
#     pass
#
# superhero = iter(flash1)
# print(next(superhero))
# print(next(superhero))
# print(next(superhero))
# print(next(superhero))
#
# test = enumerate(flash1)
# print('This is list : ' + str(list(test)))
#

#
# mutants = ['charles xavier',
#             'bobby drake',
#             'kurt wagner',
#             'max eisenhardt',
#             'kitty pryde']
#
# print(list(enumerate(mutants)))
#
# a = ('1', '2')
# b = ('a', 'b')
# c = zip(a, b)
# # print('This is list: ' + str(list(c)))
# # for v1, v2 in c:
# #     print(v1, v2)
#
# a1, a2 = zip(*c)
#
# print(a1)
# print(a2)

# A = [list(range(0, 11))]
# print(type(A))
from typing import Tuple

import pandas as pd
#
# a = pd.DataFrame({
#     'A' : [list(range(0, 11))],
#     'B' : [list(range(20, 41))]
# })
#
# total = 0
# for val in a:
#     print(val['A'])


df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar'],
                   'B': [1, 2, 3, 4, 5, 6],
                   'C': [2.0, 5., 8., 1., 2., 9.]})

print(df)

for x in df['B']:
    print('This is iteration value for B :  ' + str(x))
#
# for x,k in df.reset_index().iterrows():
#     print(x,k)
#     print('New')

itr = [x*2 for x in range(0,10,2)]
print(itr)

name = [x[0] for x in 'Nitesh']
print(name)

# y = 23456
# num = [x[0]for x in y]
# print(num)

# Create a 5 x 5 matrix using a list of lists: matrix
matrix1 = [[col,col,col,col] for col in range(5)]
# Print the matrix
for y in matrix1:
    print(y)

matrix = [[col for col in range(5)] for row in range(5)]

for x in matrix:
    print(x)

a = [[x for x in range(2)] for y in range(2)]

for c in a:
    print(c)

def test_gen(n):
    """Returns sequence of numbers till n"""
    i = 0
    while i < n:
        yield i
        i += 1

print(test_gen(3))

for i in test_gen(4):
    print(i)

# List of strings
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# List comprehension
fellow1 = [member for member in fellowship if len(member) >= 7]

# Generator expression
fellow2 = (member for member in fellowship if len(member) >= 7)

for i in fellow1:
    print(type(fellow1))
    print(i)

for i in fellow2:
    print(type(fellow2))
    print(i)

alpha = ['a', 'b']
chra = [1, 2]
z = zip(alpha, chra)
print(list(z))
#
# print(*z)
#
# for z1, z2 in zip(alpha, chra):
#     print(z1, z2)
print(alpha[0:1])

row_list = [['Arab World', 'ARB', 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT', '1960', '133.56090740552298'],
['China World', 'ARB', 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT', '1960', '133.56090740552298']]

print([x for x in row_list])


df = pd.DataFrame({'A': ['foo', 'foo', 'foo', 'foo', 'foo', 'bar'],
                   'B': [1, 2, 3, 4, 5, 6],
                   'C': [2.0, 5., 8., 1., 2., 9.]})

a = df[df['A'] == 'bar']
print(a)

# a = (1.1, 2.2)
#
# print([int(x[0]*x[1]*0.01) for x in a])

x = [2, 4, 1, 5]

sq = {y:y**2 for y in x}

print(sq)