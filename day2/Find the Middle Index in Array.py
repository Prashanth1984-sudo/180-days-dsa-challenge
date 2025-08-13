arr=list(map(int,input().split()))
total=sum(arr)
left_sum=0
for i in range(len(arr)):
    right_sum=total-left_sum-arr[i]
    if left_sum==right_sum:
        print(i)
        break
    left_sum+=arr[i]
else:
    print(-1)
