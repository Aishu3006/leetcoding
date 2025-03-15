class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxLen = 0

        def checkPalindrome(l,r):
            nonlocal res, maxLen 

            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > maxLen:
                    maxLen = r-l+1
                    res = s[l:r+1]
                
                l -= 1
                r += 1

        for i in range(len(s)):

            #odd length
            checkPalindrome(i,i)

            #even length
            checkPalindrome(i,i+1)
        
        return res