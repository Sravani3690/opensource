import math
x,n=map(int,input().split())
#p=x*100
#p=n//100
#p=n-p
p=math.ceil(n/100)
ap=max(0,p-x)
print(ap)
