# Set Matrix Zeroes
# Difficulty: Medium
# Platform: LeetCode

from typing import List

def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    
    # Find which positions need to be 0'd out
    # Account for the first row
    # Set the marked positions to 0
    
    row, col = len(matrix), len(matrix[0])
    # Set to true if the first row is a zero
    rowZero = False
    
    # Determine the positions we need to 0 out using the 'outside edge' of the matrix
    for r in range(row):
        for c in range(col):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else: 
                    rowZero = True
    
    # 0 out the matrix besides the first row/col that we're using for tracking
    for r in range(1, row):
        for c in range(1, col):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
    
    # 0 out the first col if needed
    if matrix[0][0] == 0:
        for r in range(row):
            matrix[r][0] = 0
            
    # Finally, 0 out the first row if needed
    if rowZero:
        for c in range(col):
            matrix[0][c] = 0
            
    print(matrix)
            
if __name__ == "__main__":
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print(setZeroes(matrix))
    
    # Answer should be [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]