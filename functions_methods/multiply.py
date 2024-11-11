first_number = input('Enter first number: ')
second_number = input('Enter second number: ')

def multiply(first_num, second_num):
    return float(first_num) * float(second_num)

product = multiply(first_number, second_number)
print(f"{first_number} * {second_number} = {product}")