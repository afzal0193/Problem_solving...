a =input()
a = a.replace("+","")
value =sorted(a)
v = ""
for i in value:
    v = v+i+"+"
print(v[:-1])
