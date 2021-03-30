t = int(input())
 
for i in range(t):
    y, x = list(map(int, input().split()))
 
    if y==x:
        print(1+x*(x-1))
    elif y>x:
        if y%2==0:
            print(1+y*(y-1)+(y-x))
        else:
            print(1+y*(y-1)-(y-x))
 
    else:
        if x%2==1:
            print(1+x*(x-1)+(x-y))
        else:
            print(1+x*(x-1)-(x-y))