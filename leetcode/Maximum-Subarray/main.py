from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        mid_idx = n // 2

        left_nums = nums[:mid_idx]
        right_nums = nums[mid_idx:]

        left_max = self.maxSubArray(left_nums)
        right_max = self.maxSubArray(right_nums)

        maxx = max(left_max, right_max)
        sum_max = left_max + right_max
        if maxx > sum_max:
            return maxx  # when one max < 0, return bigger

        max_mid2left = -100000
        sum_mid_left = 0
        for l in left_nums[::-1]:
            sum_mid_left += l
            if sum_mid_left > max_mid2left:
                max_mid2left = sum_mid_left

        sum_mid_right = 0
        max_mid2right = -100000
        for l in right_nums[:]:
            sum_mid_right += l
            if sum_mid_right > max_mid2right:
                max_mid2right = sum_mid_right

        return max(max_mid2right + max_mid2left, maxx)


if __name__ == "__main__":
    tests = [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6), ([1], 1), ([5, 4, -1, 7, 8], 23)]
    s = Solution()
    for test in tests:
        print(f"array: {test[0]}, expec: {test[1]}, result: {s.maxSubArray(test[0])}")
