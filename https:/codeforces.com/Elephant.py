v =int(input())
extra = 0
main_value = 0
sum = 0
for i in range(5,0,-1):
    if v>=i:
        main_value = v//i
        extra = v % i
        v =  extra
        sum = sum + main_value
    else:
        continue
print(sum)