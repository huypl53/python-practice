class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count = defaultdict(list)

        step = 10
        # row: count[i]
        # col: count[step + i]
        # grid: count[2*step + step*(i//3) + j//3]

        for i in range(9):

            for j in range(9):
                if board[i][j] == ".":
                    continue

                v = board[i][j]
                if v in count[i]:
                    return False
                else:
                    count[i].append(v)

                if v in count[step + j]:
                    return False
                else:
                    count[step + j].append(v)

                if v in count[2 * step + step * (i // 3) + j // 3]:

                    return False
                else:
                    count[2 * step + step * (i // 3) + j // 3].append(v)

        return True
