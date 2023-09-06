n, m = map(int, input().split())

dirc = {"U" : [-1, 0], "D" : [1, 0], "L" : [0, -1], "R" : [0, 1]}
plate = [[''] * n for _ in range(n)]

for _ in range(m):
    y, x, cmd = map(str, input().split())
    y, x = int(y) - 1, int(x) - 1
    while 0 <= y < n and 0 <= x < n :
        dy, dx = dirc[cmd]
        plate[y][x] = plate[y][x] + cmd
        y += dy
        x += dx

count = 0
for line in plate :
    for pixel in line :
        u, d, l, r = pixel.count('U'), pixel.count('D'), pixel.count('L'), pixel.count('R')
        count += u * l
        count += u * r
        count += d * l
        count += d * r

print(count)
