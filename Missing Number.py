t = int(input())
 
 
n= list(map(int,input().split()))
 
print(int((t*(t+1)/2)-sum(n)))