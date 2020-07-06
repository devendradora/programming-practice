'''

Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.


'''

from typing import List

class LargeNumKey(str):
	def __lt__(x,y):
		return x+y > y+x

class Solution:	
	def largestNumber(self, nums: List[int]) -> str:
		nums_str= map(str , nums) # converts each num to string
		nums_sorted = sorted(nums_str , key = LargeNumKey)
		largest_num = ''.join(nums_sorted)
		return '0' if largest_num[0] == '0' else largest_num

sol = Solution()
print(sol.largestNumber([3, 30, 34, 5, 9]))