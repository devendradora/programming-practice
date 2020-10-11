'''
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3377/

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.


solution:
Find the maximum ksuch that k (k + 1)/2 <= N 

k(k+1)/2 = N
K^2+k=2N
(k+1/2)^2-1/4=2N
k=sqrt(2N+1/4)-1/2

'''


class Solution:
    def arrangeCoins(self, n: int) -> int:
        sum,i=0,0
        while sum < n:
            i+=1
            sum+=i         
            
        return i if sum == n else i-1 


    def arrangeCoins2(self, n: int) -> int:
    	#T: O(1) , S: O(1)
        return int((2*n+0.25)**0.5 - 0.5)      


sol = Solution()
print(sol.arrangeCoins2(5))
