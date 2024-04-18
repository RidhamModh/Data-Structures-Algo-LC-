'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def sumOfLongRootToLeafPath(self,root):
        #code here
        def dfs(node):
            
            if not node:
                return (0,0)
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            if l[0] > r[0]:
                return (l[0]+1, l[1]+node.data)
            elif r[0] > l[0]:
                return (r[0]+1, r[1]+node.data)
            else:
                return (l[0]+1, max(l[1],r[1])+node.data)
        ans = dfs(root)
        return ans[1]