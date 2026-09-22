# def main():
#     dict = {}
#     sum = 0
#     m = int(input())
#     for _ in range(1, m+1):
#         l = int(input())
#         for _ in range(1, l+1):
#             k,u = map(int, input().split())
#             sum += k
#             dict[k]=u
#     for e in range(0, sum+1):
#         if dict.get(e) != None:
#             print(e, dict[e])
# main()


# n = int(input())
# k=0
# for i in str(n):
#     k+=int(i)
# n=k
# print(k)
# while k>9:
#     k = 0
#     for i in str(n):
#         k+=int(i)
#     n=k
#     print(k)
# print(k)


# t = False
# for e in range(1,151):
#     for a in range(1, 151):
#         for b in range(1, 151):
#             for c in range(1, 151):
#                 for d in range(1, 151):
#                     if a**5 + b**5 + c**5 + d**5 == e**5:
#                         print(a+b+c+d+e)
#                         t = True
#                     if t:
#                         break
#             if t:
#                 break
#         if t:
#             break
#     if t:
#         break
con = 1
s = 0
while con != 0:
    m, n, l, k = 0,0,0,0
    m1, m2, m3=[],[],[]
    print("This is matrix calculator! How many matrices you want to enter, one or two?")
    u = input()
    if u=='one':
        m, n = int(input()), int(input())
        m1 = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(0, m):
            for d in range(0, n):
                y = input()
                if 'j' in y:
                    m1[i][d]=complex(y)
                else:
                    m1[i][d]=int(y)
        for i in range(len(m1)):
            print(m1[i])
        print(f'{m}×{n}')
        h = input()
        if 'j' in h:
            h1 = complex(h)
        else:
            h1 = int(h)
        m3=[[elem * h1 for elem in row] for row in m1]
        for i in range(len(m3)):
            print(m3[i])
        print(f'{m}×{n}')
    elif u=='two':
        m, n = int(input()), int(input())
        m1 = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(0, m):
            for d in range(0, n):
                y = input()
                if 'j' in y:
                    m1[i][d] = complex(y)
                else:
                    m1[i][d] = int(y)
        l, k = int(input()), int(input())
        m2 = [[0 for _ in range(k)] for _ in range(l)]
        for i in range(0, l):
            for d in range(0, k):
                y = input()
                if 'j' in y:
                    m2[i][d] = complex(y)
                else:
                    m2[i][d] = int(y)
        for i in range(len(m1)):
            print(m1[i])
        print(f'{m}×{n}')
        for i in range(len(m2)):
            print(m2[i])
        print(f'{l}×{k}')
        c = input("What do you want to do with matrices? Enter +, -, *")
        code1 = ([m1[i] for i in range(len(m1))])
        code2 = ([m2[i] for i in range(len(m2))])
        if c=='+':
            if m==l and n==k:
                for i in range(0, m):
                    m3.append([(m1[i][d]+m2[i][d]) for d in range(0, n)])
            else:
                print(f'Матрицы {code1} и {code2} невозможно сложить')
        elif c == '-':
            if m == l and n == k:
                for i in range(0, m):
                    m3.append([(m1[i][d] - m2[i][d]) for d in range(0, n)])
            print(f'Из матрицы {code1} невозможно вычесть матрицу {code2}')
        elif c == '*':
            if n==l:
                m3 = [[0 for _ in range(k)] for _ in range(m)]
                for i in range(m):
                    for j in range(k):
                        s = 0
                        for h in range(n):
                            s += m1[i][h] * m2[h][j]
                        m3[i][j] = s
            else:
                print(f'Матрицы {code1} и {code2} невозможно умножить на друг друга')
    for i in range(len(m3)):
        print(m3[i])
    con = int(input())
