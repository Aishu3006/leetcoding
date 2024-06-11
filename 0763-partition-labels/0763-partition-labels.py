class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {}
        res = []
        i = 0
        
        for j in range(len(s)):
            c = s[j]
            count[c] = j
        
        goal = 0
        curLen = 0
        while i<len(s):
            c = s[i]
            goal = max(goal, count[c])
            curLen += 1
            
            if i==goal:
                res.append(curLen)
                curLen = 0
                
            i+=1
        
        return res
        