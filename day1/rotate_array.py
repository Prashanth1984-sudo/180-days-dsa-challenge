arr=list(map(int,input().split()))
k=int(input())
d=len(arr)
k=k%d
arr=arr[-k:]+arr[:-k]
print(arr)