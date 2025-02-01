class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = list(s)
        n = len(l)
        if n < 2:
            return n
        longest_len = 1
        start = end = 0

        # _longest_str = ''
        while end < n:
            for i in range(start, end):
                if l[i] == l[end]:
                    start = i + 1
                    break
            current_sub = end - start + 1
            if current_sub > longest_len:
                longest_len = current_sub
                # _longest_str = ''.join(l[start: end+1])
            end += 1
        # print(_longest_str)
        return longest_len
