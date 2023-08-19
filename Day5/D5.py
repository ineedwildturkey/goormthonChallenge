def sort(arr) :
	if len(arr) < 2 : return arr

	m = len(arr) // 2
	lArr, rArr = sort(arr[:m]), sort(arr[m:])
	
	mArr = []
	l = h = 0
	while l < len(lArr) and h < len(rArr) :
		if lArr[l][1] > rArr[h][1] :
			mArr.append(lArr[l])
			l += 1
		elif lArr[l][1] == rArr[h][1] :
			if lArr[l][0] > rArr[h][0] :
				mArr.append(lArr[l])
				l += 1
			else :
				mArr.append(rArr[h])
				h += 1
		else :
			mArr.append(rArr[h])
			h += 1
	
	mArr += lArr[l:]
	mArr += rArr[h:]
	
	return mArr

n, k = map(int, input().split())

arr = []
for i in list(map(int, input().split()))[:n]:
	arr.append([i, str(bin(i)).count('1')])

print(sort(arr)[k - 1][0])



"""
코드 해설

1. N, K 입력
2. 빈 배열 arr 생성 후 정렬할 값을 map을 이용하여 각각 입력받음
    - arr에는 입력한 값과 입력한 값의 2진수에서 1의 개수를 배열 형태로 값 추가
3. arr을 내림차순으로 병합 정렬
    - 이때, 서로 비교하는 값이 2진수로 표현했을 때의 1의 개수가 같다면 10진수의 값이 큰 쪽이 먼저 저장되도록 설정
4. 정렬한 값의 K번째(Index : K - 1) 10진수 출력
"""