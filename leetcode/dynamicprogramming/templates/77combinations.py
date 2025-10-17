# # all subsets from n to k
# choices: all nums from current index to n
# constraint: path length must be k
# basecase: when path len equals len(nums)
# backtrack: pop last num added

def combine(self, n, k):
    result = []
    
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        
        for num in range(start, n+1):
            path.append(num)
            backtrack(num + 1, path)
            path.pop
            
    backtrack(1, [])
    return result