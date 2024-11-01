balance = 1000 * 1.05
print(f"Balance after one year is: {balance}")
balance *= 1.05
print(f"Balance after two years is: {balance}")
balance *= 1.05
print(f"Balance after three years is: {balance}")
balance *= 1.05
print(f"Balance after four years is: {balance}")
balance *= 1.05
print(f"Balance after five years is: {balance}")


# My solution would be:
balance = 1000
for i in range(5):
    balance *= 1.05
    print(f"Balance after {i + 1} year is ${balance:.2f}")