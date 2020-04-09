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