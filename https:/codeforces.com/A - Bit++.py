count = 0
for i in range(int(input())):
    n =input()
    if n =="++X":
        count = count + 1
    elif  n =="X++":
        count = count+1
    else:
        count = count - 1
print(count)
