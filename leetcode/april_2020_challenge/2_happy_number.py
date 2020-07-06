'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and
repeat the process until the number equals 1 (where it will stay), or 
it loops endlessly in a cycle which does not include 1.
 Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1



'''


class Solution:
    def isHappy(self,n: int) -> bool:
        set_seen = set()
        while n != 1:
            sum=0
            while n != 0:
                r = n % 10 
                sum+= r**2
                n=n//10 

            if sum in set_seen:
                return False
            else:
                n=sum
                set_seen.add(sum)
        return True 

    def isHappy2(self, n: int) -> bool:
        isHappy = False
        while not isHappy:
            sum=0
            for i in str(n):
                sum+=int(i)**2
            if sum == 1:
                return True
            elif sum == 4:  # observation, the number is never happy when sum is 4 or store all sums in set , if any new sum equals any sum in set, then return false 
                return False
            else:
                n=sum                
        return IsHappy  


           


sol =  Solution()
print("is happy {}".format(sol.isHappy2(19)))            

           
                    


               
        
        
        