'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

Time complextiy : O(n)

Space complexity : O(1)

'''

from typing import *


class Solution:
	def removeDuplicates(self,arr: List[int]) -> int :		
		n=len(arr)
		if n==0 or n==1:
			return n
		j=0
		for i in range(0,n-1):
			if arr[i] != arr[i+1]:
				arr[j]=arr[i]
				j+=1


		arr[j]=	arr[n-1]
		j+=1
		return j		


arr=[1,1,2]
sol = Solution()
print("length after removing duplicates {}".format(sol.removeDuplicates(arr)))