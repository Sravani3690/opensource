t=int(input())
for i in range(t):
    n,m=list(map(int,input().split()))
    if(n<=m):
        print(0)
    else:
        print(abs(m-n))
