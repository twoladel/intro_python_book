# My initial solution
balance = 1000
for i in range(5):
    balance *= 1.05

print(f"{balance:.2f}")

# LS solution here
balance = (1000 * 1.05 * 1.05 * 1.05 * 1.05 * 1.05)
print(balance)
