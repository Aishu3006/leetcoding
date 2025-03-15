class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        ans = 0

        while l<r:
            if leftMax<rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                ans += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                ans += rightMax - height[r]
        
        return ans 
        '''

        l,r = 0, len(height)-1
        leftMax = height[l]
        rightMax = height[r]
        res = 0
        
        while l<r:
            
            #left less than right
            if leftMax<rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
                
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res
        '''