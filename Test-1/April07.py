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

# Print the results
print('This is result of reduce() excersice: ' + result)
