import random


class TicTacGame:
    '''Class tic tac game'''
    def __init__(self, dim: int, mode: bool) -> None:
        '''Initialization variables'''
        self.dim: int = dim
        self.mode: bool = mode
        self.board: list = [[' '] * dim for _ in range(dim)]
        self.player: str = 'X'
        self.residuals: list = [(i, j) for i in range(dim) for j in range(dim)]


    def show_board(self, dim: int, board: int) -> None:
        '''Fucntion showing game board'''
        indexes: list = [' ' + str(i) for i in range(1, dim + 1)]
        print(' ', *indexes, sep='')
        print(' ', *'-' * dim)
        for i in range(dim):
            print(i + 1, '|', sep='', end='')
            for j in range(dim):
                print(f'{board[i][j]}|', end='')
            print()
            print(' ', *'-' * dim)                

    def validate_input(self, user_input: str, dim: int, board: list) -> bool:
        '''Fucntion checking that inputed coordinates of cell is correct '''
        try:
            num1, num2 = map(int, user_input.split())
            if 1 <= num1 <= dim and 1 <= num2 <= dim:
                if board[num1 - 1][num2 - 1] == ' ':
                    return True
                else:
                    print('Error: this position is busy')
            else:
                print('Error: positional indexes are out-of-board')
        except ValueError:
            print('Error: input must consist two integers')
        return False
        
    def check_winner(self, dim: int, board: list) -> bool:
        '''Fucntion checking vicrtory players'''
        for i in range(dim):
            for j in range(dim - 2):
                if board[i][j] == board[i][j + 1] == board[i][j + 2] != ' ':
                    return True
        for i in range(dim - 2):
            for j in range(dim):
                if board[i][j] == board[i + 1][j] == board[i + 2][j] != ' ':
                    return True
        for i in range(dim - 2):
            for j in range(dim - 2):
                if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] != ' ':
                    return True
        for i in range(dim - 2):
            for j in range(2, dim):
                if board[i][j] == board[i + 1][j - 1] == board[i + 2][j - 2] != ' ':
                    return True
        return False


    def start_game(self) -> None:
        '''Main game function'''
        i: int = 0
        while i < self.dim ** 2:
            self.show_board(self.dim, self.board)
            if self.mode is False:
                lexicon_input: str = ' choose two integer indexes\nFor exemple: 1 2\n'
                user_input: str = input('Player ' + self.player + lexicon_input)
                if self.validate_input(user_input, self.dim, self.board):
                    num1, num2 = map(int, user_input.split())
                    if self.player == 'X':
                        self.board[num1 - 1][num2 - 1] = f'\033[31m{self.player}\033[0m'
                    else:
                        self.board[num1 - 1][num2 - 1] = f'\033[32m{self.player}\033[0m'
                    if i > 3 and self.check_winner(self.dim, self.board):
                        self.show_board(self.dim, self.board)
                        print(f'\033[33mPlayer {self.player} wins!\033[0m')
                        break
                    self.player: str = 'O' if self.player == 'X' else 'X'
            else:
                if i % 2 == 0:
                    lexicon_input: str = 'Choose two integer indexes\nFor exemple: 1 2\n'
                    user_input: str = input(lexicon_input)
                    if self.validate_input(user_input, self.dim, self.board):
                        num1, num2 = map(int, user_input.split())
                        self.board[num1 - 1][num2 - 1] = f'\033[31m{self.player}\033[0m'
                        self.residuals.remove((num1 - 1, num2 - 1))

                        if i > 3 and self.check_winner(self.dim, self.board):
                            self.show_board(self.dim, self.board)
                            print('\033[33mYou win!\033[0m')
                            break
                else:
                    num1, num2 = random.choice(self.residuals)
                    self.board[num1][num2] = '\033[32mC\033[0m'
                    self.residuals.remove((num1, num2))
                    if i > 3 and self.check_winner(self.dim, self.board):
                        self.show_board(self.dim, self.board)
                        print('\033[33mComputer wins!\033[0m')
                        break 
            i += 1
        if i == self.dim ** 2:
            self.show_board()
            print('\033[33mTie!\033[0m')            

def check_dim(dim: str) -> bool:
    '''Fucntion checking that inputed dim board is correct'''
    try:
        number = int(dim)
        if 3 <= number <= 9:
            return True
        else:
            print('Error: input must be 3 <= x <= 9')
    except ValueError:
        print('Error: input must be integer')
    return False

def check_mode(mode: str) -> bool:
    '''Fucntion checking that inputed mode of game is correct'''
    try:
        number = int(mode)
        if number in (0, 1):
            return True
        else:
            print('Error: input must be 0 or 1')
    except ValueError:
        print('Error: input must be integer')
    return False


if __name__ == "__main__":
    while True:
        user_dim: str = input('Enter dim of board(3 <= x <= 9):\n')
        if check_dim(user_dim):
            break
    while True:
        user_mode: str = input('Enter mode of game:\n0. Two players mode\n1. Computer mode\n')
        if check_mode(user_mode):
            break
    game: TicTacGame = TicTacGame(int(user_dim), bool(int(user_mode)))
    game.start_game()
