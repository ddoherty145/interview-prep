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
