n = int(input())

items = [14, 7, 1]

count = 0
for i in items :
    temp = n // i
    count += temp
    n -= i * temp

print(count)