# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def getMaxRob(currnode):
            if not currnode:
                return 0
            
            if currnode in memo:
                return memo[currnode]

            rob_curr = currnode.val
            
            if currnode.left:
                rob_curr += (
                    getMaxRob(currnode.left.left) +
                    getMaxRob(currnode.left.right)
                )
            
            if currnode.right:
                rob_curr += (
                    getMaxRob(currnode.right.left) +
                    getMaxRob(currnode.right.right)
                )
            
            skip_curr = getMaxRob(currnode.left) + getMaxRob(currnode.right)
            
            memo[currnode] = max(rob_curr, skip_curr)
            return memo[currnode]
        
        return getMaxRob(root)