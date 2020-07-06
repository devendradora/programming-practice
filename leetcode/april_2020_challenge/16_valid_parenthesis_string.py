'''
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].

'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        min_bracket= max_bracket =0
        for c in s:
            min_bracket += 1 if c == '(' else -1
            max_bracket += 1 if c != ')' else -1
            if max_bracket < 0 : break
            min_bracket = max(min_bracket,0)  
            
        return min_bracket == 0        
        