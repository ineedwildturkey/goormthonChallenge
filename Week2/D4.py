def bomb(tile) :
    try :
        return str(int(tile) + 1)
    except ValueError :
        if tile[0] == '@' : return tile + '!'
        else : return tile

n, k = map(int, input().split())

land = [['0' for _ in range(n + 2)]] + [['0'] + list(map(str, input().split())) + [0] for _ in range(n)] + [['0' for _ in range(n + 2)]]

for _ in range(k) :
    y, x = map(int, input().split())
    for i in range(x - 1, x + 2) :
        land[y][i] = bomb(land[y][i])
    for j in range(y - 1, y + 2, 2) :
        land[j][x] = bomb(land[j][x])

result = 0
for li in land[1:n + 1] :
    for sq in li[1:n + 1] :
        if sq[0] == "@" :
            temp = sq.count('!') * 2
            if temp > result : result = temp
        elif sq == "#" : continue
        else :
            if int(sq) > result : result = int(sq)
            
print(result)
