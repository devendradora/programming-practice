'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs=[]
        for str in strs:
            sorted_strs.append(''.join(sorted(str)))
            
            
        final_ans_dict = {}
        for i in range(0,len(sorted_strs)):
            if not final_ans_dict.get(sorted_strs[i]):            
                final_ans_dict[sorted_strs[i]] = []
            final_ans_dict.get(sorted_strs[i]).append(strs[i]) 
         
        return [ v for v in final_ans_dict.values()]       
            
        
      
            
            
