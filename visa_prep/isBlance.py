n=int(input())
arr=list(map(int,input().split()))
ts=sum(arr)
l=0
r=ts
res=[]
for i in range(n):
    r-=arr[i]
    res.append(abs(l-r))
    l+=arr[i]
print(" ".join(map(str,res)))
