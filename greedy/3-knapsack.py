from typing import List, Union


class Item:
    def __init__(self, value: float, weight: float, name: str | None):
        self.value = value
        self.weight = weight
        self.name = name

    @property
    def density(self) -> float:
        return self.value / self.weight

    def __str__(self) -> str:
        return f"({self.name}, {self.weight})"
    
    def __repr__(self) -> str:
        return f"({self.name}, {self.weight})"


def fractional_knapsack(items: List[Item], max_weight: int) -> List[Item]:
    available_weight = max_weight
    selected_items: List[Item] = []
    total_value = 0
    items.sort(key=lambda x: x.density)

    while available_weight > 0:
        item = items.pop()

        selected_weight= min(available_weight, item.weight)
        selected_value = selected_weight / item.weight * item.value

        selected_items.append(Item(selected_value, selected_weight, item.name))
        total_value += selected_value
        available_weight -= selected_weight

    return selected_items

if __name__ == '__main__':
    items = fractional_knapsack([Item(50, 50, 0), Item(10, 20, 1), Item(10, 20, 2)], 50)
    print(f"total_value = {sum(item.value for item in items)}, items: {items}")
    