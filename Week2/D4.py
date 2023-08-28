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


"""
코드 해설

1. 한 변 길이(이하 n), 떨어트릴 폭탄 개수(이하 k) 입력
2. (n + 2) * (n + 2) 크기의 2차원 배열(이하 land) 생성
3. 가장자리를 제외하고 n * n 구역의 픽셀 값 입력
4. 폭탄을 떨어트리는 함수 bomb 실행
    1) 해당 좌표와 그 좌표의 상하좌우 위치의 값을 바꿈
    2) 숫자면 해당 값 + 1, @면 문자열 뒤에 ! 추가, #면 아무것도 하지 않고 값 반환
5. 배열 탐색하여 최대값 계산(숫자면 그대로, @면 (!의 개수) * 2, #면 계산하지 않음) 후 출력
"""