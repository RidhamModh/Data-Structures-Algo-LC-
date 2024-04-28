#User function Template for python3

class Solution:
    #Your task is to complete this function
    #function should return True/False or 1/0
    def check(self, root):
        #Code here
        self.leafHeight = -1
        def dfs(node, height):
            if not node:
                return True
            
            if not node.left and not node.right:
                if self.leafHeight!=-1 and self.leafHeight!=height:
                    return False
                else:
                    self.leafHeight= height
                    return True
            
            l = dfs(node.left, height+1)
            r = dfs(node.right, height+1)

            if l and r:
                return True
            return False
        return dfs(root,0)