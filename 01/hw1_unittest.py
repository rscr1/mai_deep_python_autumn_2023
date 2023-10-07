import unittest

from hw1 import check_dim, check_mode, TicTacGame


class Test(unittest.TestCase):
    def setUp(self):
        self.mode = 1

        self.board3_1 = [['X', 'O', 'X'],
                      ['O', 'O', 'O'],
                      ['X', 'X', ' ']]

        self.board3_2 = [['X', 'O', 'X'],
                      ['X', 'X', 'O'],
                      ['O', 'O', 'O']]

        self.board3_3 = [['O', 'X', 'O'],
                      ['X', 'O', 'X'],
                      ['O', 'O', 'X']]

        self.board3_4 = [['O', 'X', 'X'],
                      ['X', 'O', 'O'],
                      ['O', 'X', 'O']]
        
        self.board3_5 = [['X', 'O', ' '],
                      ['O', 'O', ' '],
                      ['X', 'X', 'X']]
        
        self.board3_6 = [['X', 'O', 'X'],
                      ['O', 'X', 'O'],
                      ['O', 'X', 'O']]
        
        self.board3_7 = [['X', ' ', ' '],
                      [' ', ' ', ' '],
                      ['O', 'X', ' ']]
        
        self.board3_8 = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        
        self.board3_9 = [['X', 'O', 'X'],
                      ['X', 'O', 'O'],
                      ['O', 'X', 'X']]
        
        self.board4 = [['X', 'O', 'X', 'O'],
                       ['O', 'O', 'O', 'X'],
                       ['X', 'X', ' ', 'O'],
                       ['X', 'X', 'O', 'X']]
        
        self.board5 = [['X', 'O', 'X', 'O', 'X'],
                       ['X', 'X', 'O', 'X', 'O'],
                       ['O', 'O', 'O', 'O', 'X'],
                       ['X', 'O', 'X', 'O', 'X'],
                       ['X', 'X', 'O', 'X', 'O']]
        
        self.board6 = [['O', 'X', 'O', 'X', 'X', 'X'],
                       ['X', 'O', 'X', 'X', 'O', 'O'],
                       ['O', 'O', 'X', 'O', 'O', 'X'],
                       ['X', 'X', 'O', 'X', 'X', 'O'],
                       ['O', 'X', 'O', 'X', 'X', 'O'],
                       ['X', 'O', 'O', 'O', 'X', 'O']]
        
        self.board9 = [['O', 'X', 'O', ' ', 'X', ' ', ' ', ' ', 'O'],
                       ['X', 'X', ' ', 'X', 'O', 'O', 'X', 'O', 'X'],
                       ['O', ' ', 'O', 'O', ' ', 'X', ' ', 'X', 'O'],
                       ['X', 'X', ' ', 'X', ' ', 'X', 'O', 'O', ' '],
                       ['O', 'X', 'O', ' ', 'O', 'O', ' ', 'X', 'O'],
                       [' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', 'X'],
                       ['O', 'X', 'X', 'O', 'X', 'X', 'O', 'O', ' '],
                       ['X', ' ', ' ', ' ', 'O', ' ', ' ', 'X', 'X'],
                       ['X', 'O', 'X', ' ', 'X', 'X', 'O', ' ', 'O']]
        
    #check_dim
    def test_check_dim_valid(self):
        self.assertTrue(check_dim('3'))
        self.assertTrue(check_dim('6'))

    def test_check_dim_invalid(self):
        self.assertFalse(check_dim('2'))
        self.assertFalse(check_dim('10'))
        self.assertFalse(check_dim('5.4'))
        self.assertFalse(check_dim('abc'))
        self.assertFalse(check_dim(''))

    #check_mode
    def test_check_mode_valid(self):
        self.assertTrue(check_mode("0"))
        self.assertTrue(check_mode("1"))

    def test_check_mode_invalid(self):
        self.assertFalse(check_mode(""))
        self.assertFalse(check_mode("2"))
        self.assertFalse(check_mode("abc"))
        self.assertFalse(check_mode("0.5"))

    #check_winner
    def test_check_winner_valid(self):
        self.assertTrue(TicTacGame(3, self.mode).check_winner(3, self.board3_1))
        self.assertTrue(TicTacGame(3, self.mode).check_winner(3, self.board3_2))
        self.assertTrue(TicTacGame(3, self.mode).check_winner(3, self.board3_3))
        self.assertTrue(TicTacGame(3, self.mode).check_winner(3, self.board3_4))
        self.assertTrue(TicTacGame(3, self.mode).check_winner(3, self.board3_5))
        self.assertTrue(TicTacGame(4, self.mode).check_winner(4, self.board4))
        self.assertTrue(TicTacGame(5, self.mode).check_winner(5, self.board5))
        self.assertTrue(TicTacGame(6, self.mode).check_winner(6, self.board6))

    def test_check_winner_invalid(self):
        self.assertFalse(TicTacGame(3, self.mode).check_winner(3, self.board3_6))
        self.assertFalse(TicTacGame(3, self.mode).check_winner(3, self.board3_7))
        self.assertFalse(TicTacGame(3, self.mode).check_winner(3, self.board3_8))
        self.assertFalse(TicTacGame(3, self.mode).check_winner(3, self.board3_9))
        self.assertFalse(TicTacGame(9, self.mode).check_winner(9, self.board9))

    #validate_input
    def test_validate_input_valid(self):
        self.assertTrue(TicTacGame(3, self.mode).validate_input('1 3', 3, self.board3_5))
        self.assertTrue(TicTacGame(3, self.mode).validate_input('1 1', 3, self.board3_8))
        self.assertTrue(TicTacGame(4, self.mode).validate_input('3 3', 4, self.board4))
        self.assertTrue(TicTacGame(9, self.mode).validate_input('1 4', 9, self.board9))

    def test_validate_input_invalid(self):
        self.assertFalse(TicTacGame(3, self.mode).validate_input('4 4', 3, self.board3_8))
        self.assertFalse(TicTacGame(3, self.mode).validate_input('3.5 1', 3, self.board3_8))
        self.assertFalse(TicTacGame(3, self.mode).validate_input('1 100', 3, self.board3_8))
        self.assertFalse(TicTacGame(5, self.mode).validate_input('1 1', 5, self.board5))
        self.assertFalse(TicTacGame(6, self.mode).validate_input('1, 1', 6, self.board6))

unittest.main()