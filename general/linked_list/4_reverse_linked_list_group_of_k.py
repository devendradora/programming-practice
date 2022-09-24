'''
Given a linked list, write a function to reverse every k nodes (where k is an input to the function). 

Example: 

Input: 1->2->3->4->5->6->7->8->NULL, K = 3 
Output: 3->2->1->6->5->4->8->7->NULL 
Input: 1->2->3->4->5->6->7->8->NULL, K = 5 
Output: 5->4->3->2->1->8->7->6->NULL 


'''


class ListNode:
	def __init__(self, val= None, next=None):
		self.val = val
		self.next = next

class Solution:
	def create_linked_list_from_list(self,l):
		head = None
		if len(l)>0:
			head = ListNode(l[0])

		node = head
		for i in range(1,len(l)):
			node.next = ListNode(l[i])
			node = node.next
		return head
	
	def reverseListKGroup(self, head: ListNode, k) -> ListNode:
		#T: O(n) , S: O(1)
		prev_node = None
		cur_node = head
		count = 0

		while cur_node is not None and count < k :
			next_node = cur_node.next
			cur_node.next = prev_node
			prev_node = cur_node
			cur_node = next_node
			count += 1
		
		if next_node is not None:
			head.next = self.reverseListKGroup(next_node , k)
		
		return prev_node

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
			print(head.val,"->"),
			head = head.next

sol = Solution()
head = sol.create_linked_list_from_list([1,2,3,4,5,6,7,8,9,10])
sol.printList(head)
print("====")
new_head = sol.reverseListKGroup(head, 4)
sol.printList(new_head)

# 1,2,3,4,5,6,7,8,9,10
# 4,3,2,1,8,7,6,5,10,9


