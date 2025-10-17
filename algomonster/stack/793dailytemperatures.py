class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        # stores indices of previous colder days
        
        #store the indices 
        stack: list[int] = []
        for i in range(len(temperatures)):
            
            
            # while the stack is not empty and current day is warmer than the day referred by the top of the stack
            #while its not empty and temperatures of the stack top are less than temp of i
            while stack and temperatures[stack[-1]] < temperatures[i]:
                # pop the index of the colder previous day
                prev_day_index = stack.pop()
                
                #we are tracking indexes 
                # set the popped index in the res array to (current index - the popped index)
                #results array, append, the current index - popped prev_day_index, to get the distance 
                #we are dealing with indexes here, 
                res[prev_day_index] = i - prev_day_index
            # push the current index to stack
            stack.append(i)

        return res
