n=int(input())
cd=1
for i in range(1,n+1):
    row=[cd+j for j in range(i)]
    print(*row)
    cd+=i
