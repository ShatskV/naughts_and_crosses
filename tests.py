from main import NaughtsAndCrosses


def test_check_row():
    game = NaughtsAndCrosses(3)
    assert game.check_row([['X', 'X', 'X'], ['_', '_', '_'], ['_', '_', '_']], 'X', 3) == 'X'
    assert game.check_row([['_', '_', '_'], ['O', 'O', 'O'], ['_', '_', '_']], 'O', 3) == 'O'


def test_check_winner_row_and_col():
    game = NaughtsAndCrosses(3)

    game.field = [['X', 'X', 'X'], ['_', '_', '_'], ['_', '_', '_']]
    assert 'X' == game.check_winner_in_rows_and_columns()
    
    game.field = [['O', 'O', 'X'], ['O', 'O', '_'], ['O', 'O', '_']]
    assert 'O' == game.check_winner_in_rows_and_columns()
    
    game.field = [['O', 'X', 'X'], ['O', '_', '_'], ['O', '_', '_']]
    assert 'O' == game.check_winner_in_rows_and_columns()

    game.field = [['O', 'X', 'X'], ['O', '_', '_'], ['X', '_', '_']]
    assert None == game.check_winner_in_rows_and_columns()


def test_check_winner_in_diagonals():
    game = NaughtsAndCrosses(3)

    game.field = [['X', 'X', 'X'], ['_', 'X', '_'], ['_', '_', 'X']]
    assert 'X' == game.check_winner_in_diagonals()

    game.field = [['X', '_', 'O'], ['_', 'O', '_'], ['O', '_', 'X']]
    assert 'O' == game.check_winner_in_diagonals()

    game.field = [['X', 'X', 'X'], ['_', 'O', 'O'], ['_', '_', 'X']]
    assert None == game.check_winner_in_diagonals()


def test_check_winner():
    game = NaughtsAndCrosses(3)
    game.field = [['X', 'X', 'X'], ['_', 'X', '_'], ['_', '_', 'X']]
    assert 'X' == game.check_winner()
    game.field = [['X', '_', 'O'], ['_', 'O', '_'], ['_', '_', 'X']]
    assert None == game.check_winner()
    game.field = [['X', '_', 'O'], ['X', 'O', 'O'], ['_', '_', 'O']]    
    assert 'O' == game.check_winner()
    game.field = [['X', '_', 'O'], ['O', 'X', 'O'], ['X', '_', 'X']]    
    assert 'X' == game.check_winner()
    game.field = [['X', '_', 'O'], ['X', 'O', 'O'], ['O', '_', 'O']]  
    assert 'O' == game.check_winner()


def test_field_size():
    game = NaughtsAndCrosses(5)
    print(game.field)
    assert game.field == [['_', '_', '_', '_','_'] for _ in range(5)]

    game = NaughtsAndCrosses(3)
    print(game.field)
    assert game.field == [['_', '_', '_'] for _ in range(3)]


def test_free_positions():
    game = NaughtsAndCrosses(3)
    game.field = [['X', '_', 'X'], ['_', 'X', '_'],['_', '_', '_']]
    assert game.free_positions == [[1, 0], [2, 0], [0, 1], [2, 1], [1, 2], [2, 2]]

    game.field = [['X', 'X', '_'], ['_', 'X', '_'],['_', 'X', '_']]
    assert game.free_positions == [[1, 0], [2, 0], [0, 2], [1, 2], [2, 2]]


def test_reset_game():
    game = NaughtsAndCrosses(3)
    game.field = [['X', 'X', '_'], ['_', 'X', '_'], ['_', 'X', '_']]
    game.current_turn = 'O'
    game.reset_game()
    assert game.field == [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    assert game.current_turn == 'X'
