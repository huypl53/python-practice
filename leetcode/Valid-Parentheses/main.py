class Solution:
    PARENTHESES_PAIRS = {"(": ")", "[": "]", "{": "}"}

    def isValid(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return True
        if n % 2 != 0:
            return False

        left = list(s)
        right = list()

        for p in left[::-1]:
            if not len(right):
                right.append(p)
                continue
            if p in self.PARENTHESES_PAIRS:
                if self.PARENTHESES_PAIRS[p] == right[-1]:
                    right.pop()
                    continue

                return False

            right.append(p)

        return not len(right)


#
# if __name__ == "__main__":
#     tests = ["()", "()[]{}", "(]"]
#
#     s = Solution()
#     for test in tests:
#         print(f"f{test}: {s.isValid(test)}")
