n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

ans = 0
sum_ = 0

for i in range(n):
    if (numbers[i] >= sum_):
        ans += 1
        sum_ += numbers[i]

print(ans)