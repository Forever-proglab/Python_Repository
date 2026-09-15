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
while con != 0:
    m, n, l, k = 0,0,0,0
    m1, m2=[],[]
    print("Это калькулятор матриц! Сколько матриц вы хотите ввести, одну или две?")
    if input()=='один':
        m, n = int(input()), int(input())
        for i in range(1, m+1):
            m1.append([int(input()) for d in range(1, n+1)])
    for i in range(len(m1)):
        print(m1[i])
    con = int(input())
