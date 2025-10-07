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

#Narrative Explanation:
# Picture yourself as a conductor of a grand orchestra, but instead of musicians, you’re managing k sorted linked lists, each like a line of performers playing notes in ascending order. Your task is to combine all these lines into a single, harmonious performance—a new sorted linked list where all notes flow seamlessly from lowest to highest.
# For example, imagine three lines of performers:

# First line plays: 1, 4, 5.
# Second line: 1, 3, 4.
# Third line: 2, 6.
# Your job is to guide them into one line that plays: 1, 1, 2, 3, 4, 4, 5, 6. But what if the stage is empty (lists = [])? Or one line has no performers (lists = [[]])?

# Each line could have up to 500 notes, and you might have up to 10,000 lines, with note values ranging from -10,000 to 10,000. The total number of notes won’t exceed 10,000, so you can handle the load. How would you orchestrate this merger to ensure every note is played in perfect order, without missing a beat?

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