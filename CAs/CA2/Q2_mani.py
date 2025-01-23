from collections import deque, defaultdict

def solve_gallery_problem(n, m, k, gallery, starting_points):
    def bfs(y, x):
        queue = deque([(y, x)])
        visited[y][x] = True
        cells = []
        paintings_count = 0
        
        while queue:
            cy, cx = queue.popleft()
            cells.append((cy, cx))
            
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < n and 0 <= nx < m:
                    if gallery[ny][nx] == '*':
                        paintings_count += 1
                    elif not visited[ny][nx] and gallery[ny][nx] == '.':
                        visited[ny][nx] = True
                        queue.append((ny, nx))
        
        for cy, cx in cells:
            painting_cache[(cy, cx)] = paintings_count
        return paintings_count

    visited = [[False] * m for _ in range(n)]
    painting_cache = {}
    results = []

    for y, x in starting_points:
        if (y - 1, x - 1) in painting_cache:
            results.append(painting_cache[(y - 1, x - 1)])
        else:
            results.append(bfs(y - 1, x - 1))

    return results

n, m, k = map(int, input().split())
gallery = [input().strip() for _ in range(n)]
starting_points = [tuple(map(int, input().split())) for _ in range(k)]

results = solve_gallery_problem(n, m, k, gallery, starting_points)
print("\n".join(map(str, results)))