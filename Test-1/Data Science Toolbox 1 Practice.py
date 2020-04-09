from functools import reduce

product = [1, 2, 5, 10]
result = reduce(lambda x, y: x * y, product)
print(result)

print('\nThis is new code\n')


def add_zeros(string):
    """Returns a string padded w/ zeros"""
    updated_string = string + '0'

    def add_more():
        """Adds more zeros if necessary"""
        nonlocal updated_string
        updated_string = updated_string + '0'

    while len(updated_string) < 6:
        add_more()
    return updated_string


# print(add_zeros('3.4'))
print((add_zeros('3.4'), add_zeros('2.345')))

print('\nThis is new code\n')


def celsius(x):
    y = (x - 32) * 5 / 9
    return y


print(celsius(75))

print('\nThis is new code\n')


def square(s):
    try:
        a = s * s
        p = 4 * s
        return a, p
    except TypeError:
        print('s can not be string')


square(4)

print('\nThis is new code\n')


def list_range(x):
    min_x = min(x)
    max_x = max(x)
    a = (min_x, max_x)
    return a

print(list_range((24, 36, 34, 32)))

print('\nThis is new code\n')

def sorted_elements(x, desc=True, n=3):
    new_x = sorted(x, reverse=desc)[0:n]
    return new_x

a = [5, 5, 12, 12, 14, 7]
print(sorted_elements(a))

print('\nThis is new code\n')

# def nth_root(n):
#     def actual_root(x):
#         root = x ** (1/n)
#         return root
#     return  actual_root
#
# print(nth_root((3)(27)))

print('\nThis is new code\n')

x  = ['m','w','m','t','m']
counts = {}
for val in x:
    if val in counts.keys():
        counts[val] += 1
    else:
        counts[val] = 1

print(counts)

print('\nThis is new code\n')

# def get_choice(c):
#     choices = {'A': 25,
#                'B': 15,
#                'C': 50}
#     if c not in choices.keys():
#         raise ValueError('Invalid Choice')
#     n = choices[c]
#     return n
#
# print(get_choice('D'))

print('\nThis is new code\n')

def add_max(x, y):
    z = max(x) + max(y)
    return z
print(add_max([9, 5], [2, 11]))

print('\nThis is new code\n')

def find_type(**y):
    return type(y)

print(find_type(a = 'alpha', b = 'beta'))

print('\nThis is new code\n')

def mean(*args):
    total_sum = 0
    n = len(args)
    for x in args:
        total_sum += x
    return total_sum/n

print((mean(3, 4), mean(10, 15, 20)))

print('\nThis is new code\n')

add_sq = (lambda x, y: x**2 + y**2)
print(add_sq(5, 4))

print('\nThis is new code\n')

temp = 40

def convert_temp(x):
    global temp
    temp = (x * 1.8) + 32

convert_temp(temp)
print(temp)