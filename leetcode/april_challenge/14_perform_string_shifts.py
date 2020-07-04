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
        
    def do_left_shift(self,s,direction):
        print("left shift ", direction )
        return s[direction:]+s[0:direction]
    
    def do_right_shift(self,s,direction):
        print("right shift ", direction )
        return s[len(s)-direction:]+s[0:len(s)-direction]
        
        
     
        
            

            
        
                
                