from typing import List 

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        sum_right = sum_nums
        sum_up_current = 0
        num_valid_split = 0
        for v in nums[:-1]:
            sum_up_current += v
            sum_right -= v
            if sum_up_current >=  sum_right:
                num_valid_split += 1
        return num_valid_split
