n = int(input())

def fact(x):
    if x == 0 :
        return 1
    else:
        return x * fact(x-1)


for i in range(n):
    x = int(input())
    print(fact(x))

