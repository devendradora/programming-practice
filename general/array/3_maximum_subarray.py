'''
Given an integer array nums, find the contiguous subarray
 (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


'''

from typing import List
from sys import maxsize 


class Solution:
	def maxSubArray(self, nums: List[int]) -> int:        
		max_sum_cur=nums[0]
		max_sum_so_far=nums[0]        
		for i in range(1,len(nums)):          
			max_sum_cur = max(max_sum_cur + nums[i] ,nums[i])
			max_sum_so_far = max(max_sum_so_far, max_sum_cur)
		return max_sum_so_far   

	def maxSubArray_with_start_and_end_indices(self, nums: List[int]) -> int:  
		start=0
		start_temp=0
		end=0
		max_sum_cur=nums[0]
		max_sum_so_far=nums[0]
		for i in range(1,len(nums)):
			if max_sum_cur + nums[i] > nums[i]:
				max_sum_cur+=nums[i]
			else:
				max_sum_cur = nums[i]
				start_temp = i 

			if max_sum_cur > max_sum_so_far:
				max_sum_so_far = max_sum_cur 
				start = start_temp       		
				end=i

		print("start index {} - end index {} : sum-> {} ".format(start,end, max_sum_so_far))		
		return max_sum_so_far


	def maxSubArray_with_divide_and_conquer(self, nums: List[int]) -> int:
		# nlogn 
		return self.maxSubArray_with_divide_and_conquer_algo(nums,0,len(nums)-1)

	def maxSubArray_with_divide_and_conquer_algo(self, nums:List[int] , l:int , h:int)-> int:
		if l == h:
			return nums[l]

		m = (l+h) // 2
		
		#Return max of 3 cases
		# a. Max Sub array sum in left half
		# b. Max Sub array sum in right half
		# c. Max Sub array sum such that the subarray crosses the mid point

		return max(self.maxSubArray_with_divide_and_conquer_algo(nums,l,m),self.maxSubArray_with_divide_and_conquer_algo(nums,m+1,h),self.maxSubArray_crossing_sum(nums,l,m,h))	


	def maxSubArray_crossing_sum(self, nums:List[int] , l:int , m: int, h:int)-> int:
		sum=0
		left_sum_from_mid=-maxsize
		for i in range(m,l-1,-1):
			sum+=nums[i]
			left_sum_from_mid= max(left_sum_from_mid,sum)

		sum=0
		right_sum_from_mid=-maxsize
		for i in range(m+1,h+1):
			sum+=nums[i]
			right_sum_from_mid=max(right_sum_from_mid,sum)

		#returning only left_sum + right_sum will fail for [-2, 1]	
		return max(left_sum_from_mid+right_sum_from_mid, left_sum_from_mid,right_sum_from_mid) 	

sol = Solution()
nums=[-2,1,-3,4,-1,2,1,-5,4]  
nums2 = [-2, -3, 4, -1, -2, 1, 5, -3] 
nums3 = [-3,-2,-5]

print("max sub array sum -> {}".format(sol.maxSubArray_with_divide_and_conquer(nums)))







		  
	 
		  
		
			
		