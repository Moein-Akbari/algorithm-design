n = int(input())
a = list(map(int, input().split()))

dp = [False] * n

indexedNumbers = [(a[i], i) for i in range(n)]

indexedNumbers.sort(reverse=True)

for number, index in indexedNumbers:
    for j in range(index, n, number):
        if (a[j] <= number):
            continue
        dp[index] = dp[index] or (not dp[j])
    
    for j in range(index, -1, -number):
        if (a[j] <= number):
            continue
        dp[index] = dp[index] or (not dp[j])

for tmp in dp:
    if (tmp):
        print("Babak")
    else:
        print("Ramak") 