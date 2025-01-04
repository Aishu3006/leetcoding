class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagramGroups = defaultdict(list)

        for s in strs:
            charArray = [0]*26
            for c in s:
                charArray[ord(c)-ord("a")] += 1
            anagramGroups[tuple(charArray)].append(s)
        
        return list(anagramGroups.values())
                
                
                
        