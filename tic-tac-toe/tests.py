import unittest
from tictactoe import *

"""Created by Samuel Oswald on 7 March 2019.
Creating tests for the tic-tac-toe board class.
Looking at whether board is created correctly,
moves are updated correctly,
victory conditions met, and that raw input will work right (using analogy)"""

class boardTest(unittest.TestCase):
    """These tests just check that the board initializes right and to the correct player.
    If they fail something has gone horribly wrong."""
    
    def test_board_shape_is_correct_on_init(self):
        b = TicTacToe()
        shape = b.board.shape
        self.assertEqual(shape, (3,3))

    def test_player_starts_as_player_1(self):
        b = TicTacToe()
        p1 = b.player
        self.assertEqual(p1, "Player 1")

class moveTest(unittest.TestCase):
    """Tests that moves are registered after player movemenets."""

    def test_board_changes_when_p1_moves(self):
        b = TicTacToe()
        b.update_board("Player 1", 'w') ##Top row
        board = b.board
        expected = np.zeros((3,3))
        expected[0,1] = 1
        self.assertEqual(board.tolist(), expected.tolist())

    def test_board_changes_when_both_players_move(self):
        b = TicTacToe()
        b.update_board("Player 1", 'w') ##Top row
        b.update_board("Player 2", 'a')
        board = b.board
        expected = np.zeros((3,3))
        expected[0,1] = 1
        expected[1,0] = 2
        self.assertEqual(board.tolist(), expected.tolist())

    def test_board_changes_when_win_condition_met(self):
        b = TicTacToe()
        b.update_board("Player 1", 'w') ##Top row
        b.update_board("Player 2", 'a')
        b.update_board("Player 1", 'q') 
        b.update_board("Player 2", 's')
        b.update_board("Player 1", 'e')
        board = b.board
        expected = np.zeros((3,3))
        expected[0,1] = 1
        expected[1,0] = 2
        expected[0,0] = 1
        expected[1,1] = 2
        expected[0,2] = 1
        self.assertEqual(board.tolist(), expected.tolist())


class inputTest(unittest.TestCase):
    """Check that only inputs within the accepted keys will pass the valid check."""

    def test_valid_when_valid_input_inserted(self):
        b = TicTacToe()
        self.assertTrue(b.is_valid('w'))

    def test_false_when_invalid_input_inserted(self):
        b = TicTacToe()
        self.assertFalse(b.is_valid('g'))

    def test_false_when_string_with_valid_val_inserted(self):
        b = TicTacToe()
        self.assertFalse(b.is_valid('wongus'))
    
    def test_false_when_num_inserted(self):
        b = TicTacToe()
        self.assertFalse(b.is_valid(1))


class victoryTest(unittest.TestCase):
    """Test that victory conditions are registered."""

    def test_victory_recorded_when_condition_met(self):
        b = TicTacToe()
        b.update_board("Player 1", 'w')
        b.update_board("Player 2", 'a')
        b.update_board("Player 1", 'q') 
        b.update_board("Player 2", 's')
        b.update_board("Player 1", 'e')
        self.assertTrue(b.check_victory())

    def test_victory_not_recorded_when_condition_not_met(self):
        b = TicTacToe()
        b.update_board("Player 1", 'w')
        self.assertFalse(b.check_victory())