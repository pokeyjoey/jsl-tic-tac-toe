class Board:

    #def __init__(self, store, game):
    #   self._store = store
    #   self._game = game
    def __init__(self, state):
        self.state = state

    def winner(self):
        if self._winner('O'):
            return 'O'
        elif self._winner('X'):
            return 'X'
        elif self._neither_has_won():
            return 'N/A'
        elif self._its_a_tie():
            return 'tie'

    def _list_of_all_entries(self):
        # combine the rows into one list so we can coumt the entries
        full_list = []
        for row in self.state:
            for entry in row:
                full_list.append(entry)

        return full_list

    def _neither_has_won(self):
        # count the number of entries of X and O
        # - if the total count is less than the
        #   total number of positions in the board,
        #   then there are still spots to play
        full_list_of_entries = self._list_of_all_entries()
        X_count = full_list_of_entries.count('X')
        O_count = full_list_of_entries.count('O')
        if (X_count + O_count) < 9:
            return True

        return False

    def _its_a_tie(self):
        # count the number of entries of X and O
        # - if the total count is equal to the
        #   total number of positions in the board,
        #   then there are no more spots to play
        full_list_of_entries = self._list_of_all_entries()
        X_count = full_list_of_entries.count('X')
        O_count = full_list_of_entries.count('O')
        if (X_count + O_count) == 9:
            return True

        return False

    def _horizontal_winner(self, entry):
        for row in self.state:
            if row.count(entry) == 3:
                return True

        return False

    def _vertical_winner(self, entry):
        for index in range(0, 3):
            test_list = [self.state[0][index], self.state[1][index], self.state[2][index]]
            if test_list.count(entry) == 3:
                return True

        return False

    def _right_diagonal_winner(self, entry):
        test_list = [self.state[0][0], self.state[1][1], self.state[2][2]]

        return True if test_list.count(entry) == 3 else False

    def _left_diagonal_winner(self, entry):
        test_list = [self.state[0][2], self.state[1][1], self.state[2][0]]

        return True if test_list.count(entry) == 3 else False

    def _winner(self, entry):
        winner = self._vertical_winner(entry) or \
                 self._horizontal_winner(entry) or \
                 self._right_diagonal_winner(entry) or \
                 self._left_diagonal_winner(entry)
        return winner

