import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):    # check the cells main diagonal and anti-diagonal,
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    if check_winner(board, "X"):  #if player win return -1
        return -1
    if check_winner(board, "O"): #if AI win return 1
        return 1
    if is_board_full(board):  #if draw return 0
        return 0

    if is_maximizing:
        max_eval = float("-inf")    #lowest possible initial score.
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False)  # recursively calls the minimax function with the updated board state and depth
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")  #highest possible initial score.
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_move = None
    best_eval = float("-inf")
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_eval = minimax(board, 0, False)
                board[i][j] = " "
                if move_eval > best_eval:
                    best_eval = move_eval
                    best_move = (i, j)
    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while not check_winner(board, "X") and not check_winner(board, "O") and not is_board_full(board):
        row, col = map(int, input("Enter your move (row col): ").split())
        if board[row][col] == " ":
            board[row][col] = "X"
            print_board(board)

            if not check_winner(board, "X") and not is_board_full(board):
                print("AI is making a move...")
                ai_row, ai_col = find_best_move(board)
                board[ai_row][ai_col] = "O"
                print_board(board)
        else:
            print("Cell is already occupied. Try again.")

    if check_winner(board, "X"):
        print("You win!")
    elif check_winner(board, "O"):
        print("AI wins!")
    else:
        print("Game is  draw!")

if __name__ == "__main__":
    main()