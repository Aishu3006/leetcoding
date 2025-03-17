class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        minLen = min(len(s) for s in strs)

        for i in range(minLen):
            c = strs[0][i]

            for s in strs:
                if s[i]!=c:
                    return strs[0][:i]
        
        return strs[0][:minLen]


        '''
        if not strs:
            return ""

        #The maximum a prefix can be amongst all 
        minLen = min(len(s) for s in strs)

        for i in range(minLen):
            c = strs[0][i]

            for s in strs:
                if s[i]!=c:
                    return strs[0][:i]
        
        return strs[0][:minLen]
        '''