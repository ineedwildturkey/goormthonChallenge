from collections import deque

def net(node) :
    q = deque([node])

    component = set()
    while q :
        crnt = q.popleft()
        
        if visited[crnt] : continue
        
        visited[crnt] = 1
        component.add(crnt)
        
        for i in graph[crnt] :
            if not visited[i] : q.append(i)
    
    edges = 0
    for i in component :
        for to in graph[i] :
            if to in component : edges += 1

    return sorted(list(component)), edges / len(component)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
max_nodes, max_density = [], 0
for i in range(1, n + 1) :
    if not visited[i] :
        nodes, density = net(i)
        if abs(density - max_density) < 1e-8 :
            if len(nodes) < len(max_nodes) :
                max_nodes, max_density = nodes, density
            elif len(nodes) == len(max_nodes) :
                if nodes[0] < max_nodes[0] :
                    max_nodes, max_density = nodes, density
        elif density > max_density :
            max_nodes, max_density = nodes, density

print(*max_nodes)