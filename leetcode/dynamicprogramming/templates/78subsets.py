from typing import List

class Solutions(object):
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans, sol = [], []

        def backtrack(i):
            if i == n:
                ans.append(sol[:])
                return

            # Don't pick nums[i]
            #All of the backtracking calls are doing this with sol that doesnt include the current picked item
            backtrack(i + 1)

            # Pick nums[i]
            #now all of the following backtracks do it with sol that includes i
            
            sol.append(nums[i])
            backtrack(i + 1)
            #previously apppended is popped at each backtracking level. 
            sol.pop()

        backtrack(0)
        return ans

if __name__ == "__main__":
    nums = [1, 2, 3]
    sol = Solutions()
    subsets = sol.subsets(nums)
    print(subsets)
