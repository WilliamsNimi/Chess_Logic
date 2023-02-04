import utils_valid_moves_specific
import utils_threatened_squares_specific

def add_valid_moves_to_dict(origin_squares_list, destination_square, valid_moves_dict):
    for origin_square in origin_squares_list:
        if origin_square in valid_moves_dict:
            valid_moves_dict[origin_square].append(destination_square)
        else:
            valid_moves_dict[origin_square] = [destination_square]

def valid_moves_when_in_check(king_square, color, current_board, pinned_squares_map, attacking_squares):
    """
    This function accepts the king's square and the pieces attackng the king
    and returns either a dictionary of valid moves (originating and destination squares)
    or an empty dictionary, in which case, the other piece has checkmated.
    """
    valid_check_response_moves = {}
    if(len(attacking_squares) == 1):
        #Check if piece on attacking square can be captured
        attacking_square = attacking_squares[0]
        attacking_square_details = utils_threatened_squares_specific.extract_piece_name_and_color(current_board[attacking_square][2])
        valid_moves_for_all_opponent_color_pieces = utils_valid_moves_specific.all_valid_opponent_piece_moves(color, current_board, pinned_squares_map)
        pieces_that_can_capture = utils_threatened_squares_specific.find_attackers(attacking_square, valid_moves_for_all_opponent_color_pieces)
        if(len(pieces_that_can_capture) > 0):
            add_valid_moves_to_dict(pieces_that_can_capture, attacking_square, valid_check_response_moves)
        #Evaluate whether check can be blocked
        if(attacking_square_details["name"] in ["q", "r", "b"]):
            (king_x_coord, king_y_coord) = utils_threatened_squares_specific.squares[king_square]
            (attacker_x_coord, attacker_y_coord) = utils_threatened_squares_specific.squares[attacking_square]
            x_diff = king_x_coord - attacker_x_coord
            y_diff = king_y_coord - attacker_y_coord
            if(x_diff > 0 or y_diff > 0):
                max_diff = max(abs(x_diff), abs(y_diff))
                for n in range(1, max_diff):
                    current_x_coord = int(king_x_coord - ((x_diff/max_diff)*n))
                    current_y_coord = int(king_y_coord - ((y_diff/max_diff)*n))
                    current_blockable_square = utils_threatened_squares_specific.inverted_squares_map[str(current_x_coord) + ',' + str(current_y_coord)]
                    pieces_that_can_block = utils_threatened_squares_specific.find_attackers(current_blockable_square, valid_moves_for_all_opponent_color_pieces)
                    if(len(pieces_that_can_block) > 0):
                        add_valid_moves_to_dict(pieces_that_can_block, current_blockable_square, valid_check_response_moves)
    #Check if the king has any safe spaces to move to
    king_safe_squares = utils_valid_moves_specific.king_move_valid_squares(king_square, current_board, utils_threatened_squares_specific.flatten_a_dictionary_of_arrays(utils_threatened_squares_specific.all_threatened_and_defended_squares(current_board, color)))
    if len(king_safe_squares) > 0:
        valid_check_response_moves[king_square] = king_safe_squares
    return valid_check_response_moves
            


