#no of rounds
n = int(input())
#lead for player
x =0
y = 0
cl = 0
# in each round
for i in range(n):
    p1 , p2 = map(int , input().split(' '))
    x += p1
    y += p2
    l = abs(x-y)
    while l > cl:
        cl = l
        if x > y:
            win = 1
        else:
            win = 2
print(win , cl)