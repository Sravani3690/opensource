def absent(n):
    a=list(map(int,input().split()))
    ma=0
    cs=0
    for i in a:
        if(i==0):
            cs+=1
        else:
            ma=max(ma,cs)
            cs=0
    ma=max(ma,cs)
    return ma
    
n=int(input())
print(absent(n))
