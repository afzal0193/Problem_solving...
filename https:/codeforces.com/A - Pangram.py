import string
val = string.ascii_lowercase
a =int(input())
b =input().lower()
va = set(b)
count  = 0
for  i in va:
    if i in b:
        count = count + 1
if count>=26:
    print("YES")
else:
    print("NO")

