# Leet code solution
# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         if n <= 0:
#             return False
#         while (n % 3 == 0):
#             n //= 3
#         return n == 1
n=int(input("Enter a number: "))
if n<0:
    print("false")
elif n>0:
    while n%3==0:
        n//=3
        if n==1:
            print("true")
    else:
        print("false")
