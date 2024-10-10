# In the name of God

l = int(input())
prices = list(map(int, input().split(' ')))

best_price = [0] * l 
best_price[0] = prices[0]
for length in range(2, l):
    price = prices[length]
    for selected_length in range(1, length + 1):
        #TODO: Check -21
        price = max(price, best_price[length - selected_length - 1] + prices[selected_length])
    best_price[length] = price

# print(best_price)
print(best_price[l - 1])