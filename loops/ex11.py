my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]
# extract even numbers with while loop
counter = 0
index = 0
while counter < len(my_list):
    number = my_list[counter][index]
    if number % 2 == 0:
        print(number)
    index += 1
    if index == len(my_list[counter]):
        counter += 1
        index = 0