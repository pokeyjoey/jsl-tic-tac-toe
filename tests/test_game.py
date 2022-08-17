from src.game import Game
from src.board import Board
from src.player import Player

def test_game_has_board():
    state = [['X', 'X', 'O'],
            ['X', 'O', 'O'],
            ['O', 'X', 'O']]
    max_players = 2
    board = Board(state)
    game = Game(board, max_players)
    assert game.board == board

def test_game_has_players():
    state = [[],[],[]]
    max_players = 2
    board = Board(state)
    player1 = Player('O')
    game = Game(board, max_players)
    breakpoint()
    game.player(player1)
    breakpoint()
    assert game.player == [player]

