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
        for i in range(1, m+1):
            m1.append([int(input()) for d in range(1, n+1)])
        for i in range(len(m1)):
            print(m1[i])
        print(f'{m}×{n}')
    elif u=='two':
        m, n = int(input()), int(input())
        for i in range(1, m + 1):
            m1.append([int(input()) for d in range(1, n + 1)])
        l, k = int(input()), int(input())
        for i in range(1, l + 1):
            m2.append([int(input()) for d in range(1, k + 1)])
        for i in range(len(m1)):
            print(m1[i])
        print(f'{m}×{n}')
        for i in range(len(m2)):
            print(m2[i])
        print(f'{l}×{k}')
        c = input("What do you want to do with matrices? Enter +, -, *")
        if c=='+':
            if m==l and n==k:
                for i in range(0, m):
                    m3.append([(m1[i][d]+m2[i][d]) for d in range(0, n)])
        elif c == '-':
            if m == l and n == k:
                for i in range(0, m):
                    m3.append([(m1[i][d] - m2[i][d]) for d in range(0, n)])
        elif c == '*':
            if n==l:
                for i in range(0, m):
                    for d in range(0, k):
                        s = 0
                        for h in range(0, l):
                            s += m1[i][l]*m2[i][l]
                        m3[i][k]=s
        for i in range(len(m3)):
            print(m3[i])
    con = int(input())
