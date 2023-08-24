n, k = map(int, input().split())

plate = [[0 for _ in range(n + 2)]]
for i in range(n) :
    plate.append([0] + list(map(int, input().split()))[:n] + [0])
plate.append([0 for _ in range(n + 2)])

result = 0
for h in range(1, n + 1) :
    for w in range(1, n + 1) :
        goormCount = 0
        if plate[h][w] == 0 :
            for li in plate[h - 1:h + 2] :
                for px in li[w - 1:w + 2] :
                    if px == 1 : goormCount += 1
        if goormCount == k : result += 1

print(result)



"""
코드 해설

1. 한 변 길이(이하 n), 찾는 값(이하 k) 입력
2. (n + 2) * (n + 2)의 2차원 배열(이하 plate) 생성, 1행(열) 또는 마지막행(열)은 제외하고 값 입력
3. 배열 탐색
    1) 2행 2열 칸부터 시작하여 값 확인(1이면 계산 안 함)
    2) 확인한 값(i행 j열)을 제외하고 plate를 (i - 1)행부터 (i + 1)행, (j - 1)열부터 (j + 1)까지의 값 중 1의 개수 구하여 k와 비교
4. 결과 출력
"""