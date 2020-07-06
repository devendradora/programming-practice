from collections import OrderedDict

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.s=set()
        self.od= OrderedDict()
        
        for i in nums:
            self.add(i)
        

    def showFirstUnique(self) -> int:
        if len(self.od) == 0 : return -1
        else:
            for i in self.od:
                return i
        

    def add(self, value: int) -> None:
        if value not in self.s:
            self.s.add(value)
            self.od[value]=None
        else:
            self.od.pop(value,None)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)