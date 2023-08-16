result = 0
for i in range(int(input())) :
    n, s, m = map(str, input().split())
    n, m = int(n), int(m)
    if s == '+' : result += n + m
    elif s == '-' : result += n - m
    elif s == '*' : result += n * m
    elif s == '/' : result += n // m

print(result)



"""
코드 해설

1. 결과값 초기화, T값 입력(for문의 range 값으로 바로 사용)
2. for문 내에서 피연산자, 연산 기호, 연산자를 map을 이용해 공백으로 구분 후 문자열 자료형으로 입력받음
3. 조건문 이용하여 계산, 나눗셈은 나머지를 버리므로 '//' 연산자 사용
4. 결과 출력

* eval문 사용 시 : 연산 기호가 나눗기인 경우 'eval(f'{피연산자}{연산 기호}{연산 기호}{연산자}')' 형태로 작성해야 함
"""