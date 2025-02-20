class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n==0:
            return 0
        
        l = 0
        r = 0

        while r<n:
            ch = chars[r]
            count = 0

            while r<n and chars[r]==ch:
                count += 1
                r += 1
            
            chars[l] = ch
            l+=1
            if count>1:
                for d in str(count):
                    chars[l] = d
                    l+=1
        
        return l

        