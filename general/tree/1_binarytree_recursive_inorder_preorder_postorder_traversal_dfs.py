'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
	\
	 2
	/
   3

inOrder  : [1,3,2]
preOrder : [1,2,3]
postOrder: [3,2,1]


Input :
		   1
		 /   \
        2     3
       / \
      4   5





'''

from typing import List

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:		
	#output_list = []
	def __init__(self):
		self.output_list = []

	def inorderTraversal(self, root: TreeNode) -> List[int]:
		if root == None:
			return None

		self.inorderTraversal(root.left)
		self.output_list.append(root.val)
		self.inorderTraversal(root.right)

		return self.output_list

	def preorderTraversal(self, root: TreeNode) -> List[int]:
		if root == None:
			return None

		self.output_list.append(root.val)
		self.preorderTraversal(root.left)
		self.preorderTraversal(root.right)

		return self.output_list
		
	def postorderTraversal(self, root: TreeNode) -> List[int]:
		if root == None:
			return None

		self.postorderTraversal(root.left)
		self.postorderTraversal(root.right)
		self.output_list.append(root.val)


		return self.output_list		

root = TreeNode(1,None,TreeNode(2))
root.right.left=TreeNode(3)


sol = Solution()
print("inorder ",sol.inorderTraversal(root)) 

sol = Solution()   
print("preorder ",sol.preorderTraversal(root)) 

sol = Solution()
print("postorder ",sol.postorderTraversal(root))    	



		