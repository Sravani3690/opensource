n=int(input())
results=[]
for i in range(n):
    x,y=list(map(int,input().split()))
    res=x-y+1
    results.append(res)
for i in results:
    print(i)
