for p in range(100, 1000):
        a = p // 100
        b = (p % 100) // 10
        c = p % 10
        if (p - (a+b+c))/3==300:
            print(p)
        else:
            continue
print("No")