n =list(input().lower())
li =list(map(str,input().lower()))
value =""
for i in li:
    value = value+ i
if n[0] in value or n[1] in value:
    print("YES")
else:
    print("NO")