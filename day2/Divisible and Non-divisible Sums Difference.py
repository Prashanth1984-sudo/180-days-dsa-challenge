n=int(input())
m=int(input())
sum1=0
sum2=0
for i in range(n+1):
    if i%m!=0:
        sum1+=i
    else:
        sum2+=i
print("The difference is:",sum1-sum2)

#Leet code solution

# class Solution:
#     def differenceOfSums(self, n: int, m: int) -> int:
#         sum_not_div = 0
#         sum_div = 0
        
#         for i in range(1, n + 1):
#             if i % m != 0:
#                 sum_not_div += i
#             else:
#                 sum_div += i
        
#         return sum_not_div - sum_div
