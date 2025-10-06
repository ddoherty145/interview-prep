# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
 

# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution #1: Merge with Min-Heap
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        
        import heapq
        
        min_heap = []
        
        for l in lists:
            while l:
                heapq.heappush(min_heap, l.val)
                l = l.next
        
        dummy = ListNode(0)
        current = dummy
        
        while min_heap:
            val = heapq.heappop(min_heap)
            current.next = ListNode(val)
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
    
# Solution #3: Merge with Brute Force
class SolutionBrute(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        
        values = []
        
        for l in lists:
            while l:
                values.append(l.val)
                l = l.next
        
        values.sort()
        
        dummy = ListNode(0)
        current = dummy
        
        for val in values:
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next