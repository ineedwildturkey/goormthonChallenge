n = int(input())

items = [14, 7, 1]

count = 0
for i in items :
    temp = n // i
    count += temp
    n -= i * temp

print(count)


"""
코드 해설

1. n 입력
2. 아이템의 통증 감소 수치를 내림차순으로 배열(이하 items)에 저장
3. n ÷ (items에 저장된 값)을 순서대로 몫이 최대가 될 때까지 계산 후 그 몫을 결과 값에 추가, n은 나눈 후의 나머지 값으로 갱신
4. 결과 출력
"""