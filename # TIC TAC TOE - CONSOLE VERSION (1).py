# Console-Based Tic-Tac-Toe Game

def print_board(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


def check_winner(board, player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False


def tic_tac_toe():
    board = [" " for _ in range(9)]
    current_player = "X"
    moves = 0

    while True:
        print_board(board)
        try:
            choice = int(input(f"Player {current_player}, choose position (1-9): ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        if choice < 0 or choice > 8 or board[choice] != " ":
            print("Invalid move. Try again.")
            continue

        board[choice] = current_player
        moves += 1

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        if moves == 9:
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()

