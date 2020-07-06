'''

You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:
direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.

Example 1:
Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation: 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"
Example 2:
Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:  
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"

Constraints:
1 <= s.length <= 100
s only contains lower case English letters.
1 <= shift.length <= 100
shift[i].length == 2
0 <= shift[i][0] <= 1
0 <= shift[i][1] <= 100

'''




class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        right_dir_amt=0
        left_dir_amt = 0
        for sh in shift:
            if sh[0] == 1:
                right_dir_amt += sh[1]                
            elif sh[0] == 0:
                left_dir_amt += sh[1]
                
        
        if right_dir_amt > left_dir_amt:
            right_dir_amt-= left_dir_amt
            return self.do_right_shift(s,right_dir_amt % len(s))
        else:
            left_dir_amt -= right_dir_amt
            return self.do_left_shift(s,left_dir_amt % len(s))
        
    def do_left_shift(self,s,direction_amount):
        print("left shift ", direction_amount )
        return s[direction_amount:]+s[0:direction_amount]
    
    def do_right_shift(self,s,direction_amount):
        print("right shift ", direction_amount )
        return s[len(s)-direction_amount:]+s[0:len(s)-direction_amount]
        
        
     
        
            

            
        
                
                