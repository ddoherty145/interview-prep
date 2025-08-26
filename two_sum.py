class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map ={}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        raise ValueError("No two sum solution")
    
    # Usage example:
if __name__ == "__main__":
    
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(s.twoSum([3, 2, 4], 6))       # Output: [1, 2]
    print(s.twoSum([3, 3], 6))          # Output: [0, 1]