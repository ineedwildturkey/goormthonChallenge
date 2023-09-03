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


"""
코드 해설

1. 한 변의 길이 입력 후 n * n 크기의 배열(이하 city)에 각 칸의 집 여부 입력
2. 방문 여부를 확인하기 위한 배열(이하 visited) 생성(초기 값은 n개의 0을 가진 배열 n개)
3. 집이 있는 구역마다 인접 여부 확인, 확인이 끝나면 발전기 개수 추가
    1) 해당 좌표가 담긴 스택 생성
    2) 해당 좌표 값을 스택에서 꺼낸 후 그 값을 기준으로 city의 상하좌우 위치에 집이 있을 경우 스택과 visited에 해당 집의 좌표 추가
    3) 스택이 빌 때까지 2)를 반복
4. 결과 출력
"""