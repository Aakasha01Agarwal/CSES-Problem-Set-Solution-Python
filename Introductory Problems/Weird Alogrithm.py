n=int(input())
l=[]
l.append(n)
while n>1:
    if n%2 is 1:
 
        l.append(n*3+1)
        n = n * 3 + 1
    else:
 
        l.append(int(n/2))
        n = int(n / 2)
 