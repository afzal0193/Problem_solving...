n =int(input())
li =list(map(int,input().split()))
value = []
store = 0
for i in li:
    if store>0:
        store = store + i
    elif i == -1:
        value.append(i)
    elif i>0:
        store = i
print(len(value))

