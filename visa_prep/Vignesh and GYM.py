x,y,z=list(map(int,input().split()))
if(z<x):
    print("0")
else:
    if(x+y<=z):
        print("2")
    else:
        print("1")
