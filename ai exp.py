from heapq import heappush, heappop

goal = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 0))

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                x = (value - 1) // 3
                y = (value - 1) % 3
                distance += abs(i - x) + abs(j - y)
    return distance

def neighbors(state):
    state = [list(row) for row in state]

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j

    result = []

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            result.append(tuple(map(tuple, new_state)))

    return result

def solve(start):
    pq = []
    heappush(pq, (heuristic(start), 0, start, []))
    visited = set()

    while pq:
        f, g, state, path = heappop(pq)

        if state == goal:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)

        for next_state in neighbors(state):
            if next_state not in visited:
                heappush(
                    pq,
                    (g + 1 + heuristic(next_state),
                     g + 1,
                     next_state,
                     path + [state])
                )

    return None

start = (
    (1, 2, 3),
    (4, 0, 6),
    (7, 5, 8)
)

solution = solve(start)

if solution:
    print("Solution Found:\n")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
