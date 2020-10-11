'''
Given weights and values of n items, we need to put these items in a knapsack of capacity W
to get the maximum total value in the knapsack.

In the 0-1 Knapsack problem, we are not allowed to break items. We either take the whole item or don’t take it.
we can break items for maximizing the total value of knapsack. This problem in which we can break an item is 
also called the fractional knapsack problem.

'''




from typing import List


class KnapsackItemKey:
	def __init__(self,weight: int, value: int):
		self.weight = weight
		self.value = value
		self.cost =  self.value/self.weight

	def __lt__(self,other):
		 return self.cost > other.cost # descending order by cost

	def __repr__(self):
		return "(weight {}, value {}, cost {})".format(self.weight,self.value,self.cost)



class Solution:

	#Returns the max value that can be put in a knapsack of capacity W
	def knapsack_fractional(self, W: int, wt : List[int], val:List[int], n: int) -> int:

		items = []
		for i in range(n):
			items.append(KnapsackItemKey(wt[i],val[i]))			

		print(items)
		items.sort()
		#sorted(items,reverse=True)
		#sorted(items,key=lambda k:k.cost)
		#sorted(items,key=KnapsackItemKey)
		print(items)
		max_value_of_items_in_knapsack=0
		for i in range(len(items)):
			diff = W-items[i].weight
			if diff >=0:
				W=W-items[i].weight
				max_value_of_items_in_knapsack+=items[i].value
			else:
				max_value_of_items_in_knapsack+=items[i].cost*abs(diff)
				break

		return max_value_of_items_in_knapsack		







		


sol = Solution()

W=6
wt=[1,2,3]
val =[10,15,40]

W2=8
wt2=[2,2,4,5]
va2=[2,4,6,9]

wt = [10, 40, 20, 30]
val = [60, 40, 100, 120] 
W = 50

print(sol.knapsack_fractional(W,wt,val,len(wt)))