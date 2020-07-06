'''
Last Stone Weight

Solution
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 

Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000


heapq - min heap

heapify – This function converts a regular list to a heap. In the resulting heap the smallest element gets pushed to the index position 0. But rest of the data elements are not necessarily sorted.
heappush – This function adds an element to the heap without altering the current heap.
heappop – This function returns the smallest data element from the heap.
heapreplace – This function replaces the smallest data element with a new value supplied in the function.

'''
from typing import List
from heapq import heapify,heappush,heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        heapify(heap)
        
        for stone in stones:
            heappush(heap,-1*stone)
            
        
        heap_size = len(stones)

        while heap_size > 1 :            
            max_first= heappop(heap)
            max_second = heappop(heap)


            diff = max_first - max_second
            if diff != 0:
                heappush(heap, diff)
                heap_size-=1
            else:
                heap_size-=2
                
        if heap_size == 0:
            return 0
        else:
            return -1*heappop(heap)



sol = Solution()                
print(sol.lastStoneWeight([2,7,4,1,8,1]))               

        
        
        
        
        
        