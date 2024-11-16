n=int(input())
arr=list(map(int,input().strip().split()))
#n=str(arr)
n=arr[::-1]
print(*n)
