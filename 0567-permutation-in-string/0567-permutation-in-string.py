class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2:
            return False 
        
        s1_counter = Counter(s1)
        window_counter = Counter(s2[:len(s1)])
        
        for r in range(len_s1,len_s2):
            if s1_counter == window_counter:
                return True
            
            window_counter[s2[r-len_s1]] -= 1
            window_counter[s2[r]] += 1
        
        return s1_counter==window_counter
        