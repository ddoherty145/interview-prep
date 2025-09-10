# 38. Count and Say
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
# which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of
# groups so that each group is a contiguous section all of the same character.
# Then for each group, say the number of characters, then say the character.
# To convert the saying into a digit string, replace the counts with a number and
# concatenate every saying.

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n - 1)
        result = []
        count = 1
        
        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                count += 1
            else:
                result.append(str(count))
                result.append(prev[i - 1])
                count = 1
        
        result.append(str(count))
        result.append(prev[-1])
        
        return ''.join(result)