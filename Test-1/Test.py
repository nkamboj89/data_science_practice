# Define count_entries()
import pandas as pd

tweets_df = pd.read_csv('tweets.csv')


def count_entries(tweets_df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Extract column from DataFrame: col
    col = tweets_df[col_name]

    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] = cols_count[entry] + 1

        # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count


# Call count_entries(): result1
result1 = count_entries(tweets_df)

# Call count_entries(): result2
result2 = count_entries(tweets_df, col_name='source')

# Print result1 and result2
print(result1)
print(result2)

# 04/07

# Using lambda()
raise_to_power = lambda x, y: x ** y
raise_to_power(2, 3)

s = map(lambda x: x * 2, (2, 4))
print(tuple(s))

nums = [2, 4, 6, 8]
times_2 = map(lambda num: num * 2, nums)
print(tuple(times_2))

# Using filter() with lambda()
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

six_list = []
small_char = []

for x in fellowship:
    if len(x) >= 6:
        six_list.append(x)
    else:
        small_char.append(x)

print(six_list)
print('This list contains words less than 6 chars :' + str(small_char))

result = filter(lambda member: len(member) > 6, fellowship)
result_list = list(result)
print(result_list)

# Using reduce()
# Import reduce from functools
from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2: item1 + item2, stark)

# Print the result
print('This is result of reduce() excersice: ' + result)


# 04/08
# def sqrt(x):
#     try:
#         return x ** (0.5)
#     except TypeError:
#         print('pass int or float number')
#
# def sqrt_1(x):
#     if x < 0:
#         raise ValueError('X must be positive number')
#     try:
#         return x ** (0.5)
#     except TypeError:
#         print('pass int or float number')
#
# print(sqrt_1(-1))

test_df = pd.DataFrame({
    'fruits' : ['Mango', 'Orange', 'Banana', 'Mango', 'Apple', 'Mango'],
    'Vegetables' : ['Onion', 'xxx', 'xxx', 'xxx', 'xxx', 'xxx']
})

blank_list = []
for word in test_df['fruits']:
    if word[0:2] == 'Ma':
        blank_list.append(word)
print('\nFor Function\n')
print(blank_list)

result4 = filter(lambda word: word[0:2] == 'Ma', test_df['fruits'])
test_result = list(result4)
print('\nLambda Function\n')
print(test_result)


print(tweets_df.columns.values)

test_result = lambda x: x[0:2] == 'RT', tweets_df['text']
test_list = list(test_result)

for tweet in test_list:
    print(tweet)


# tweet_list = []
# for tweet in tweets_df['text']:
#     if tweet[0:2] == 'RT':
#         tweet_list.append(tweet)
#     else:
#         return 1

# print(tweet_list)
#
# print(tweets_df['text'][0:2])
# print(test_df['fruits'][0:2])



def count_entries(x, col_name='lang'):
    """Return a dictionary with counts of
        occurrences as value for each key."""
    #Adding ValueError with raise
    if col_name not in x.columns:
        raise ValueError ('The DF does not have col :' + col_name)
    # Initialize an empty dictionary: cols_count
    cols_count = {}

    #Add try block
    try:
        # Extract column from DataFrame: col
        col = x[col_name]

        # Iterate over the column in dataframe
        for entry in col:

            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1

            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1
        # Return the cols_count dictionary
        return cols_count

    #Add except block
    except:
        print('The DataFrame does not have a ' + col_name + ' column.')

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Print result1
print(result1)