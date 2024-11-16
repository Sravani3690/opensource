t=int(input())
arr=[]
for i in range(t):
    x,n=map(int,input().split())
    y=x//10
    s=y*n
    print(s)
