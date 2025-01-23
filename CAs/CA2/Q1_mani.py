def dfs(node, current_distance, num, graph, path, result):
    if current_distance == num:
        result.add(node)
        return
    if current_distance > num:
        return
    for neighbor, weight in graph[node]:
        if neighbor not in path:
            if current_distance + weight <= num:
                path.add(neighbor)
                dfs(neighbor, current_distance + weight, num, graph, path, result)
                path.remove(neighbor)
            if current_distance + weight > num:
                if node < neighbor:
                    result.add((node, neighbor, num - current_distance))
                else:
                    result.add((neighbor, node, weight - num + current_distance))

def find_treasure_points(n, m, start, streets, num):
    graph = {i: [] for i in range(1, n + 1)}
    for v, u, w in streets:
        graph[v].append((u, w))
        graph[u].append((v, w))
    result = set()
    path = set()
    path.add(start)
    dfs(start, 0, num, graph, path, result)
    return len(result)

n, m, start = map(int, input().split())
streets = [tuple(map(int, input().split())) for _ in range(m)]
num = int(input())

print(find_treasure_points(n, m, start, streets, num))