'''

https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3390/

Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

 

Example 1:



Input: hour = 12, minutes = 30
Output: 165
Example 2:



Input: hour = 3, minutes = 30
Output: 75
Example 3:



Input: hour = 3, minutes = 15
Output: 7.5
Example 4:

Input: hour = 4, minutes = 50
Output: 155
Example 5:

Input: hour = 12, minutes = 0
Output: 0
 

Constraints:

1 <= hour <= 12
0 <= minutes <= 59
Answers within 10^-5 of the actual value will be accepted as correct.
   Hide Hint #1  
The tricky part is determining how the minute hand affects the position of the hour hand.
   Hide Hint #2  
Calculate the angles separately then find the difference


'''
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
    	# minute hand would cover 6 degrees in 1 min (60 min = 360 degrees => 1 min = 6 degrees)
    	# hour hand would cover 0.5 degrees in 1 min (1hr = 60 min = 30  degrees => 1 min = 0.5 degrees)
    	# 3:30 AM -> min hand 30*6 = 180 , hour hand 3*30 + 30*0.5 = 105 , diff angle = 180-105 = 75 
    	min_hand_angle = minutes*6
    	hour_hand_angle = (hour%12)*30 + minutes*0.5 
    	diff_angle = abs(min_hand_angle-hour_hand_angle)
    	return min(diff_angle,360-diff_angle)

sol = Solution()
print(sol.angleClock(3,30))   	





        
