
def check_alphanumeric(c: str):
    i = ord(c)
    if 48 <= i <= 57: return True
    if 97 <= i <= 122 or 97 <= i+32 <= 122: return True
    return False

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        valid_chars = [c.lower() for c in s if check_alphanumeric(c)]
        i = 0
        j = len(valid_chars) - 1
        if j == -1: return True
        if j == 0: return True

        while i < j:
            if valid_chars[i] != valid_chars[j]: return False
            i += 1
            j -= 1

        return True
