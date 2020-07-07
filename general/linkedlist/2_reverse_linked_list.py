'''
https://leetcode.com/problems/reverse-linked-list/

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?


'''


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def reverseList(self, head: ListNode) -> ListNode:
		#T: O(n) , S: O(1)
		prev_node = None
		cur_node = head

		while cur_node is not None:
			next_node = cur_node.next
			cur_node.next = prev_node
			prev_node = cur_node
			cur_node = next_node

		return prev_node

	def reverseList_recursive(self, head: ListNode) -> ListNode:
		#T: O(n) , S: O(n) The extra space comes from implicit stack space due to recursion. 
		#The recursion could go up to n levels deep	, head is not None condition is required if empty list is passed	
		if head is not None and head.next is not None:
			head_new = self.reverseList_recursive(head.next) # return value assigned to head_new so that it is retained upto the base method call
			head.next.next = head
			head.next = None # it is optional for all nodes, but mandatory for first node's next pointer to second node should be None, otherwise it would be cyclic
			return head_new
		else:
			return head	
	

	def printList(self, head: ListNode)->None:        
		while head is not None:
			print(head.val," "),
			head = head.next

sol = Solution()
li = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))) 
print("main list")
sol.printList(li)


print("reversed list")
reverse_li = sol.reverseList_recursive(li) 
sol.printList(reverse_li) 
  


