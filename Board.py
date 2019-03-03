class Board:
    
    def __init__(self):
        self.board = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]
    
    
    def mark_X(self, row, column):
        self.board[row][column] = "X"
    
    
    def mark_O(self, row, column):
        self.board[row][column] = "O"
   
    
    def check_row(self):
        for row in self.board:
            if row[0] == row[1] and row[1] == row[2] and row[0] != 0:
                return True
        return False
    
    
    def check_column(self):
        if self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0] and self.board[0][0] != 0:
            return True
        elif self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1] and self.board[0][1] != 0:
            return True
        elif self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2] and self.board[0][2] != 0:
            return True
        return False
    
    
    def check_left_diagonal(self):
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != 0:
            return True
        return False
    
    
    def check_right_diagonal(self):
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[0][2] != 0:   
            return True
        return False
    
    
    def win(self):
        if self.check_row() or self.check_column() or self.check_left_diagonal() or self.check_right_diagonal():
            return True
        return False

        
    def display(self):
        print(" ", self.board[0][0], " | ", self.board[0][1], " | ", self.board[0][2], " ")
        print("-----------------")
        print(" ", self.board[1][0], " | ", self.board[1][1], " | ", self.board[1][2], " ")
        print("-----------------")
        print(" ", self.board[2][0], " | ", self.board[2][1], " | ", self.board[2][2], " ")