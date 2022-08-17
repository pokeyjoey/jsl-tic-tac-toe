class Move:

    def __init__(self, store, game,  player):
        self._store = store
        self._game = game
        self._player = player
        self._x_coordinate = None
        self._y_coordinate = None

    @property
    def x_coordinate(self):
        return self._x_coordinate

    @x_coordinate.setter
    def x_coordinate(self, x_coordinate):
        self._x_coordinate = x_coordinate

    @property
    def y_coordinate(self):
        return self._y_coordinate

    @y_coordinate(self, y_coordinate):
        self._y_coordinate = y_coordinate

