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

#Using lambda()
raise_to_power = lambda x, y: x ** y
raise_to_power(2, 3)

s = map(lambda x: x * 2, (2, 4))
print(tuple(s))

nums = [2, 4, 6, 8]
times_2 = map(lambda num: num * 2, nums)
print(tuple(times_2))

#Using filter() with lambda()
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

#Using reduce()
# Import reduce from functools
from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2 : item1 + item2, stark)

# Print the result
print('This is result of reduce() excersice: ' + result)
