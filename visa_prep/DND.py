n,m=map(int,input().split())
arr=list(map(int,input().split()))
sum=0
os=0

for i in arr:
    if(i%m==0):
        sum=sum+i
    else:
        os=os+i
print(sum-os)
