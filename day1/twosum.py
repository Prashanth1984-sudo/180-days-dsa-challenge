n=int(input())
arr=list(map(int,input().split()))
target=int(input())
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print("Pair found:",i,j)  