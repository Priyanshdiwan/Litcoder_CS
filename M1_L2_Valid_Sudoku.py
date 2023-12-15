def check_for_sudoku(board):
    for row in board:
        if not is_valid_until(row):
            return False
    for col in zip(*board):
        if not is_valid_until(col):
            return False
    for i  in range(0,9,3):
        for j in range(0,9,3):
            square=[board[x][y] for x in range(i,i+3) for y in range(j,+j+3)]
            if not is_valid_until(square):
                return False
    return True
def is_valid_until(unit):
    seen=set()
    for num in unit:
        if num!='.':
            if num in seen:
                return False
            seen.add(num)
    return True
num_cols=input()
input_board = [list(cell if cell.isdigit() else '.' for cell in input().split()) for _ in range(9)]
print(check_for_sudoku(input_board))
                                                                                                                            