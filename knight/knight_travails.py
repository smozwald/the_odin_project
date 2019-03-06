"""Created by Samuel Oswald on 6 March 2018.
The purpose of this project is to implement the Knight's Travails algorithm,
as presented on the Odin Project. 

I also aim to utilize test-driven development, creating failing tests prior to implementation.
"""

import numpy as np

class Board():
    """Python class with a board of set dimensions. On this board all the squares will be created as a numpy array."""
    def __init__(self, board_size = 8):
        ##Board contains an array of zero values, knight will be inserted at position 1.
        if (isinstance(board_size, int) and (board_size >= 4)):
            self.size = np.zeros([board_size,board_size])
        else:
            self.size = np.zeros([8,8])
        ##Create an array of every possible knight jump permutation, than eliminate invalid ones.
        self.change_pos = [[x,y] for x in [-2,-1,1,2] for y in [-2,-1,1,2] if abs(x) != abs(y)]

    def valid_check(self, start_pos, end_pos = [0,0]):
        """Helper function to check that positions are within bounds"""
        start_check = all(0 <= p <= self.size.shape[0] for p in start_pos)
        end_check = all(0<= p <= self.size.shape[0] for p in end_pos)
        if (start_check and end_check):
            return True
        else:
            return False

    def get_positions(self, start_pos, searched = []):
        """"Get the positions we can go"""
        
        new_pos = []
        for perm in self.change_pos:
            potential_pos = [start_pos[0] + perm[0], start_pos[1] + perm[1]]
            if (self.valid_check(potential_pos) and not (potential_pos in searched)):
                new_pos.append(potential_pos)
        return new_pos


    def get_moves(self, start_pos = [], end_pos = [], depth = 0, search_path = [], searched = []):
        """start pos and end pos are what we have and what we search for.
        Depth is the current amount of moves taken, search path is the current search path, 
        and searched is used to eliminate squares already explored in a shallower iteration."""
        search = []
        if not (len(start_pos) == 2 or len(end_pos) == 2):
            return ("Please input parameters for start and end moves")
        valid = self.valid_check(start_pos, end_pos)
        if not (valid):
            return ("The moves you have attempted exceed board dimensions")
        
        new_pos = self.get_positions(start_pos, searched)







        


