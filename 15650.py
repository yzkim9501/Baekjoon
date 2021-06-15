# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.
x,y=map(int,input().split())
flag=False
count=0
if(y==1):
    for a in range(1,x+1):
        print(a)
elif(y==2):
    for a in range(1,x+1):
        for b in range(a+1,x+1):
            print(a, b)
elif(y==3):
    for a in range(1,x+1):
        for b in range(a+1,x+1):
            for c in range(b+1,x+1):
                print(a, b, c)
elif(y==4):
    for a in range(1,x+1):
        for b in range(a+1,x+1):
            for c in range(b+1,x+1):
                for d in range(c+1,x+1):
                    print(a, b, c, d)
elif(y==5):
    for a in range(1,x+1):
        for b in range(a+1,x+1):
            for c in range(b+1,x+1):
                for d in range(c+1,x+1):
                    for e in range(d+1,x+1):
                        print(a, b, c, d,e)
elif(y==6):
    for a in range(1,x+1):
        for b in range(a+1,x+1):
            for c in range(b+1,x+1):
                for d in range(c+1,x+1):
                    for e in range(d+1,x+1):
                        for f in range(e+1,x+1):
                            print(a, b, c, d,e,f)
elif(y==7):
    for a in range(1,x+1):
        for b in range(a+1,x+1):
            for c in range(b+1,x+1):
                for d in range(c+1,x+1):
                    for e in range(d+1,x+1):
                        for f in range(e+1,x+1):
                            for g in range(f+1,x+1):
                                print(a, b, c, d, e, f, g)
elif(y==8):
    for a in range(1,x+1):
        for b in range(a+1,x+1):
            for c in range(b+1,x+1):
                for d in range(c+1,x+1):
                    for e in range(d+1,x+1):
                        for f in range(e+1,x+1):
                            for g in range(f+1,x+1):
                                for h in range(g+1,x+1):
                                    print(a, b, c, d, e, f, g, h)
