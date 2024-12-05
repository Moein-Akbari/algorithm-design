# In the name of God 

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __str__(self):
        return f"({self.name}, {self.weight})"
    
    def __repr__(self):
        return f"({self.name}, {self.weight})"

def dp_knapsack(items, weight_limit):
    weight_limit += 1
    max_value = [[0] * weight_limit for _ in range(len(items))]

    for weight in range(weight_limit):
        if weight >= items[0].weight:
            max_value[0][weight] = items[0].value

    for item_number in range(1, len(items)):
        for weight in range(weight_limit):
            excluding_new_item = max_value[item_number - 1][weight]
            including_new_item = 0
            if items[item_number].weight <= weight:
                including_new_item = max_value[item_number][weight - items[item_number].weight]\
                      + items[item_number].value
            max_value[item_number][weight] = max(excluding_new_item, including_new_item) 
    return max_value[-1][-1]

n, weight_limit = list(map(int, input().split()))
items = []

for _ in range(n):
    weight, value = list(map(int, input().split()))
    items.append(Item(value, weight))

print(dp_knapsack(items, weight_limit))