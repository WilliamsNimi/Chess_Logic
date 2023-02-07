import util_constants

squares = util_constants.squares
castling_rooks_map = util_constants.castling_rooks_map

def is_castling_move(move):
    x_diff = squares[move[1]][0] - squares[move[2]][0]
    if(len(move[0])!=2 or x_diff not in [2, -2]):
        return []
    if(move[0][1].lower()!='k'):
        return []
    castling_direction = '+ve' if x_diff == 2 else '-ve'
    return castling_rooks_map[move[0][0].lower() + castling_direction]


def is_empty_square(board, square):
    return board[square][2] == ""

def castling_check(color, direction, board, forbidden_squares):
    squares_to_check_dict = util_constants.squares_to_check_dict
    valid_castling_square_dict = util_constants.valid_castling_square_dict

    for index, square_to_check in enumerate(squares_to_check_dict[color.lower()+direction]):
        if(index < 2 and square_to_check in forbidden_squares):
            return ''
        if(not is_empty_square(board, square_to_check)):
            return ''
    return valid_castling_square_dict[color.lower()+direction]