class Solution:
    def countElements(self, a: List[int]) -> int:
        s = set(a)
        c = 0
        for e in a:
            if e+1 in s:
                c+=1
        return c