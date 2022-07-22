n =int(input())
value = ["Tetrahedron","Cube","Octahedron","Dodecahedron","Icosahedron"]
sum = 0
for _ in range(n):
    a =input()
    if a ==value[0]:
        sum = sum + 4
    elif a ==value[1]:
        sum = sum + 6
    elif a == value[2]:
        sum = sum + 8
    elif a == value[3]:
        sum =  sum + 12

    elif a == value[4]:
        sum = sum + 20
print(sum)

