class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)

        if s1_len>s2_len:
            return False
        
        s1_counter = Counter(s1)
        window_counter = Counter(s2[:s1_len])

        for i in range(s1_len, s2_len):

            if s1_counter==window_counter:
                return True

            window_counter[s2[i-s1_len]] -= 1
            window_counter[s2[i]] += 1
        
        return s1_counter==window_counter
            
        