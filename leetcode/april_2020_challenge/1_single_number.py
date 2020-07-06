'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res=nums[0]
        for i in range(1,n):
            res = res^nums[i]  # xor of 2 same elements is 0 , xor of element with 0 is element 
        return res    