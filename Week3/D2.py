def supply(x, y) :
    adjoin_list = [[x, y]]
    while adjoin_list :
        x, y = adjoin_list.pop()
        visited[x][y] = 1
        for dx, dy in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]] :
            if dx < 0 or dx >= n or dy < 0 or dy >= n : continue
            elif not visited[dx][dy] and city[dx][dy] :
                adjoin_list.append([dx, dy])

n = int(input())
city = [list(map(int, input().split()))[:n] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

result = 0
for i in range(n) :
    for j in range(n) :
        if not visited[i][j] and city[i][j] :
            supply(i, j)
            result += 1

print(result)