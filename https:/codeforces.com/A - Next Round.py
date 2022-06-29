a,b =map(int,input().split())
arr =list(map(int,input().split()))
count = 0
value = arr[b-1]+1 if arr[b-1] is 0 else arr[b-1]
for i in arr:
    if i>=value:
        count = count + 1
if  any(arr):
    print(count)
else:
    print(0)


