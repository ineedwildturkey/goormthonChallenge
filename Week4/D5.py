def scan(a, b):
    visited = set()
    target = matrix[a][b]

    stack = [(a, b)]
    while stack:
        sy, sx = stack.pop()

        if (sy, sx) in visited:
            continue
        visited.add((sy, sx))

        for dy, dx in dirc:
            temp_y, temp_x = sy + dy, sx + dx
            if 0 <= temp_y < n and 0 <= temp_x < n \
                and matrix[temp_y][temp_x] == target:
                stack.append((temp_y, temp_x))

    if len(visited) >= k:
        for vy, vx in visited:
            matrix[vy][vx] = '.'

n, k, q = map(int, input().split())

dirc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

matrix = [list(input()) for _ in range(n)]

for _ in range(q):
    y, x, s = map(str, input().split())
    y, x = int(y) - 1, int(x) - 1
    matrix[y][x] = s
    scan(y, x)

for line in matrix:
    print(*line, sep='')