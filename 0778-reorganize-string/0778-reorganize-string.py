class Solution:
    def reorganizeString(self, s: str) -> str:
        charCounter = Counter(s)
        maxCount, letter = 0, ''

        for char, count in charCounter.items():
            if count>maxCount:
                maxCount = count
                letter = char
        
        if maxCount>(len(s)+1)//2:
            return ""
        
        index = 0
        ans = ['']*len(s)

        while charCounter[letter]!=0:
            ans[index] = letter
            index += 2
            charCounter[letter] -= 1
        
        for char, count in charCounter.items():
            while count>0:
                if index>=len(s):
                    index = 1
                ans[index] = char
                count -= 1
                index += 2
        
        return ''.join(ans)