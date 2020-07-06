'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 3 * 10^4
0 <= nums[i][j] <= 10^5

'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_jump_index = 0 
        for i in range(0,len(nums)-1):
            if i + nums[i] > max_jump_index:
                max_jump_index = i + nums[i]
                
            if max_jump_index == i:
                break
                
        return max_jump_index >= len(nums)-1
            
        
                
            
        
