class Solution:
    def numberOfWays(self, s: str) -> int:
        valid_ways = 0
        ones = zeros = one_zeros = zero_ones = 0

        for c in s:
            if c == "0":
                zeros += 1
                one_zeros += ones
                valid_ways += zero_ones

            else:
                ones += 1
                zero_ones += zeros
                valid_ways += one_zeros

        return valid_ways


if __name__ == "__main__":
    s = Solution()
    ways = s.numberOfWays("001101")
    print(f"Num ways: {ways}")
