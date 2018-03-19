import random
from connect_four.board import Board


class Player:
    def __init__(self):
        self.internalboard = Board()
        self.counts = [0] * 7
        self.best_move = 0
        self.won_score = 1000
        
    def name(self):
        play_name = 'MYPLAYER'
        return play_name

    def make_move(self, move):
        self.counts[move] += 1
        
        for i in range(0, 7):
            if self.counts[i] != 0:
                for j in range(1, self.counts[i] + 1):
                    self.internalboard.make_move(j)
                
        return self.internalboard       

    def get_move(self):
        legal_move = 0
        search_depth = 3
        intial_alpha = -float('inf')
        intial_beta = float('inf')
        
        score = self.alphaBetaWithNegamax(self.internalboard, intial_alpha, intial_beta, search_depth)
        
        if score == self.won_score:
            legal_move = self.best_move
            
        return legal_move
    
    def alphaBetaWithNegamax(self, board, alpha, beta, depth):
        v = 0
        
        if board.last_move_won():
            return self.utility_evaluation(board)
        else:
            if depth == 0:
                return self.evaluationForPlayer(board)
            else:
                for i in board.generate_moves():
                    board.make_move(i)
                    v = -self.alphaBetaWithNegamax(board, -beta, -alpha, depth - 1)
                    board.unmake_last_move()
                    
                    if v == 1000:
                        self.best_move = i
                        break
                                         
                    if v >= beta:
                        return beta
                    elif v > alpha:
                        alpha = v
             
        return alpha

    def utility_evaluation(self, finalboard):
        utility = self.won_score
        
        return utility     

    def evaluationForPlayer(self, board):
        return 100
