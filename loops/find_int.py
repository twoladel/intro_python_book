# First instinct was list comprehension
def find_integers(collection):
    return [item for item in collection if type(item) is int]

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]


# Below is solution using a for loop
def find_ints(collection):
    integers = []
    for item in collection:
        if type(item) is int:
            integers.append(item)
    return integers

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_ints(my_tuple)
print(integers)                    # [1, 3, -4]
