class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        for i in range(9):
            d_row_i = {}
            for j in range(9):
                if A[i][j] != ".":
                    if A[i][j] in d_row_i:
                        return 0
                    else:
                        d_row_i[A[i][j]] = 1
        for i in range(9):
            d_col_i =  {}
            for j in range(9):
                if A[j][i] != ".":
                    if A[j][i] in d_col_i:
                        return 0
                    else:
                        d_col_i[A[j][i]] = 1
        baap = [[{} for i in range(3)] for j in range(3)]
        for i in range(9):
            for j in range(9):
                pos_x = i // 3
                pos_y = j // 3
                if A[i][j] != ".":
                    if A[i][j] in baap[pos_x][pos_y]:
                        return 0
                    else:
                        baap[pos_x][pos_y][A[i][j]] = 1
        return 1