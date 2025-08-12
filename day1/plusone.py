# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
arr=list(map(int,input().split()))
for i in range(len(arr)-1,-1,-1):
    if arr[i]<9:
        arr[i]+=1
        break
    arr[i]=0
else:
    arr.insert(0,1)
print(arr)