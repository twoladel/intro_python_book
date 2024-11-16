age = input('How old are you? ')
print(f'You are {age} years old.')
print()
for i in range(10, 41, 10):
    print(f'In {i} years, you will be {int(age) + i} years old.')