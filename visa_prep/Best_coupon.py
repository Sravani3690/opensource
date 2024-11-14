x=float(input())
dis_10_per=(x-(0.10*x))
flatdis=x-100
finalprice=min(dis_10_per,flatdis)
print(int(finalprice))
