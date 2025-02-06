class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        dif_chars = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                dif_chars.append(s1[i])
                dif_chars.append(s2[i])

            if len(dif_chars) > 4:
                return False  # there are more than different pair
        if len(dif_chars) == 0:
            return True
        if len(dif_chars) == 2:
            return False
        return dif_chars[0] == dif_chars[3] and dif_chars[1] == dif_chars[2]
