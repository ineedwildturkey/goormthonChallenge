n = int(input())
a, b = map(int, input().split())
if b > a : a, b = b, a

count = -1

aCount = n // a
while aCount :
    temp = n - (a * aCount)
    if temp % b : aCount -= 1
    else : 
        count = aCount + (temp // b)
        break

if aCount :
    print(count)
else :
    if n % b : print(count)
    else : print(n // b)
    
"""
코드 해설

1. n, a, b 입력, b > a면 a, b 값 교환
2. n ÷ a의 몫(이하 aCount)을 이용하여 while문 실행
    1) 1) n - a × aCount(이하 temp) 가 b로 나눠질 경우 aCount + temp / b 출력
    2) 그렇지 않다면 aCount - 1로 1)을 다시 실행
    3) aCount가 0이라면 b만으로 나눠지는지 확인, 참이면 n / b 출력
    4) 3)이 거짓이면 -1 출력
"""