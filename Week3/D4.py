n, m, k = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m) : 
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)) :
    graph[i].sort(reverse=True)

visited = [k]
while True : 
    if graph[k] :
        temp = graph[k].pop()
        if temp not in visited :
            visited.append(temp)
            k = temp
    else : break

print(len(visited), k)



"""
코드 해설

1. 노드 개수(이하 n)와 간선 개수(이하 m)와 시작 노드 값(이하 k) 입력
2. 각 노드마다 연결된 상대 노드를 저장할 2차원 배열(이하 graph) 생성(크기는 n + 1)
3. 각 간선의 양끝에 연결된 노드 값 입력
    - a, b를 입력했다고 하면 graph[b]에 a 추가, graph[a]에 b 추가
4. graph의 각 배열을 내림차순으로 정렬
5. 방문한 노드 생성, 초기 값은 [k]
6. k번 노드부터 규칙에 따라 탐색
    1) graph[k]에서 제일 작은 값(graph[k][-1], 이하 temp) 빼낸 후 visited에 저장
    2) k를 temp로 교환
    3) k번 노드에서 더이상 이동할 노드가 없을 때까지 반복
7. 결과 출력
"""