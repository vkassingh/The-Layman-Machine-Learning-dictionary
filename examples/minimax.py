# Minimax for tic-tac-toe

# NOTE : THIS IS NOT COMPLETELY SET UP FOR USE
# IT IS UP TO YOU TO DESIGN YOUR OWN TIC-TAC TO GAME TO APPLY THIS. THIS IS MERELY THE ALGORITHM

def minimax(state, depth, player):
    if player == COMPUTER:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]
    
    # If the game is over, evaluate the board
    # If you are winning, return infinity else, return -infinity
    # The goal is to choose the option with the best possible score
    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]
        
    # Play through every different possible game
    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        # recursively call minimax to build a tree and get the choose the best move from it
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMPUTER:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score

    return best
