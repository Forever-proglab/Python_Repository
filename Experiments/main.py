import sys


def main():
    dict = {}
    sum = 0
    m = int(input())
    for _ in range(1, m+1):
        l = int(input())
        for _ in range(1, l+1):
            k,u = map(int, input().split())
            sum += 1
            dict[k]=u
    return print(dict.items())
            



if __name__ == '__main__':
    main()