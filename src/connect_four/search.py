import board
import random


def perft(board, depth):
    new_board = board
    tree_depth = depth
    alist = new_board.generate_moves()
 
    leavesnum = 0
            
    if tree_depth > 0 :
        if not new_board.last_move_won():
            tree_depth = tree_depth - 1    
            for i in alist:
                new_board.make_move(i)
                leavesnum = leavesnum + perft(new_board, tree_depth)
                new_board.unmake_last_move()
        else:
            leavesnum = leavesnum + 1
    else:
        leavesnum = leavesnum + 1
    
    return leavesnum 

max_utility = 1000
min_utility = -1000
draw = 0
step_list = []
    
def find_win(board, depth):
    search_depth = depth
    intial_board = board
    intial_alpha = -float('inf')
    intial_beta = float('inf')

    value = alphaBetaWithNegamax(intial_board, intial_alpha, intial_beta, search_depth)
    
    if value == max_utility:
        reslut_str = 'WIN BY PLAYING %d' % (step_list[0])
        step_list.clear()
    elif value == min_utility:
        reslut_str = 'ALL MOVES LOSE'
        step_list.clear()
    else:
        reslut_str = 'NO FORCED WIN IN %d MOVES' % (depth)
        step_list.clear()
    
    return reslut_str 

def alphaBetaWithNegamax(board, alpha, beta, depth):
    v = 0
    
    if board.last_move_won():
        return utility_evaluation(board)
    else:
        if depth == 0:
            return evaluationForPlayer(board)
        else:
            for i in board.generate_moves():
                board.make_move(i)
                v = -alphaBetaWithNegamax(board, -beta, -alpha, depth - 1)
                board.unmake_last_move()
                
                if v == max_utility:
                    step_list.append(i)
                              
                if v >= beta:
                    return beta
                elif v > alpha:
                    alpha = v
            
            return alpha

def utility_evaluation(finalboard):
    if finalboard.player == finalboard.playerlist[0]:
        utility = max_utility
    elif finalboard.player == finalboard.playerlist[1]:
        utility = min_utility
    else:
        utility = draw

    return utility           

def evaluationForPlayer(board):
    player1num = 0
    player2num = 0
    random_value = random.randint(-10, 10)
    
    for i in range(6):
        for j in range(7):
            if board.matrix[i][j] == 1:
                player1num = player1num + 1
            elif board.matrix[i][j] == 2:
                player2num = player2num + 1
                
    evaluation_function = random_value * player1num + random_value * player2num
    return evaluation_function
