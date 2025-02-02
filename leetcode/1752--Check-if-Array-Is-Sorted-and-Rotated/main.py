from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        MAXX = 101
        max1 = max2 = 0
        min2 = MAXX
        min1 = nums[0]
        len1 = 1
        # len2 = 0
        for i in range(1, len(nums)):
            if nums[i] >= nums[i - 1]:
                if min2 == MAXX:
                    # len1 += 1
                    max1 = nums[i]
                else:
                    # len2 += 1
                    max2 = nums[i]
            else:
                if min2 != MAXX:
                    return False
                min2 = nums[i]
                max2 = nums[-1]
            if max2 > min1:
                return False
        # print(len1)
        return True
