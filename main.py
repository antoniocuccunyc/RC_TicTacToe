def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()

def check_win(board):
    win_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)  # diagonals
    ]
    for a, b, c in win_combos:
       if board[a] != ' ' and board[a] == board[b] and board[a] == board[c]:
           return board[a]
    return None

def is_board_full(board):
    return '' not in board

def get_move(board, player):
    while True:
        try:
            move = input(f'Player{player}, enter your move (1-9: ')
            move = int(move) - 1
            if move < 0 or move > 8:
                print('Invalid move, please enter a number between 1 and 9')
            if board[move] != ' ':
                print('Invalid move, the spot is already filled')
            return move
        except ValueError:
            print('Invalid move, please enter a number between 1 and 9')

