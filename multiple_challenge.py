def count_mul(n):
    c3=n//3
    c5=n//5
    c15=n//15
    res=c3+c5-c15
    return res
n=int(input())
print(count_mul(n))
