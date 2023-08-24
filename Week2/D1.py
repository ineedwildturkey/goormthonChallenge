from itertools import combinations

n, s = int(input()), input()

sl = set()

idx_list = list(combinations([i for i in range(1, n)], 2))
for l, r in idx_list :
    sl.add(s[:l])
    sl.add(s[l:r])
    sl.add(s[r:])

sl = sorted(list(sl))

result = 0
for l, r in idx_list : 
    sumIdx = sl.index(s[:l]) + sl.index(s[l:r]) + sl.index(s[r:]) + 3
    if sumIdx > result : result = sumIdx

print(result)



"""
코드 해설

1. 길이(이하 n), 문자열(이하 s) 입력받음
2. 부분문자열을 중복 없이 저장하기 위한 빈 set(이하 sl) 생성
3. combination을 이용하여 1부터 n - 1 사이의 값에서 중복 없이 2개를 뽑은 값을 배열(이하 idx_list)에 저장
4. 3의 배열을 이용하여 s를 슬라이싱하고 set에 추가한 뒤, sl을 정렬된 리스트로 변환
5. idx_list를 이용하여 s를 3개의 부분문자열로 나눈 뒤 점수 계산
6. 점수 최대값 출력
"""