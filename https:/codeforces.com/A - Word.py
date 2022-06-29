a =input()
count_upper = 0
count_lower = 0
for i in a:
    if i.isupper():
        count_upper +=1
    if i.islower():
        count_lower +=1
if count_upper==count_lower:
    print(a.lower())
elif count_upper>count_lower:
    print(a.upper())
elif count_upper<count_upper:
    print(a.lower())
