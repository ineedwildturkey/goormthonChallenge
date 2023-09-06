def find_root(i):
    if root[i] != i:
        root[i] = find_root(root[i])
    return root[i]

def union(a, b):
    fa, fb = find_root(a), find_root(b)
    if fa < fb:
        root[fb] = fa
    else:
        root[fa] = fb

n, m = map(int, input().split())

root = [i for i in range(n + 1)]
matrix = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    my, mx = map(int, input().split())
    matrix[my][mx] = 1

for y in range(1, n + 1):
    for x in range(1, n + 1): 
        if matrix[y][x] and matrix[x][y]:
            union(y, x)

root_list = set()
for i in range(1, n + 1):
    root_list.add(find_root(i))

print(len(root_list))