from typing import List 

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # at leach len 1 of each dimension
        matrix_size = len(matrix) * len(matrix[0])
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            return [row[0] for row in matrix]
        start_i, end_i = 0, len(matrix[0])-1 
        start_j, end_j = 0, len(matrix)-1 

        j = 0
        i = 1

        # step_i = step_j = 1
        step_ji = [0, 1]

        flatten: List[int] = [matrix[0][0]]

        # jump_i = True
        while len(flatten) < matrix_size:
            print(flatten)
            # print(j, i)
            # if start_i == end_i:
            #     # flatten += matrix[]
            #     flatten.append(matrix[start_j][start_i])
            #     start_j += 1
            #     continue
            # if start_j == end_j:
            #     flatten.append(matrix[start_j][start_i])
            #     start_i += 1
            #     continue
            flatten.append(matrix[j][i])
            print(f'get {matrix[j][i]} at [{j}, {i}]. step: {step_ji}.  [{start_i, end_i,start_j, end_j}]')

            if i == end_i and j == start_j:
                # step_j = 1
                if step_ji[1] != 0 : start_j += 1
                step_ji = [1, 0]
                # continue
            if i == end_i and j == end_j:
                # step_i = -1
                if step_ji[0] != 0: end_i -= 1
                step_ji = [0, -1]
                # i += step_i
                # continue
            if i == start_i and j == end_j:
                # step_j = -1
                # j += step_j
                if step_ji[1] != 0: end_j -= 1
                step_ji = [-1, 0]
                # continue
            if i == start_i and j == start_j:
                if step_ji[0] != 0 : start_i += 1
                step_ji =[0, 1]
            i += step_ji[1]
            j += step_ji[0]
        return flatten

                



