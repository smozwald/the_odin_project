""""Samuel Oswald 4 March 2019.
A simple tic-tac-toe game, made for the Odin Project curriculum, using Python instead of Ruby."""
import numpy as np

##As players make moves, they will add either 1 or 2 depending on player to squares.
##Track total moves to reset game.

class TicTacToe():

    def __init__(self):
        self.board, self.total_moves, self.player = self.new_game()
        ##Initialize valid moves into corresponding parts of board.
        ##seperated to easily lookup the letters and easily lookup the board position.
        self.valid_letters = list("qweasdzxc")
        self.valid_moves = []
        for i in range(3):
            self.valid_moves.append(self.valid_letters[i*3:i*3+3])

    def new_game(self):
        board = np.zeros((3,3))
        total_moves = 0
        player = "Player 1"
        return board, total_moves, player

    def make_move(self):
        """Make a move for each player, check its valid and victory condition."""
        player = self.player
        move = input(player +", it is your turn. \n Please select a move.").lower()
        if self.is_valid(move):
            self.update_board(player, move)
        else:
            print("Invalid move, please try again.")
            self.make_move()
            return

    def is_valid(self, move):
        """Checks that a move is valid, and that the player hasn't moved into an occupied square."""
        if move in self.valid_letters:
            for i in range(3):
                for j in range(3):
                    if move == self.valid_moves[i][j]:
                        return True if self.board[i,j] == 0 else False
        else:
            return False

    def update_board(self, player, move):
        """Updates the board when a valid move is made."""
        num = int(player[-1])
        for i in range(3):
                for j in range(3):
                    if move == self.valid_moves[i][j]:
                        self.board[i][j] = num
                        return
    
    def check_victory(self):
        """Checks if victory condition of 3 in a row met."""
        for i in range(3):
            if ((np.all(self.board[i,:] == self.board[i,0])) 
                and (self.board[i,0] != 0)):
                    return True
            if ((np.all(self.board[:, i] == self.board[0,i])) 
                and (self.board[0,i] != 0)):
                    return True
        ##Also check diagonal
        if (((self.board[0,0] == self.board[1,1] == self.board[2,2])
            or (self.board[2,0] == self.board[1,1] == self.board[0,2]))
            and self.board[1,1] != 0):
            return True
        else:
            return False
    
    def show_board(self):
        """Shows the current state of the board."""
        line = "Current game state is:"
        for row in self.board:
            line = line + "\n "
            for cell in row:
                line = line + str(int(cell)) + " "
        print(line)

    def play_game(self):
        """Plays the game."""
        victory = False
        print ("You have started a new game of Tic Tac Toe." 
            + "\n The selections possible are as follows:"
            + "\n q w e"
            + "\n a s d"
            + "\n z x c"
            + "\n Points on the board correspond to player 1 and player 2.")
        while not victory:
            self.show_board()
            self.make_move()
            victory = self.check_victory()
            if victory:
                print ("The game has been won by " + self.player)
                self.show_board()
                return
            self.total_moves += 1
            if self.total_moves >= 9:
                print ("The game has concluded with no winner.")
                return
            if self.player == "Player 1":
                self.player = "Player 2"
            else: 
                self.player = "Player 1"

game = TicTacToe()
game.play_game()

        


