'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i,j=0,0
        cur_sum=nums[0]
        max_sum=nums[0]
        
        for k in range(1,len(nums)):          
            cur_sum = max(cur_sum + nums[k] ,nums[k])
            max_sum = max(max_sum, cur_sum)
        return max_sum    
          
        
            
        