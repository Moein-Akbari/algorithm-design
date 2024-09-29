# This code is based on a Greedy Algorithm

from typing import List, Tuple


def activity_selection(activities: List[Tuple[int, int]]) -> int:
    total_activities = 0
    selected_activities: List[Tuple[int, int]] = []
    activities.sort(key=lambda x: x[1])
    
    last_finish_time = 0
    for activity in activities:
        if activity[0] >= last_finish_time:
            total_activities += 1
            selected_activities.append(activity)
            last_finish_time = activity[1]

    return total_activities

if __name__ == '__main__':
    print(
        activity_selection([
            (1, 2),
            (2, 3),
            (0, 4),
            (4, 5)
        ])
    )