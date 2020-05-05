import numpy as np
import random 
random.seed(1)

def create_board():
    board = np.zeros((3,3), dtype=int)
    return board

def possibilities(board):
    return list(zip(*np.where(board==0)))

def random_place(board, player):
    selection=possibilities(board)
    position=random.choice(selection)
    board[position]=player
    return board

def row_win(board, player):
    if np.any(np.all(board==player, axis=1)):
        return True
    else:
        return False

def col_win(board, player):
    if np.any(np.all(board==player, axis=0)): # this checks if any column contains all positions equal to player
        return True
    else:
        return False

def diag_win(board, player):
    if np.all(np.diag(board)==player) or np.all(np.diag(np.fliplr(board))==player):
        # np.diag returns the diagonal of the array
        # np.fliplr rearranges columns in reverse order
        return True
    else:
        return False

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # add your code here!
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

def play_game():
    board = create_board()
    winner = 0
    while winner == 0:
        for player in [1, 2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

results = [play_game() for i in range(1000)]
print(results.count(1))