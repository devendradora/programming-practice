'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.pivotedBinarySearch(nums,0,len(nums)-1, target)
        
        
    def pivotedBinarySearch(self,nums,low,high,target):
        
        if low > high:
            return -1
        
        mid = (low+high) // 2
        
        if target == nums[mid] :
            return mid
        
        # First sub-array is sorted
        if nums[low] <= nums[mid]:
            if target <= nums[mid] and target >= nums[low]:
                return self.pivotedBinarySearch(nums,low,mid-1,target)
            else:
                return self.pivotedBinarySearch(nums,mid+1,high,target)
        else:
            # if first sub array is not sorted , 2nd sub array must be sorted
            if target >= nums[mid] and target <= nums[high]:
                return self.pivotedBinarySearch(nums,mid+1,high,target)
            else:
                return self.pivotedBinarySearch(nums,low,mid-1,target)

                
                
            
        
            
                
        
        
        
        
        
        