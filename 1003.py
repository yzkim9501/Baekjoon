# N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.
arr=[0,1]
for i in range(1,40):
    arr.append(arr[i-1]+arr[i])
t=int(input())
for _ in range(t):
    ff=int(input())
    if(ff==0):
        print("1 0")
    elif(ff==1):
        print("0 1")
    else:
        print(arr[ff-1],arr[ff])
