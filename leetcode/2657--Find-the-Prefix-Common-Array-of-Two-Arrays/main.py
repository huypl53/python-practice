class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        # 1 <= n <= 50
        # A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.
        # unique numbers from 1 to n
        permut_counts = [0] * (n+1)
        result = []
        s = 0
        for a, b in zip(A, B):

            permut_counts[a] += 1
            permut_counts[b] += 1

            if a == b:
                s += 1
            elif permut_counts[a] > 1 and permut_counts[b] > 1:
                s += 2
            elif permut_counts[a] > 1 or permut_counts[b] > 1:
                s += 1
            else:
                pass
            result.append(s)
        return result
            
                




