x,y,z=map(int,input().split())
rc=z-y
if rc<0:
    print(0)
else:
    mm=rc//x
    print(mm)
