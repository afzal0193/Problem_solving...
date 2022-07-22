a =int(input())
li = list(map(int,input().split()))
max = max(li)
value_sum = 0
for i in li:
    sum = max - i
    value_sum += sum
print(value_sum)

