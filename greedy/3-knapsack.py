# In the name of god

class Item:
    def __init__(self, value, weight, name):
        self.value = value
        self.weight = weight
        self.name = name   

    def __str__(self):
        return f"({self.name}, {self.weight})"
    
    def __repr__(self):
        return f"({self.name}, {self.weight})"

def fractional_knapsack(items, max_weight):
    
    available_weight = max_weight
    selected_items = []
    total_value = 0
    items.sort(key=lambda x: x.value / x.weight)

    while available_weight > 0:
        item = items.pop()
        # print(item)
        selected_weight= min(available_weight, item.weight)
        selected_value = selected_weight / item.weight * item.value
        selected_items.append(Item(selected_value, selected_weight, item.name))
        total_value += selected_value
        available_weight -= selected_weight

    return (total_value, selected_items)

if __name__ == '__main__':
    tst1 = [Item(50, 50, 0), Item(10, 20, 1), Item(10, 20, 2)]
    total_value, items = fractional_knapsack(tst1, 50)
    print(f"total_value = {total_value}, Items: {items}")
    