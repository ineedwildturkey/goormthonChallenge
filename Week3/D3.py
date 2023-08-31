def needSupply(y, x, num) :
    adjoin, count = [[y, x]], 0
    
    while adjoin :
        ty, tx = adjoin.pop()
        if city[ty][tx] != num : continue
        
        city[ty][tx] = 0
        count += 1
        
        for dy, dx in [[ty - 1, tx], [ty + 1, tx], [ty, tx - 1], [ty, tx + 1]] :
            if dy < 0 or dy >= n or dx < 0 or dx >= n : continue
            adjoin.append([dy, dx])
    
    return count

n, k = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(n)]

vill_list = []
for i in range(n) :
    for j in range(n) :
        if city[i][j] :
            temp = city[i][j]
            supply_count = needSupply(i, j, temp)
            if supply_count >= k : vill_list.append(temp)

max_count, result = 0, 0
for i in range(1, 31) : 
    temp = vill_list.count(i)
    if temp >= max_count :
        max_count = temp
        result = i
            
print(result)