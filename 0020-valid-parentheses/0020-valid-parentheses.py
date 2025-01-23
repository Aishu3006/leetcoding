class Solution:
    def isValid(self, s: str) -> bool:
        charMap = {')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if char in charMap and stack:
                prev = stack[-1]
                if charMap[char]==prev:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return not stack


        