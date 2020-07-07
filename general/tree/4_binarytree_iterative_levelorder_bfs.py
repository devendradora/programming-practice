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


'''

from typing import List
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:	
	def levelOrder(self, root: TreeNode) -> List[List[int]]:
		if root is None:
			return 

		level_order_multi_list=[]
		each_level_list=[]

		queue = []
		queue.append(root)
		queue.append(TreeNode('|')) # | denotes each level ending


		while len(queue) > 0 :
			temp = queue.pop(0)

			if temp.val == '|':
				if len(queue) > 0 :
					queue.append(temp)
				level_order_multi_list.append(each_level_list)
				each_level_list=[]
			else:				
				each_level_list.append(temp.val)
				if temp.left is not None:
					queue.append(temp.left)
				if temp.right is not None:
					queue.append(temp.right)

		return level_order_multi_list		


sol = Solution()

root = TreeNode(3,TreeNode(9),TreeNode(20))
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(sol.levelOrder(root))

					



