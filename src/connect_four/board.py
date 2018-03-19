
class Board:
    def __init__(self):
        self.width = 7
        self.height = 6 
        self.matrix = [[0 for col in range(self.width)] for row in range(self.height)]
        self.movelist = []
        
        self.playerlist = [1, 2]
        self.player = self.playerlist[0]
    
    def generate_moves(self):
        available_moveslist = []
        for i in range(0, len(self.matrix[0])):
            if self.matrix[0][i] == 0:
                available_moveslist.append(i)
            else:
                continue
            
        return available_moveslist
    
    def make_move(self, move):
        for i in range(5, -1, -1):
            if self.matrix[i][move] == 0:
                if self.player == self.playerlist[0]:
                    self.matrix[i][move] = 1
                    self.movelist.append([i, move])
                    self.player = self.playerlist[1]
                    break
                
                elif self.player == self.playerlist[1]:
                    self.matrix[i][move] = 2
                    self.movelist.append([i, move])
                    self.player = self.playerlist[0]
                    break
            else:
                continue
                       
        return self.matrix
        
    def unmake_last_move(self):
        lp = self.movelist.pop()
        self.matrix[lp[0]][lp[1]] = 0
        
        if self.player == self.playerlist[0]:
            self.player = self.playerlist[1]
        elif self.player == self.playerlist[1]:
            self.player = self.playerlist[0]
                
    def last_move_won(self):
        isWon = False
        
        if not isWon:
            for row in range(6):
                for col in range(4):
                    if self.player == self.playerlist[0]:
                        if self.matrix[row][col] == self.matrix[row][col + 1] == self.matrix[row][col + 2]\
                         == self.matrix[row][col + 3] == 2:
                            isWon = True
                            break
                
                    elif self.player == self.playerlist[1]:
                        if self.matrix[row][col] == self.matrix[row][col + 1] == self.matrix[row][col + 2]\
                         == self.matrix[row][col + 3] == 1:
                            isWon = True
                            break
                    
        if not isWon:        
            for col in range(7):
                for row in range(3):
                    if self.player == self.player == self.playerlist[0]:
                        if self.matrix[row][col] == self.matrix[row + 1][col] == self.matrix[row + 2][col]\
                        == self.matrix[row + 3][col] == 2:
                            isWon = True
                            break
                
                    elif self.player == self.player == self.playerlist[1]:
                        if self.matrix[row][col] == self.matrix[row + 1][col] == self.matrix[row + 2][col]\
                        == self.matrix[row + 3][col] == 1:
                            isWon = True
                            break
        
        if not isWon: 
            for row in range(3):
                for col in range(4):
                    if self.player == self.player == self.playerlist[0]:
                        if self.matrix[row][col] == self.matrix[row + 1][col + 1] == self.matrix[row + 2]\
                        [col + 2] == self.matrix[row + 3][col + 3] == 2:
                            isWon = True
                            break
                        
                    elif self.player == self.player == self.playerlist[1]:
                        if self.matrix[row][col] == self.matrix[row + 1][col + 1] == self.matrix[row + 2]\
                        [col + 2] == self.matrix[row + 3][col + 3] == 1:
                            isWon = True
                            break
                    
        if not isWon:
            for row in range(5, 2, -1):
                for col in range(4):
                    if self.player == self.player == self.playerlist[0]:
                        if self.matrix[row][col] == self.matrix[row - 1][col + 1] == self.matrix[row - 2]\
                        [col + 2] == self.matrix[row - 3][col + 3] == 2:
                            isWon = True
                            break
                
                    elif self.player == self.player == self.playerlist[1]:
                        if self.matrix[row][col] == self.matrix[row - 1][col + 1] == self.matrix[row - 2]\
                        [col + 2] == self.matrix[row - 3][col + 3] == 1:
                            isWon = True
                            break
        
        return isWon        
  
    def __str__(self):
        board_info = 'board width:%d  board height:%d' % (self.width, self.height)
        board_state = str(self.matrix)
        move_info = str(self.movelist)
        total_info = board_info + '\n' + board_state + '\n' + move_info
        
        return total_info
