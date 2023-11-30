

class Solution:
    def reverseString(self, s: List[str]) -> None:

        def reverse(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                reverse(l + 1, r - 1)
            return

        reverse(0, len(s) - 1)


# class Solution:


# stack solution
#     def reverseString(self, s: List[str]) -> None:
#         stack = []
#         for c in s:
#             stack.append(c)

#         i = 0
#         while stack:
#             s[i] = stack.pop()
#             i += 1

# simple

# class Solution:

#     def reverseString(self, s: List[str]) -> None:
#         l = 0
#         r = len(s) - 1

#         while l < r:
#             s[l], s[r] = s[r], s[l]
#             r -= 1
#             l += 1
