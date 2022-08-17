from src.board import Board

def test_board_has_state():
    state = [['X', 'X', 'O'],
            ['X', 'O', 'O'],
            ['O', 'X', 'O']]
    board = Board(state)
    assert board.state == state

def test_O_has_won():
    state = [['X', 'X', 'O'],
            ['X', 'O', 'O'],
            ['O', 'X', 'O']]
    board = Board(state)
    assert (board.winner() == 'O')

def test_X_has_won():
    state = [['X', 'X', 'X'],
            ['X', 'O', 'O'],
            ['O', 'X', 'O']]
    board = Board(state)
    assert (board.winner() == 'X')

def test_left_diagonal_has_won():
    state = [['X', 'X', 'O'],
            ['X', 'O', ''],
            ['O', 'X', 'O']]
    board = Board(state)
    assert (board.winner() == 'O')

def test_righttdiagonal_has_won():
    state = [['X', 'O', 'O'],
            ['X', 'X', ''],
            ['O', 'O', 'X']]
    board = Board(state)
    assert (board.winner() == 'X')


def test_tie_has_won():
    state = [['O', 'X', 'O'],
            ['O', 'X', 'X'],
            ['X', 'O', 'X']]
    board = Board(state)
    assert (board.winner() == 'tie')
