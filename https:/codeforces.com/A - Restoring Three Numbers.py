list = list(map(int,input().split()))
min_value =min(list)
max_value1 = max(list)
list.remove(max_value1)
max_value2 =max(list)
a = max_value1 - max_value2
b = min_value - a
c = max_value1 -(a+b)
arr = []
arr.append(str(a))
arr.append(str(b))
arr.append(str(c))
print(" ".join(arr))
