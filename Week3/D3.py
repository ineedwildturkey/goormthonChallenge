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



"""
코드 해설

1. 한 변의 길이(이하 n)와 단지로 설정할 값(이하 k) 입력, n * n 크기의 배열(이하 city)에 각 칸의 집 번호 입력
2. 배열 순회하여 인접한 집 번호 확인
    1) 해당 좌표 값이 담긴 스택 생성, 측정값 초기화
    2) city의 해당 좌표에서 상하좌우 위치에 해당 좌표의 단지 번호와 같은 값을 가진 집이 있는지 확인, 같다면 측정값 += 1
    3) 더 이상 인접한 집이 없다면 측정 종료
3. 인접한 집 개수가 k개 이상이면 단지 리스트(이하 vill_list)에 추가
4. vill_list에 저장된 값들 중 집 번호가 가장 많은 값 선출
5. 결과 출력
"""