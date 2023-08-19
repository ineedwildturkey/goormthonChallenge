n = int(input())
t, m = map(int, input().split())

for i in range(n) :
	m += int(input())
	while m >= 60 :
		t += 1 if t < 23 else -23
		m -= 60

print(t, m)



"""
코드 해설

1. N, T, M 순서에 맞게 입력
2. 개발 시간 입력하여 M에 추가 (N번 반복)
3. M이 60 이상일 경우 M이 60 미만이 될 때까지 m -= 60 반복하며 T값 변경 (한 줄 if-else문)
    - T가 23 미만이라면 T += 1
    - T가 23(이상)이라면 T -= 23, 즉 T = 0
4. 결과값 출력
"""