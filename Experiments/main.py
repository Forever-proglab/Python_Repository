def main():
    dict = {}
    sum = 0
    m = int(input())
    for _ in range(1, m+1):
        l = int(input())
        for _ in range(1, l+1):
            k,u = map(int, input().split())
            sum += k
            dict[k]=u
    for e in range(0, sum+1):
        if dict.get(e) != None:
            print(e, dict[e])




main()