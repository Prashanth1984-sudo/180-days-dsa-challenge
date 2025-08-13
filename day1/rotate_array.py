arr=list(map(int,input().split()))
k=int(input())
d=len(arr)
k=k%d
arr=arr[-k:]+arr[:-k] #This rotates the array to the right by k steps
print(arr)
# to rotate the array to the left by k steps
#arr=arr[k:]+arr[:k]
