while True:
    a = int(input())
    b = int(input())
    c = input()
    if c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)
    elif c == "/":
        print(a / b)
    elif c == "^":
        for i in range(b):
            a *= a
        print(a)
    contin = input('Do you want to continue? Write "yes" or "no"')
    if contin == "not":
        break
        
