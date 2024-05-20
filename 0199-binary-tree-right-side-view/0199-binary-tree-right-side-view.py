# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        res = []
        
        if root:
            q.append(root)
            
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightSide = node
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            if rightSide:
                res.append(rightSide.val)
            
        return res
        