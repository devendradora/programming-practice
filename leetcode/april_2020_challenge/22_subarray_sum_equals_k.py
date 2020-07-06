'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
 

Constraints:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 0 :
            return 0
        
        num_of_contigious_sub_arrays=0
        cur_sum=0
        prefix_sum_count_map = {}
        
        for i in range(0,len(nums)):
            cur_sum+=nums[i]            
            if cur_sum == k:
                num_of_contigious_sub_arrays+=1
                
            if cur_sum - k in  prefix_sum_count_map:
                num_of_contigious_sub_arrays += prefix_sum_count_map[cur_sum-k] 
                
                
            if cur_sum in prefix_sum_count_map:
                prefix_sum_count_map[cur_sum]+=1
            else:
                prefix_sum_count_map[cur_sum]=1
                
        return  num_of_contigious_sub_arrays       
                
            
            
            
        