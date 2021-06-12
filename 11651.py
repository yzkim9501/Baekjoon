# 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
t=int(input())
d={}
for _ in range(t):
    a,b=map(int,input().split())
    if(d.get(b)):
        d[b].append(a)
    else:
        d[b]=[a]
for i, j in sorted(d.items(), key=lambda item: int(item[0])):
    if(len(j)==1):
        print(j[0],i)
    else:
        for w in sorted(j):
            print(w,i)
