class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for day, temp in enumerate(temperatures):

            while stack and stack[-1][0] < temp:
                prevTemp, prevDay = stack.pop()
                res[prevDay] = day-prevDay
            
            stack.append([temp, day])
        
        return res
        
        