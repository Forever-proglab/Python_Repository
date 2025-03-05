n = int(input())
p = 0
d = int(input())
prog = int(input("1-арифм. прогрессия или 2-геом. прогрессия?"))
sum = 0
if prog == 1:
    for i in range(n):
        sum += p
        p += d
else:
    for i in range(0, n):
        sum += p
        p *= d
print(p)
print(sum)
