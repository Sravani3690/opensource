n=int(input())
m=[]
for _ in range(n):
    row=list(map(int,input().split()))
    m.append(row)
for row in m:
    print(' '.join(map(str,row[::-1])))
