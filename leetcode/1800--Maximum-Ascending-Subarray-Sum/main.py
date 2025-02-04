from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_asc_sum = 0
        current_sum = 0
        prev = 0
        for v in nums:
            if v > prev:
                current_sum += v
            else:
                if current_sum > max_asc_sum:
                    max_asc_sum = current_sum
                current_sum = v
            prev = v
        return max(current_sum, max_asc_sum)
