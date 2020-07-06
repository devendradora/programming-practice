'''

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3

Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.



Proof
Proving that at least one duplicate must exist in nums is simple application of the pigeonhole principle. 
Here, each number in nums is a "pigeon" and each distinct number that can appear in nums is a "pigeonhole". 
Because there are n+1n+1 numbers are nn distinct possible numbers, the pigeonhole principle implies that at 
least one of the numbers is duplicated.

https://leetcode.com/articles/find-the-duplicate-number/ (very imp)

'''

from typing import List

class Solution:

	def findDuplicate(self, nums:List[int]) -> int :
		# T:O(n) , S: O(1)
		# Linked List with cycle is formed if duplicate number exists
		# Find the intersection point of 2 runners
		tortoise = hare = nums[0]
		while True:
			tortoise= nums[tortoise]
			hare = nums[nums[hare]]
			if tortoise == hare:
				break

		#Find the entrance of cycle
		tortoise = nums[0]
		while tortoise != hare :
			tortoise = nums[tortoise]
			hare = nums[hare]

		return tortoise	



	def findDuplicate2(self, nums:List[int]) -> int :
		# T:O(n) , S: O(1) , but by constraint array should n't be modified
		n = len(nums)
		for i in range(0,n):
			nums[nums[i]%n]+=n

		for i in range(0,n):
			if nums[i] >= 2*n:
				return i

			

	def findDuplicate3(self, nums:List[int]) -> int :
		# T : O(n) , S : O(n) but by constraints space complexity allowed is O(1)
		seen_set = set()
		for num in nums:
			if num in seen_set:
				return num
			else:
				seen_set.add(num)	


	def findDuplicate4(self, nums:List[int]) -> int :
		# T : nlog(n) , S : O(1) if nums sorted inplace , if we copy nums to new array , then S is O(n) , 
		# but by constraints space complexity allowed is O(1)
		nums.sort()
		for i in range(0,len(nums)-1):
			if nums[i] == nums[i+1]:
				return nums[i]



sol = Solution()
print(sol.findDuplicate([3,1,3,4,2]))


