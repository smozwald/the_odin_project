import unittest
from knight_travails import *

class boardTest(unittest.TestCase):
    """Test that the board can be initialized to positive ints greater than 4.
        When a false input is provided, it defaults to size 8."""

    def test_board_no_input(self):
        board = Board()
        shape = board.size.shape
        self.assertEqual(shape, (8, 8))
    
    def test_board_pos_input(self):
        board = Board(20)
        shape = board.size.shape
        self.assertEqual(shape, (20, 20))

    def test_board_neg_input(self):
        board = Board(-2)
        shape = board.size.shape
        self.assertEqual(shape, (8, 8))

    def test_board_word_input(self):
        board = Board("Chaos")
        shape = board.size.shape
        self.assertEqual(shape, (8, 8))

class moveTest(unittest.TestCase):

    def test_test_valid_inputs_false(self):
        b = Board()
        self.assertEqual(b.get_moves(), "Please input parameters for start and end moves")

    def test_error_start_off_board(self):
        b = Board()
        self.assertEqual(b.get_moves([20,20], [0,0]), "The moves you have attempted exceed board dimensions")

    def test_error_end_off_board(self):
        b = Board()
        self.assertEqual(b.get_moves([0,0], [20,20]), "The moves you have attempted exceed board dimensions")

    ##Test the right moves show up where they should in the first rung of dict.
    def test_all_valid_moves_center(self):
        b = Board()
        self.assertEquals(len(b.get_positions([4,4])), 8)

    def test_valid_moves_appear(self):
        b = Board()
        self.assertIn([2,3],b.get_positions([4,4]))

    def test_all_valid_moves_corner(self):
        b = Board()
        self.assertEquals(len(b.get_positions([0,0])), 2)

    def test_searched_cells_not_appended(self):
        b = Board()
        self.assertEquals(len(b.get_positions([4,4], [[2,3]])), 7)


if __name__ == '__main__':
    unittest.main()