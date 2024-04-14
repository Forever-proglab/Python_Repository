sum = 0 #сумма чисел, кратных 8-ми
n = 0 #количество чисел, кратных 8-ми
i = int(input())
while i != 0:
    if i % 8 == 0:
        sum = sum + i
        n += 1
    i = int(input())
if sum == 0:
    print("NO")
else:
    print(round(sum / n, 1))

        
