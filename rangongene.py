
n = int(input())
for i in range(n):
    x, y = map(int,input().split(' '))
    a = x
    b = y
    while a != b :
        if a > b :
            a = a-b
        elif b > a :
            b = b-a
    gcd = a
    lcm = int((x*y)/gcd)
    print('(')
    print(gcd , lcm )
    print(') ')