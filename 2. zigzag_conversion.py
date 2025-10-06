# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rType: str
        """
        if numRows == 1:
            return s
        
        result = []
        n = len(s)
        cycle = 2 * numRows - 2

        for i in range(numRows):
            j = i
            while j < n:
                result.append(s[j])
                if i != 0 and i != numRows - 1:
                    k = j + cycle - 2 * i
                    if k < n:
                        result.append(s[k])
                j += cycle

        return ''.join(result)
