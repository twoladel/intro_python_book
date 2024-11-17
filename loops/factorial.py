# first instinct is for loop
def factorial(number):
    total = 1
    for num in range(1, (number + 1)):
        total *= num
    return total

print(factorial(1))   # 1
print(factorial(2))   # 2
print(factorial(3))   # 6
print(factorial(4))   # 24
print(factorial(5))   # 120
print(factorial(6))   # 720
print(factorial(7))   # 5040
print(factorial(8))   # 40320
print(factorial(25))  # 15511210043330985984000000

# did with while loop to try it
def factor_ial(number):
    total = 1
    while number > 0:
        total *= number
        number -= 1
    return(total)

print(factor_ial(1))   # 1
print(factor_ial(2))   # 2
print(factor_ial(3))   # 6
print(factor_ial(4))   # 24
print(factor_ial(5))   # 120
print(factor_ial(6))   # 720