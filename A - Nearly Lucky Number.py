a =input()
count = 0
for i in a:
    if i =="4" or i=="7":
        count = count + 1
if count in [4,7]:
    print("YES")
else:
    print("NO")