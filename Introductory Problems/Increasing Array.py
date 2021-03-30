n= int(input())
 
arr=list(map(int,input().split()))
moves=0
for i in range(len(arr)-1):
 
    if arr[i+1]<arr[i]:
        # print('HEY')
        moves += arr[i] - arr[i + 1]
        arr[i+1]=arr[i]
 
print(moves)