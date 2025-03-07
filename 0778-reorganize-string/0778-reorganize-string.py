class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []

        pq =[(-count, char) for char,count in Counter(s).items()]
        heapify(pq)

        while pq:
            firstCharCount, firstChar = heappop(pq)

            if not ans or ans[-1]!=firstChar:
                ans.append(firstChar)
                if firstCharCount+1!=0:
                    heappush(pq, (firstCharCount+1, firstChar))
            
            else:
                if not pq: return ""
                secondCharCount, secondChar = heappop(pq)
                ans.append(secondChar)
                if secondCharCount+1!=0:
                    heappush(pq, (secondCharCount+1, secondChar))
                heappush(pq, (firstCharCount, firstChar))

        return ''.join(ans)
                
        