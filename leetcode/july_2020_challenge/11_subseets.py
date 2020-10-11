'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

no. of unique sets [each no. can be choosen (1) or not (0)] = 2^N =2^3 = 8

https://leetcode.com/articles/subsets/

'''
from typing import List

class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		power_set=[[]]  

		for num in nums:
			#append nums[i] to all existing subsets 
			new_subsets=[]
			print(" process ----")
			for entry in power_set:
				print("set {}".format(entry))	
				new_subsets.append(entry.append(num))
			print("new subsets {}".format(new_subsets))		
			for entry in new_subsets:
				power_set.append(entry)
			print("power set {}".format(power_set))	
				

		return power_set


sol = Solution()
nums=[1,2,3]
print(sol.subsets(nums))   			



		
