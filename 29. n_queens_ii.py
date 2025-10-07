# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

# Example 1:


# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 9

# Solution: Backtracking
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def backtrack(row, diagonals, anti_diagonals, cols):
            if row == n:
                return 1
            
            count = 0
            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                
                if (col in cols or 
                    curr_diagonal in diagonals or 
                    curr_anti_diagonal in anti_diagonals):
                    continue
                
                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                
                count += backtrack(row + 1, diagonals, anti_diagonals, cols)
                
                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
            
            return count
        
        return backtrack(0, set(), set(), set())
    
# Solution 2: Bit Manipulation
class SolutionBit(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def backtrack(row=0, hills=0, next_row=0, dales=0):
            if row == n:
                return 1
            
            count = 0
            free_columns = ((1 << n) - 1) & ~(hills | next_row | dales)
            
            while free_columns:
                curr_column = -free_columns & free_columns
                free_columns ^= curr_column
                
                count += backtrack(row + 1, 
                                   (hills | curr_column) << 1, 
                                   next_row | curr_column, 
                                   (dales | curr_column) >> 1)
            return count
        
        return backtrack()