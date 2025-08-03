# https://leetcode.com/problems/happy-number/

# start with positive integer,
# square the number, replace it with the sum of its digits
# repeat until = 1, or it loops forever
# if final = 1 = happy




class Solution: 
# class Solution:

#     # should actually use a linekd list cycle
#     def isHappy(self, n) -> bool:
#         visit = set()
#         # memory 0(n)

#         while n not in visit:
#             visit.add(n)

#             n = self.sumOfSquares(n)

#             if n == 1:
#                 return True

#         # n was already in the set, return false
#         return False

#     def sumOfSquares(self, numInput: int) -> int:

#         # make the num iterable
#         # return sum(int(digit)**2 for digit in str(numInput))

#         output = 0

#         while n:
#             digit = n % 10
#             digit = digit ** 2
#             output += digit
#             n = n // 10

#         return output
