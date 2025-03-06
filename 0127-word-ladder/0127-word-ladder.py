class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if(endWord not in wordList 
        or not beginWord
        or not endWord
        or not wordList
        ):
            return 0
        
        n = len(beginWord)
        
        betweenwordToWords = defaultdict(list)
        for word in wordList:
            for i in range(n):
                betweenWord = word[:i]+"*"+word[i+1:]
                betweenwordToWords[betweenWord].append(word)
        
        q = collections.deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)

        while q:

            currentWord, level = q.popleft()

            for i in range(n):
                betweenWord = currentWord[:i] + "*" + currentWord[i+1:]

                for word in betweenwordToWords[betweenWord]:
                    if word == endWord:
                        return level+1
                    
                    if word not in visited:
                        visited.add(word)
                        q.append((word,level+1))
                
                betweenwordToWords[betweenWord] = []


        return 0