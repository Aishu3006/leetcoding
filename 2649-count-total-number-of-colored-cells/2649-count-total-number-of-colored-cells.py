'''
Input - n (1<=n<=10^5)

1 1
2 5 --> 1 + 4(1)
3 13 --> 1 + 4(1) + 4(2)
4 1 + 4(1) + 4(2) + 4(3) = 25?
'''

class Solution:
    def coloredCells(self, n: int) -> int:
        if n==0:
            return 0
        
        res = 1 + 2*(n*(n-1))
        
        return res 
        