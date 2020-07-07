'''
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
 

Example 2:


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
 

Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Each value on each linked list is in the range [1, 10^9].
Your code should preferably run in O(n) time and use only O(1) memory.

'''


# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
		# T: O(m+n) , S : O(1)
		pA = headA
		pB = headB
		
		while pA != pB:
			if pA == None: # change pointer to another list node head on reaching end
				pA = headB
			else:
				pA=pA.next
				
			if pB == None:
				pB= headA
			else:
				pB= pB.next
				
		return pA        
				
	def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
		pA = headA
		lenA = 0
		while pA != None:
			lenA+=1
			pA = pA.next
			
		pB = headB
		lenB=0
		while pB !=None:
			lenB+=1
			pB = pB.next
			
		diff = lenA - lenB
		
		count=0
		pA= headA
		pB= headB
		#Traverse upto diff of more sized linked list 
		if diff > 0:                                   
			while count < diff:
				pA = pA.next
				count+=1

		else:
			while count < diff:
				pB= pB.next
				count+=1
				
				
		while pA != None :
			if pA == pB:
				return pA

			pA=pA.next
			pB=pB.next
		 
		return pA 


sol = Solution()

# listA = [1,9,1,2,4], listB = [3,2,4]
temp = ListNode(2)
temp.next = ListNode(4)


headA = ListNode(1)
headA.next = ListNode(9)
headA.next.next = ListNode(1)
headA.next.next.next = temp
# headA.next.next.next = ListNode(2)
# headA.next.next.next.next = ListNode(4)

headB = ListNode(3)
headB.next = temp
# headB.next = ListNode(2)
# headB.next.next = ListNode(4)

#[8] ,[4,1,8,4,5]
headC = ListNode(8)
headD = ListNode(4)
headD.next = ListNode(1)
headD.next.next = headC
headD.next.next.next = ListNode(4)
headD.next.next.next.next = ListNode(5)



print(sol.getIntersectionNode(headC,headD).val)    	



