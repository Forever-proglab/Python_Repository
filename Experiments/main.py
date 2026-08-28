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
for e in range(0,151):
    for a in range(0, 151):
        for b in range(0, 151):
            for c in range(0, 151):
                for d in range(0, 151):
                    if a**1 + b**1 + c**1 + d**1 == e**1:
                        print(a+b+c+d+e)

