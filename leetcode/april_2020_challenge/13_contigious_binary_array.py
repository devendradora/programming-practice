'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.

O(n) appoach is very good

num2= [0 ,0, 1, 0, 0 ,0, 1, 1]
      -1 -2 -1 -2 -3 -4 -3 -2  index : (2,7) max length 6


'''

from typing import List

class Solution:
	def findMaxLength(self, nums: List[int]) -> int:		
		count=0
		max_len_sub_array=0
		count_2_array_index={}
		count_2_array_index[count]=-1
		start_i,end_i=0,0
		for i in range(0,len(nums)):
			count += (-1 if nums[i] == 0 else 1)
			if count in count_2_array_index:
				if max_len_sub_array < i-count_2_array_index[count]:
					max_len_sub_array = i-count_2_array_index[count]
					start_i = count_2_array_index[count]+1
					end_i = i
			else:	
				count_2_array_index[count]=i

		print("start index {} - end index {} max length {}".format(start_i,end_i,max_len_sub_array))			
		return max_len_sub_array			

			    	

		

	def findMaxLength2(self, nums: List[int]) -> int:
		max_len_sub_array=0
		start_i,end_i=0,0
		for start in range(0,len(nums)):
			zeros,ones=0,0
			for end in range(start,len(nums)):
				if nums[end] == 0:
					zeros+=1
				else:
					ones+=1
				if zeros == ones:
					if max_len_sub_array < end-start+1:
						max_len_sub_array = end-start+1
						start_i = start
						end_i = end

		print("start index {} - end index {} max length {}".format(start_i,end_i,max_len_sub_array))				
		return max_len_sub_array	

sol = Solution()
num=[0,1,0]
num2= [0 ,0, 1, 0, 0 ,0, 1, 1]
# O(n) approach    -1 -2 -1 -2 -3 -4 -3 -2  index : (2,7) max length 6
print(sol.findMaxLength(num2))   		
						

