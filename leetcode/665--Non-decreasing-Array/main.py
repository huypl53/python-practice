from typing import List

class Solution:
    non_decreasing = 0
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True
        head = 0
        n = len(nums)
        tail = n - 1
        err_nums = 0
        if nums[head] > nums[head+1]:
            nums[head] = nums[head+1]
            err_nums += 1
            head += 1
        if nums[tail-1] > nums[tail]:
            nums[tail] = nums[tail-1]
            err_nums += 1
            tail -= 1
        while tail - head > 0 and err_nums < 2:
            
            if nums[head] > nums[head+1]:
                if nums[head-1] > nums[head+1]:
                    nums[head+1] = nums[head]
                else:
                    nums[head] = nums[head+1]               
                err_nums += 1
            head += 1
        return err_nums < 2
