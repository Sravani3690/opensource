n=int(input())
sign=-1 if n<0 else 1
n=abs(n)
num=str(n)
rev=int(num[::-1])
rev*=sign
if(rev<-2**31) or (rev>2**31-1):
    print("0")
else:
    print(rev)
