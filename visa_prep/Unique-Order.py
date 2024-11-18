n=int(input())
arr=list(map(int,input().split()))
seen=set()
res=[]
for num in arr:
    if num not in seen:
        res.append(num)
        seen.add(num)
print(*res)
