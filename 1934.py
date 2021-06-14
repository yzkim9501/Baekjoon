# 두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.

def gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    print(a*b//gcd(a,b))
