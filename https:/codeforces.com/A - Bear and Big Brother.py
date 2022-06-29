a,b =map(int,input().split())
i = a
j = b
c = 0
while True:
    if i>j:
        break
    else:
        i = i *3
        j = j*2
        c = c  + 1
print(c)
