#for loop over nums, then dfs down each. 
def permutations(nums):
    n = len(nums)
    ans, sol = [], [] 
    
    def backtrack():
       
       for i in nums:
        if len(sol) == n:
            ans.append(sol[:])
            return
        
        
        for x in nums:
            #only go down this path if 
            if x not in sol:
                sol.append(x)
                backtrack()
                sol.pop()
                
        
        #write out the steps
        #start at the element 

    backtrack()
    return ans 