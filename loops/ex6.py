my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]
even_or_odd = []
for number in my_list:
    if number % 2 == 0:
        even_or_odd.append('even')
    else:
        even_or_odd.append('odd')

print(even_or_odd)