from collections import deque

def water_jug(jug1, jug2, target):
    visited = set()
    queue = deque([((0, 0), [])])

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        path = path + [(x, y)]

        if x == target or y == target:
            return path

        next_states = [
            (jug1, y),          # Fill Jug1
            (x, jug2),          # Fill Jug2
            (0, y),             # Empty Jug1
            (x, 0),             # Empty Jug2
            (max(0, x-(jug2-y)), min(jug2, x+y)),  # Pour Jug1 -> Jug2
            (min(jug1, x+y), max(0, y-(jug1-x)))   # Pour Jug2 -> Jug1
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state, path))

    return None

# Example
jug1 = 4
jug2 = 3
target = 2

solution = water_jug(jug1, jug2, target)

if solution:
    print("Steps:")
    for step in solution:
        print(step)
else:
    print("No solution exists.")
