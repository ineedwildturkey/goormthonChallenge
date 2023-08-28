n, s = int(input()), input()

str_list = []
for i in range(n) :
    for j in range(1, n - 1) : str_list.add(s[i:i + j])
            
str_list = sorted(list(set(str_list)))

result = 0
for a in str_list :
    for b in str_list :
        for c in str_list :
            if a + b + c == s :
                temp = str_list.index(a) + str_list.index(b) + str_list.index(c) + 3
                if temp > result : result = temp

print(result)


"""
시간 초과, for 문을 너무 많이 쓴 것 같다
"""