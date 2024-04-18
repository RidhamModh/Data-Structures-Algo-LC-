"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def findLargestSubtreeSum(self, root : Optional['Node']) -> int:
        # code here
        self.maxtotal = float("-inf")
        def dfs(node):
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            self.maxtotal = max(self.maxtotal, (l+r+node.data))
            return (l+r+node.data)
        dfs(root)
        return self.maxtotal