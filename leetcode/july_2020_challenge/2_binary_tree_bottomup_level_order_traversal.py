'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

'''
from typing import List
from collections import deque 
 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    	if root is None:
    		return
    	queue=deque()
    	queue.append(root)
    	queue.append(TreeNode('|'))

    	stack=deque()

    	level_row =[]	
    	while len(queue) > 0:
    		temp = queue.popleft()
    		if temp.val == '|':
    			if len(queue) >0:
    				queue.append(temp)
    			stack.append(level_row)
    			level_row=[]
    		else:
    			level_row.append(temp.val)
    			if temp.left:
    				queue.append(temp.left)
    			if temp.right:
    				queue.append(temp.right)	

    	level_order_bottom_up = []  
    	while len(stack) > 0:    		 		
    		level_order_bottom_up.append(stack.pop())    			

    	return level_order_bottom_up		


sol = Solution()

root = TreeNode(3,TreeNode(9),TreeNode(20))
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(sol.levelOrderBottom(root))

