# 스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.

# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

t=int(input())
idx=0
stack=[]
a=[False for i in range(t)]
ret=[]
flag="yes"
for _ in range(t):
    i=int(input())
    if(idx<i):
        while(idx!=i and idx<t):
            idx+=1
            if(a[idx-1]==False):
                stack.append(idx)
                ret.append("+")
        if(idx!=i):
            flag="no"
        elif len(stack)!=0:
            idx-=1
            a[idx]=True
            stack.pop()
            ret.append("-")
        else:
            flag="no"
    else:
        while(idx>i and idx>0):
            idx-=1
            if a[idx]==False and len(stack)!=0:
                a[idx]=True
                stack.pop()
                ret.append("-")
            elif len(stack)==0:
                flag="no"
        if(idx!=i):
            flag="no"
        else:
            idx-=1
            if a[idx]==False and len(stack)!=0:
                a[idx]=True
                stack.pop()
                ret.append("-")
            elif len(stack)==0:
                flag="no"

if(flag=="no"):
    print("NO")
else:
    for i in ret:
        print(i)
