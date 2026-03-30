class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])
        left, right = 0, rows * columns - 1  # Total elements
        
        while left <= right:
            middle = (left + right) // 2
            # Convert 1D index to 2D coordinates
            row = middle // columns
            col = middle % columns
            
            value = matrix[row][col]
            
            if value < target:
                left = middle + 1
            elif value > target:
                right = middle - 1
            else:
                return True
        
        return False