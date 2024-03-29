'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if root is None:
            return -math.inf
        
        self.h=-math.inf
        p_lsubtree = self.maxPathSum(root.left)
        h_lsubtree = self.h
        
        self.h = -math.inf        
        p_rsubtree = self.maxPathSum(root.right)
        h_rsubtree = self.h
        
        self.h = max(max(h_lsubtree,h_rsubtree),0)+root.val
        
        return max(max(h_lsubtree,0)+max(h_rsubtree,0)+root.val,max(p_lsubtree,p_rsubtree))
    
    
   
        
        

