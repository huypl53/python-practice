from typing import List

class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
        # uniq_nums = list(set(nums))
        # uniq_nums.sort()
        # for i, v in enumerate(uniq_nums):
        #     nums[i] = v
        # return len(uniq_nums)

    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0

        i = 0
        for v in nums[1:]:
            if nums[i] != v:
                i += 1
                nums[i] = v

        return i + 1
