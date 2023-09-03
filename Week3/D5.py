n, k = map(int, input().split())

fruits = []

for _ in range(n):
    p, c = map(int, input().split())
    fruits.append([c // p, p])

fruits.sort(reverse=True)

result, idx = 0, 0
for fruit in fruits :
    piece, cnt = fruit[0], fruit[1]
    if cnt <= k :
        result += piece * cnt
        k -= cnt
    elif not k : break
    else :
        while k :
            result += piece
            k -= 1

print(result)



"""
코드 해설

1. 과일 개수(이하 n), 소지금(이하 k) 입력
2. 과일 가격 정보를 저장할 배열(이하 fruits) 생성 후 값 입력
    1) 과일 가격(이하 p)과 포만감(이하 c) 입력
    2) fruits에 [p ÷ c, p] 형태로 원소 추가
3. fruits 정렬(포만감 높은 순 → 조각 수 많은 순으로 저장)
4. 과일 구매
    1) 포만감 높은 순으로 과일 하나의 가격이 소지금보다 작을 경우 1개 그대로 구매, 가격만큼 k 차감
    2) 과일 하나의 가격이 k보다 클 경우 조각내서 k가 0이 될 때까지 구매
    3) 만약 과일을 전부 샀는데도 소지금이 남을 경우 그대로 종료
    4) 1)~3) 반복
5. 결과 출력
"""