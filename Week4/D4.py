from collections import deque

def routing(start, end, day) :
    if day == start or day == end:
        return -1

    q = deque([start])
    visited = [0] * (n + 1)
    visited[start] = 1
    min_root_count = 1

    while q:
        min_root_count += 1

        for _ in range(len(q)):
            crnt = q.popleft()

            for nxt in graph[crnt]:
                if nxt == e : return min_root_count

                if visited[nxt] or nxt == day : continue

                visited[nxt] = 1
                q.append(nxt)

    return -1

n, m, s, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    print(routing(s, e, i))