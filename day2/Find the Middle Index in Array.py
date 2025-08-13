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
# Leetcode solution
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum_not_div = 0
        sum_div = 0
        
        for i in range(1, n + 1):
            if i % m != 0:
                sum_not_div += i
            else:
                sum_div += i
        
        return sum_not_div - sum_div

