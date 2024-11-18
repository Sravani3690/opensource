from collections import Counter
n=int(input())
arr=list(map(int,input().split()))
counter=Counter(arr)
for ele, c in counter.items():
    if c==1:
        print(ele)
         
         
