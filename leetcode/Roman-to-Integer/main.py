class Solution:
    def romanToInt(self, s: str) -> int:
        SYM_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = SYM_VALUES[s[0]]
        pre_v = num

        for i in range(1, len(s)):
            c = s[i]
            v = SYM_VALUES[c]

            if pre_v < v:
                num += -2 * pre_v + v
            else:
                num += v
            pre_v = v
        return num


if __name__ == "__main__":
    tests = [("III", 3), ("LVIII", 58), ("MCMXCIV", 1994)]
    s = Solution()
    for test in tests:
        print(f"test: {test}, result: {s.romanToInt(test[0])}")
