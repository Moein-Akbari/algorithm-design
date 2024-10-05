def recursive_fibonacci(n: int) -> int:
    if n <= 2:
        return 1
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


fibs = [0, 1, 1]
def iterative_fibonacci(n: int) -> int:
    for i in range(3, n + 1):
        fibs.append(fibs[i - 1] + fibs[i - 2])
    return fibs[n]


def iterative_fibonacci_constant_memory(n: int) -> int:
    fibs = [0, 1, 1] # fixed-size
    if n < 3:
        return fibs[n]
    
    for _ in range(n - 2):
        fibs3 = fibs[1] + fibs[2]
        fibs.pop(0)
        fibs.append(fibs3)
    
    return fibs[2]


def fibonacci(n: int) -> int:
    return int(
            1/(5 ** 0.5) * ((1 + 5**0.5) / 2) ** n - (
            1/(5 ** 0.5) * ((1 - 5**0.5) / 2) ** n
        )
    )


n = 50
print(recursive_fibonacci(n))
print(iterative_fibonacci(n))
print(iterative_fibonacci_constant_memory(n))
print(fibonacci(n))