class Game:

    def __init__(self, store, board, players):
        self._board = board
        self._players = players

    @property
    def players(self):
        return self._players

    @player.setter
    def player(self, player):
        # Add a player to the game if we have not reached maximum number
        if (len(self._players) < self._max_players):
            self._players.append(player)
        else:
            print('maximum number of players reached')

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        self._board = board
