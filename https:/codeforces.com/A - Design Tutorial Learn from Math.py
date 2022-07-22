def prime(a):
    for i in range(2,(a//2)+1):
        if a%i ==0:
            return  False
    return  True
value = int(input())
st = value//2
stf = 1
ste = value - 1
for i in range(1,st+1):
    if not prime(stf) and  not prime(ste) and ((stf+ste) == value):
        break
    stf = stf + 1
    ste = ste -1
print(stf,ste)
