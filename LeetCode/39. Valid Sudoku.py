from collections import defaultdict

def isValidSudoku(board):
    rows = defaultdict(set) #memory on On max 9 elements
    cols = defaultdict(set)
    boxes = defaultdict(set)

    for r in range(9): # check row position
        for c in range(9): # check colunm position
            current = board[r][c]
            if board[r][c] == ".":
                continue
            
            # Search on O1
            if current in rows[r] or current in cols[c] or current in boxes[(r//3,c//3)]:
                return False

            rows[r].add(current)
            cols[c].add(current)
            boxes[(r//3,c//3)].add(current)

    return True



if __name__ == '__main__':

#Input: > Output: true
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

#Input: Output: false
    board2= [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

    print("Is valid Sudoku:",isValidSudoku(board2))


# 39. Valid Sudoku

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be 
# validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without 
# repetition.

# Note:
#   A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#   Only the filled cells need to be validated according to the mentioned rules.