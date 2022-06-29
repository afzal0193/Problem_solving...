a,b =input().split()
b =int(b)
li =list(map(int,input().split()))
sum = 0
for i in li:
    div = i//b
    div1 = i/b
    if div< div1:
        va = div + 1
        sum = sum + va
    else:
        va = div
        sum = sum + va
print(sum)
