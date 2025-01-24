import heapq

def dijkstra(n, neighbours, start):
    dist = [float('+inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        current_dist, u = heapq.heappop(heap)
        if current_dist > dist[u]:
            continue

        for v, w in neighbours[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist

def count_treasure_locations(n, distances, streets, num):
    count = 0
    
    # The treasure is in a square
    for i in range(1, n + 1):
        if distances[i] == num:
            count += 1

    # The treasure is in streets (by some conditions)
    for vi, ui, wi in streets:
        # Both ends of the streets are reachable
        if distances[vi] < num and distances[ui] < num:
            # when both ends of the streets are reachable, we can consider an "x" in

            # the treuasure is in the middle of the street
            if distances[vi] + distances[ui] + wi == 2 * num:
                count += 1
            # it is not in the midde of the street so there are two reachable points
            elif distances[vi] + distances[ui] + wi > 2 * num:
                count += 2
        elif distances[vi] < num:
            if distances[vi] + wi > num:
                count += 1
        elif distances[ui] < num:
            if distances[ui] + wi > num:
                count += 1

    return count

n, m, start = list(map(int, input().split()))
streets = []
for _ in range(m):
    streets.append(tuple(map(int, input().split())))

num = int(input())
if num == 0:
    print(1)
else:
    neighbours = [[] for _ in range(n + 1)]
    for vi, ui, wi in streets:
        neighbours[vi].append((ui, wi))
        neighbours[ui].append((vi, wi))

    distances = dijkstra(n, neighbours, start)
    print(count_treasure_locations(n, distances, streets, num))