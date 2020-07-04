# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dimensions = binaryMatrix.dimensions()
        rows= dimensions[0]
        cols= dimensions[1]
        
        if rows == 0 or cols == 0:
            return -1
        
        #Top Right 
        curr_row_index = 0 
        curr_col_index=cols-1
        one_found = False
        while curr_row_index < rows and curr_col_index >= 0:
            if binaryMatrix.get(curr_row_index,curr_col_index) == 0:
                curr_row_index+=1
            else:
                curr_col_index-=1
                one_found = True
                
        return curr_col_index + 1 if one_found else -1       
        