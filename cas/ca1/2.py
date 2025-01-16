import math

factorials = [math.factorial(i) for i in range(0, 21)]
def _max(n0, k0):
    product = 1
    for i in range(n0):
        product = product * (k0 + i)
    return product / factorials[n0-1]

n, m = int(input()), int(input())
result = 1

while _max(n, result) < m:
    result += 1

print(int(result))