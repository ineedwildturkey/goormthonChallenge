def isComplete(arr) :
    maxIdx = arr.index(max(arr))
    for i in range(maxIdx, 0, -1) :
        if arr[i] < arr[i - 1] : return 0
    for j in range(maxIdx, len(arr) - 1) :
        if arr[j] < arr[j + 1] : return 0
    return sum(arr)

n = int(input())
hbg = list(map(int, input().split()))[:n]

print(isComplete(hbg))


"""
코드 해설

1. N값 입력 후 map 이용하여 연속으로 값 입력받음, 이후 함수에 사용하기 위해 리스트로 변환
2. isComplete 함수 실행
    - 최댓값을 가지는 인덱스 찾음
    - 최댓값을 기준으로 리스트 왼쪽과 오른쪽으로 순차 탐색하면서 현재 값과 다음 값을 비교하여 값이 같거나 감소하는지 확인, 그렇지 않으면 0 반환
3. 결과값 출력
"""