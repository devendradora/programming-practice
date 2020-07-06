'''
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 

Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
The values of preorder are distinct.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        return self.constructBST(preorder,0,len(preorder)-1)
    
    
    def constructBST(self,preorder,l,r):
        if l > r :
            return None
        root = TreeNode(preorder[l])
        
        if l == r :
            return root
        
        i=l+1
        
        while i <= r and preorder[i] < preorder[l]:
            i += 1
            
        root.left = self.constructBST(preorder,l+1,i-1)
        root.right = self.constructBST(preorder,i,r)
        
        return root
        
        
        
            
        
