# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if root == None: return len(arr) == 0
        return self.checkPath(root,arr,0)
            
        
    def checkPath(self,root:TreeNode, arr: List[int],index: int) -> bool :
        if root.val != arr[index] : return False
        
        if index == len(arr)-1:
            return root.left == None and root.right == None
        
        return ( (root.left != None and self.checkPath(root.left,arr,index+1)) or (root.right != None and self.checkPath(root.right,arr,index+1)))
        
        
        