# sampleBoard1 = {'a1': [0, 0, 'WQR'], 'b1': [1, 0, 'WQN'], 'c1': [2, 0, 'WQB'], 'd1': [3, 0, ''], 'e1': [4, 0, 'WK'], 'f1': [5, 0, 'WKB'], 'g1': [6, 0, 'WKN'], 'h1': [7, 0, 'WKR'], 
#                'a2': [0, 1, 'Wp1'], 'b2': [1, 1, 'Wp2'], 'c2': [2, 1, 'Wp3'], 'd2': [3, 1, 'Wp4'], 'e2': [4, 1, ''], 'f2': [5, 1, 'Wp6'], 'g2': [6, 1, 'Wp7'], 'h2': [7, 1, 'Wp8'], 
#                'a3': [0, 2, ''], 'b3': [1, 2, ''], 'c3': [2, 2, ''], 'd3': [3, 2, ''], 'e3': [4, 2, ''], 'f3': [5, 2, ''], 'g3': [6, 2, ''], 'h3': [7, 2, ''], 
#                'a4': [0, 3, ''], 'b4': [1, 3, ''], 'c4': [2, 3, ''], 'd4': [3, 3, ''], 'e4': [4, 3, ''], 'f4': [5, 3, ''], 'g4': [6, 3, ''], 'h4': [7, 3, ''], 
#                'a5': [0, 4, 'Bp8'], 'b5': [1, 4, ''], 'c5': [2, 4, ''], 'd5': [3, 4, ''], 'e5': [4, 4, 'WQ'], 'f5': [5, 4, 'Wp5'], 'g5': [6, 4, ''], 'h5': [7, 4, ''], 
#                'a6': [0, 5, ''], 'b6': [1, 5, ''], 'c6': [2, 5, ''], 'd6': [3, 5, ''], 'e6': [4, 5, ''], 'f6': [5, 5, ''], 'g6': [6, 5, ''], 'h6': [7, 5, ''], 
#                'a7': [0, 6, ''], 'b7': [1, 6, 'Bp7'], 'c7': [2, 6, 'Bp6'], 'd7': [3, 6, 'Bp5'], 'e7': [4, 6, ''], 'f7': [5, 6, ''], 'g7': [6, 6, 'Bp2'], 'h7': [7, 6, 'Bp1'], 
#                'a8': [0, 7, 'BQR'], 'b8': [1, 7, 'BQN'], 'c8': [2, 7, 'BQB'], 'd8': [3, 7, 'BQ'], 'e8': [4, 7, 'BK'], 'f8': [5, 7, 'BKB'], 'g8': [6, 7, 'BKN'], 'h8': [7, 7, 'BKR']}

# sampleCurrentColor = 'b'

# sampleAttackingSquares1 = ['e5']

# samplePinnedSquaresMap = {}

# sampleKingSquare = 'e8'

# sampleBoard = {'a1': [0, 0, 'WQR'], 'b1': [1, 0, 'WQN'], 'c1': [2, 0, 'WQB'], 'd1': [3, 0, ''], 'e1': [4, 0, 'WK'], 'f1': [5, 0, ''], 'g1': [6, 0, 'WKN'], 'h1': [7, 0, 'WKR'], 
#                'a2': [0, 1, 'Wp1'], 'b2': [1, 1, 'Wp2'], 'c2': [2, 1, 'Wp3'], 'd2': [3, 1, 'Wp4'], 'e2': [4, 1, ''], 'f2': [5, 1, 'Wp6'], 'g2': [6, 1, 'Wp7'], 'h2': [7, 1, 'Wp8'], 
#                'a3': [0, 2, ''], 'b3': [1, 2, ''], 'c3': [2, 2, ''], 'd3': [3, 2, ''], 'e3': [4, 2, ''], 'f3': [5, 2, ''], 'g3': [6, 2, ''], 'h3': [7, 2, ''], 
#                'a4': [0, 3, ''], 'b4': [1, 3, ''], 'c4': [2, 3, 'WKB'], 'd4': [3, 3, ''], 'e4': [4, 3, 'Wp5'], 'f4': [5, 3, ''], 'g4': [6, 3, ''], 'h4': [7, 3, ''], 
#                'a5': [0, 4, ''], 'b5': [1, 4, ''], 'c5': [2, 4, ''], 'd5': [3, 4, ''], 'e5': [4, 4, 'Bp4'], 'f5': [5, 4, ''], 'g5': [6, 4, ''], 'h5': [7, 4, ''], 
#                'a6': [0, 5, ''], 'b6': [1, 5, ''], 'c6': [2, 5, ''], 'd6': [3, 5, ''], 'e6': [4, 5, ''], 'f6': [5, 5, 'BKN'], 'g6': [6, 5, ''], 'h6': [7, 5, 'Bp1'], 
#                'a7': [0, 6, 'Bp8'], 'b7': [1, 6, 'Bp7'], 'c7': [2, 6, 'Bp6'], 'd7': [3, 6, 'Bp5'], 'e7': [4, 6, ''], 'f7': [5, 6, 'WQ'], 'g7': [6, 6, 'Bp2'], 'h7': [7, 6, ''], 
#                'a8': [0, 7, 'BQR'], 'b8': [1, 7, 'BQN'], 'c8': [2, 7, 'BQB'], 'd8': [3, 7, 'BQ'], 'e8': [4, 7, 'BK'], 'f8': [5, 7, 'BKB'], 'g8': [6, 7, ''], 'h8': [7, 7, 'BKR']}

# sampleAttackingSquares = ['f7']

# print(valid_moves_when_in_check(sampleKingSquare, sampleCurrentColor, sampleBoard, samplePinnedSquaresMap, sampleAttackingSquares))
