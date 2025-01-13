from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        h = len(board)
        w = len(board[0])
        mask_board = list()
        for j, row in enumerate(board):
            mask_board.append(list())
            for i, cell in enumerate(row):
                sum_cell_neighs = self.calc_sum_neighbors(board, i, j, w, h)
                new_value = 0
                if cell == 0:
                    if sum_cell_neighs == 3:
                        new_value = 1
                    else: new_value = cell
                else:
                    if sum_cell_neighs < 2:
                        new_value = 0
                    elif 2 <= sum_cell_neighs <=3: new_value = 1
                    else: new_value = 0
                mask_board[-1].append(new_value)
        
        for j in range(h):
            for i in range(w):
                board[j][i] = mask_board[j][i]

    def calc_sum_neighbors(self, board: List[List[int]], i_c: int, j_c: int, w: int, h: int) -> int:
        start_i = max(0, i_c - 1)
        end_i = min(w, i_c + 2)
        start_j = max(0, j_c - 1)
        end_j = min(h, j_c + 2)
        neighbor_sum = 0
        for j in range(start_j, end_j):
            for i in range(start_i, end_i):
                neighbor_sum += board[j][i]
        neighbor_sum -= board[j_c][i_c]
        return neighbor_sum

