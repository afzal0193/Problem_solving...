n,k =map(int,input().split())
temp = n
for _ in range(k):
    temp = str(temp)
    if temp[-1] =="0":
        temp =int(temp)//10
    else:
        temp = int(temp) - 1
print(temp)
