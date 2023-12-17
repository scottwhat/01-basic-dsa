class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        i = 0
        n = len(s)

        while i < n:
            while i < n and s[i] == ' ':
                i += 1
            if i >= n:
                break
            j = i + 1
            while j < n and s[j] != ' ':
                j += 1
            sub = s[i:j]
            if len(result) == 0:
                result = sub
            else:
                result = sub + " " + result
            i = j+1

        return result


print(Solution().reverseWords("Let's   take LeetCode contest"))

# class Solution:
#   def reverseWords(self, s: str) -> str:
#     result = ""
#     i = 0
#     n = len(s)

#     while i < n:
#         while i < n and s[i] == ' ': i += 1
#         if i >= n: break
#         j = i + 1
#         while j < n and s[j] != ' ': j += 1
#         sub = s[i:j]
#         if len(result) == 0: result = sub
#         else: result = sub + " " + result
#         i = j+1

#     return result
