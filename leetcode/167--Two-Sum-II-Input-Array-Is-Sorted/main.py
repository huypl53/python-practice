from typing import List

class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1

        # There is exactly 1 solution
        while left < right:
            s = numbers[left] + numbers[right]
            if s > target:
                right -= 1
            elif s < target:
                left += 1
            
            else: return (left+1, right+1)

    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        # 2 <= n
        # There is exactly one solution -> ignore duplicated numbers
        # non-decreasing order ??
        pre_num = None
        for i in range(0, n-1):
            if numbers[i]  == pre_num: continue

            pre_num = numbers[i]
            
            for j in range(i+1, n-1):
                if numbers[j] == numbers[j+1]: continue

                if numbers[i] + numbers[j] == target:
                    return (i+1, j+1)
            else:
                j = n - 1
                if numbers[i] + numbers[j] == target: return (i+1, j+1)


