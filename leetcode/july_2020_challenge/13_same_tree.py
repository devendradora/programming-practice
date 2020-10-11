'''

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false


'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    	#Both empty
    	if p is None and q is None:
    		return True  	 
    	#Both non-empty	
    	if p and q :
    		return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) 
    		return True    		
    	else:
    		return False# one empty and other non-empty			
	



sol = Solution()
p = TreeNode(1,TreeNode(2),TreeNode(3))
q = TreeNode(1,TreeNode(2),TreeNode(3))


p = TreeNode(1,TreeNode(2),None)
q = TreeNode(1,None,TreeNode(2))

print(sol.isSameTree(p,q))   	
