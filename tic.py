import itertools

def is_legal(move, moves_played):
   return move > -1 and move < 9 and move not in moves_played

def moves_for_player(player, moves_played):
    number_of_players = 2
    return moves_played[player::number_of_players]

def test_first_player_wins():
    game_moves = [0, 3, 1, 5, 2]
    assert last_move_wins(game_moves) is True

def test_second_player_wins():
    game_moves = [4, 0, 3, 1, 8, 2]
    assert last_move_wins(game_moves) is True

def is_win(player_moves):
    combos = itertools.combinations(player_moves, 3)
    winning_moves = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any([sorted(combo) in winning_moves for combo in combos])

def last_player(moves_played):
    return (len(moves_played) + 1) % 2

def last_move_wins(moves_played):
    player = last_player(moves_played)
    player_moves = moves_for_player(player, moves_played)
    return is_win(player_moves)
