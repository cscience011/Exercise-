def is_valid_move(board, row, col):
    return 0 <= row < len(board) and 0 <= col < len(board[0])

def count_adjacent_mines(board, row, col):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            r, c = row + dr, col + dc
            if is_valid_move(board, r, c) and board[r][c] == 'M':
                count += 1
    return count

def reveal_empty_cells(board, row, col, visited):
    if not is_valid_move(board, row, col) or (row, col) in visited:
        return
    visited.add((row, col))
    if board[row][col] != 0:
        return
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            reveal_empty_cells(board, row + dr, col + dc, visited)

def solve_minesweeper(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                visited = set()
                reveal_empty_cells(board, row, col, visited)
                for r, c in visited:
                    if board[r][c] == 'X':
                        board[r][c] = ' '

def minesweeper_solver(board):
    # Step 1: Reveal safe cells
    solve_minesweeper(board)

    # Step 2: Backtracking algorithm to solve remaining cells
    def backtrack(row, col):
        if not is_valid_move(board, row, col):
            return False
        if board[row][col] != 'X':
            return backtrack(row, col + 1) if col < len(board[0]) - 1 else backtrack(row + 1, 0)

        # Try placing a mine and check if it leads to a valid solution
        board[row][col] = 'M'
        if is_valid_solution(board) and backtrack(row, col + 1) if col < len(board[0]) - 1 else backtrack(row + 1, 0):
            return True

        # If placing a mine didn't work, backtrack and try an empty cell
        board[row][col] = ' '
        if is_valid_solution(board) and backtrack(row, col + 1) if col < len(board[0]) - 1 else backtrack(row + 1, 0):
            return True

        # If neither mine nor empty cell works, reset and backtrack further
        board[row][col] = 'X'
        return False

    backtrack(0, 0)
def is_valid_solution(board):
    # Check if the board satisfies the revealed cells' constraints
    for row in range(len(board)):
        for col in range(len(board[0])):
            cell = board[row][col]
            if cell != ' ' and cell != 'M':
                if cell == 'X':
                    continue
                count = count_adjacent_mines(board, row, col)
                if int(cell) != count:
                    return False
    return True


if __name__ == "__main__":
    board = [
        ['X', 'X', '1', ' '],
        ['3', 'X', '2', ' '],
        [' ', '2', 'X', ' '],
        [' ', '2', ' ', ' ']
    ]

    print("Original Board:")
    for row in board:
        print(' '.join(row))

    minesweeper_solver(board)

    print("\nSolved Board:")
    for row in board:
        print(' '.join(row))
