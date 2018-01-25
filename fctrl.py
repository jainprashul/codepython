def zeros(n):
    i = 5
    if n < i:
        return 0
    elif i <= n < 10:
        return 1
    else:
        return n // i + zeros(n // i)

n = int(input())
for i in range(n):
    x = int(input())
    print(zeros(x))
