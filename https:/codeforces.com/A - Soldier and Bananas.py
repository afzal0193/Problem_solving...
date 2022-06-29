k,n,w =list(map(int,input().split()))
i = 1
sum = 0
while i<w+1:
    sum = sum+  k*i
    i = i + 1
value = sum - n
if value>0:
    print(value)
else:
    print(0)