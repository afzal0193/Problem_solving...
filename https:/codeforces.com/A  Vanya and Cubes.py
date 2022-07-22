def number_sum(a):
    sum = 0
    for i in range(1,a+1):
        sum = sum + i
    return  sum
n =int(input())
i = 1
sum = 0
count = 0
while True:
    sum = sum + number_sum(i)
    if sum<=n:
        count = count + 1
    else:
        break
    i = i + 1
print(count)