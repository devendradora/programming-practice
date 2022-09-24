'''https://www.youtube.com/watch?v=sVAB0p58tlg

Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value 
in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values 
and weights associated with n items respectively. Also given an integer W which represents knapsack capacity,
find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than 
or equal to W. You cannot break an item, either pick the complete item or don’t pick it (0-1 property).


Note : You can also think of a problem , thief has a bag of capacity W to hold items. He wants to pick combintation of
items that gives him highest profit but combination weight should be less than or equal to W 

eg Knapsack capacity W=8,  4 items with weights 2,2,4,5 with values 2,4,6,9 respectively


eg. Knapsack capacity W=6,  3 items with weights 1,2,3 with values 10,15.40 respectively

DP bottom up
val	wt   	W------>
 |	|  		0   1   2   3   4   5   6
 |  |
 V	V
 0	0  		0   0   0   0   0   0   0

10	1 		0  10  10  10  10  10  10

15	2  		0  10  15  25  25  25  25

40	3  		0  10  15  40  50  55  65


if i==0 or w == 0 :
	dp[i][w] = 0
elif wt[i-1] > w : # u can't pick current item, then pick all items picked before that has given highest value until now
	dp[i][w] = dp[i-1][w]	
else:
	dp[i][w] = max(val[i-1]+dp[i-1][w-wt[i-1]], dp[i-1][w])


 [0,  0, 0,  0,   0,  0, 0], 
 [0, 10, 10, 10, 10, 10, 10],
 [0, 10, 15, 25, 25, 25, 25],
 [0, 10, 15, 40, 50, 55, 65]





'''


from typing import List

class Solution:

	#Returns the max value that can be put in a knapsack of capacity W
	def knapsack_recursion(self, W: int, wt : List[int], v:List[int], n: int) -> int:
		#T: O(2^n) , S: O(n)
		if  n == 0 or W == 0 :
			return 0

		#If weight of nth item is more than knapsack capacity W, this item can't be included in optimal sol	
		if wt[n-1] > W:
			return self.knapsack_recursion(W,wt,val,n-1)
		else:
			#max(nth item included in bag, nth item excluded from bag)	
			return max(val[n-1]+self.knapsack_recursion(W-wt[n-1], wt, val,n-1),self.knapsack_recursion(W,wt,val,n-1))


	def knapsack_dp_topdown(self, W: int, wt : List[int], val:List[int], n: int, dp_top_down_memorization: List[List]) -> int:
		#T: O(n*W) , S: O(n*W)
		if  n == 0 or W == 0 :
			return 0

		if dp_top_down_memorization[n][W] != -1:
			return knapsack_dp_topdown[n][W] # return memorized result	

		#If weight of nth item is more than knapsack capacity W, this item can't be included in optimal sol	
		if wt[n-1] > W:
			dp_top_down_memorization[n][W] = self.knapsack_dp_topdown(W,wt,val,n-1,dp_top_down_memorization)
		else:
			#max(nth item included in bag, nth item excluded from bag)	
			dp_top_down_memorization[n][W] = max(val[n-1]+self.knapsack_dp_topdown(W-wt[n-1], wt, val,n-1,dp_top_down_memorization),self.knapsack_dp_topdown(W,wt,val,n-1,dp_top_down_memorization))
	
		return dp_top_down_memorization[n][W]	

		

	def knapsack_dp_bottom_up(self, W: int, wt : List[int], val:List[int], n: int) -> int:
		#T: O(n*W) As for every weight element we traverse through all weight capacities 1<=w<=W.
		#S: O(n*W)
		# consider all the possible weights from 0 to W as columns  and the input item weights as rows
		dp = [[0]*(W+1) for _ in range(n+1)]
		for i in range(n+1):
			for w in range(W+1):
				if i==0 or w == 0 :
					dp[i][w] = 0
				elif wt[i-1] > w :
					dp[i][w] = dp[i-1][w]	
				else:
					dp[i][w] = max(val[i-1]+dp[i-1][w-wt[i-1]], dp[i-1][w])
		print(dp)			
		return dp[n][W]				
							


sol = Solution()

W=6
wt=[1,2,3]
val =[10,15,40]

W2=8
wt2=[2,2,4,5]
va2=[2,4,6,9]


print(sol.knapsack_recursion(W,wt,val,len(wt)))
print(sol.knapsack_dp_bottom_up(W,wt,val,len(wt)))

dp_top_down_memorization = [[-1]*(W+1) for _ in range(len(wt)+1)] 
print(sol.knapsack_dp_topdown(W,wt,val,len(wt),dp_top_down_memorization))


