a =input()
n =len(a)
value =[]
i = 0
while i<n:
    if a[i] == ".":
         value.append(str(0))

    if a[i] == "-" and a[i + 1] == "-":
        value.append("2")
        i = i + 2
    elif a[i] == "-" and a[i + 1] == ".":
        value.append("1")
        i = i + 2
    else:
        i  = i + 1
print("".join(value))