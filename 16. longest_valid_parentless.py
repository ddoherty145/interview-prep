# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

 

# Example 1:

# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:

# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:

# Input: s = ""
# Output: 0
 

# Constraints:

# 0 <= s.length <= 3 * 104
# s[i] is '(', or ')'.

# Solution #1: Dynamic Programming
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        dp = [0] * len(s)
        
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif (i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '('):
                    dp[i] = dp[i - 1] + ((dp[i - dp[i - 1] - 2] if (i - dp[i - 1]) >= 2 else 0) + 2)
                
                max_length = max(max_length, dp[i])
        
        return max_length
        while min_heap:
            current.next = ListNode(heapq.heappop(min_heap))
            current = current.next
        return dummy.next
            
# Solution #2: Merge with Divide and Conquer
class SolutionDivide(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists:
            return None
        
        def mergeTwoLists(l1, l2):
            dummy = ListNode(0)
            current = dummy
            
            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            
            if l1:
                current.next = l1
            if l2:
                current.next = l2
            
            return dummy.next
        
        interval = 1
        total_lists = len(lists)
        
        while interval < total_lists:
            for i in range(0, total_lists - interval, interval * 2):
                lists[i] = mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        
        return lists[0]
    