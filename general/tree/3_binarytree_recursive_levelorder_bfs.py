'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
	3
   / \
  9  20
	/  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]


Time Complexity: O(n^2) in worst case. For a skewed tree, printGivenLevel() takes O(n) time where n is the number of nodes 
in the skewed tree. So time complexity of printLevelOrder() is O(n) + O(n-1) + O(n-2) + .. + O(1) which is O(n^2).
Space Complexity: O(n) in worst case. For a skewed tree, printGivenLevel() uses O(n) space for call stack. 
For a Balanced tree, call stack uses O(log n) space, (i.e., height of the balanced tree).

'''

from typing import List
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:	
	def __init__(self):
		self.each_level_list=[]
	

	def levelOrder(self, root: TreeNode) -> List[List[int]]:
		level_order_multi_list=[]
		h = self.height(root)
		print("height {}".format(h))
		for l in range(1,h+1):
			self.each_level_list=[]
			level_order_multi_list.append(self.levelOrder_each_level(root,l))

		return level_order_multi_list	



	def levelOrder_each_level(self, root: TreeNode, level : int) -> List[int]:
		if root is None:
			return

		if level == 1 :
			self.each_level_list.append(root.val)			
		elif level > 1:
			self.levelOrder_each_level(root.left, level-1)
			self.levelOrder_each_level(root.right, level-1)

		return self.each_level_list
		


	def height(self, root : TreeNode)-> int:
		if root is None:
			return 0 # height is assumed as same as no. of levels
		return 1+max(self.height(root.left),self.height(root.right))	



sol = Solution()

root = TreeNode(3,TreeNode(9),TreeNode(20))
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(sol.levelOrder(root))
					



