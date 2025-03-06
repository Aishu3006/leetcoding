class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        charMap = {}
        l = 0
        maxLen = 0

        for r in range(len(s)):

            charMap[s[r]] = 1 + charMap.get(s[r], 0)

            while len(charMap)>2:
                charMap[s[l]] -= 1
                if charMap[s[l]] == 0:
                    del charMap[s[l]]
                l += 1
                
            maxLen = max(maxLen, r-l+1)
            

        return maxLen
        