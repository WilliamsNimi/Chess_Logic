"""
TO-DO:
1/ Rewrite Pawn, King, and Knight logic with a for or while loop. Too verbose.
2/ Track all moves and store board position before and after
"""

squares = {"a1":(0,0),"b1":(1,0),"c1":(2,0),"d1":(3,0),"e1":(4,0),"f1":(5,0),"g1":(6,0),"h1":(7,0),"a2":(0,1),"b2":(1,1),"c2":(2,1),"d2":(3,1),"e2":(4,1),"f2":(5,1),"g2":(6,1),"h2":(7,1),"a3":(0,2),"b3":(1,2),"c3":(2,2),"d3":(3,2),"e3":(4,2),"f3":(5,2),"g3":(6,2),"h3":(7,2),"a4":(0,3),"b4":(1,3),"c4":(2,3),"d4":(3,3),"e4":(4,3),"f4":(5,3),"g4":(6,3),"h4":(7,3),"a5":(0,4),"b5":(1,4),"c5":(2,4),"d5":(3,4),"e5":(4,4),"f5":(5,4),"g5":(6,4),"h5":(7,4),"a6":(0,5),"b6":(1,5),"c6":(2,5),"d6":(3,5),"e6":(4,5),"f6":(5,5),"g6":(6,5),"h6":(7,5),"a7":(0,6),"b7":(1,6),"c7":(2,6),"d7":(3,6),"e7":(4,6),"f7":(5,6),"g7":(6,6),"h7":(7,6),"a8":(0,7),"b8":(1,7),"c8":(2,7),"d8":(3,7),"e8":(4,7),"f8":(5,7),"g8":(6,7),"h8":(7,7)}
inverted_squares_map = {'0,0': 'a1', '1,0': 'b1', '2,0': 'c1', '3,0': 'd1', '4,0': 'e1', '5,0': 'f1', '6,0': 'g1', '7,0': 'h1', '0,1': 'a2', '1,1': 'b2', '2,1': 'c2', '3,1': 'd2', '4,1': 'e2', '5,1': 'f2', '6,1': 'g2', '7,1': 'h2', '0,2': 'a3', '1,2': 'b3', '2,2': 'c3', '3,2': 'd3', '4,2': 'e3', '5,2': 'f3', '6,2': 'g3', '7,2': 'h3', '0,3': 'a4', '1,3': 'b4', '2,3': 'c4', '3,3': 'd4', '4,3': 'e4', '5,3': 'f4', '6,3': 'g4', '7,3': 'h4', '0,4': 'a5', '1,4': 'b5', '2,4': 'c5', '3,4': 'd5', '4,4': 'e5', '5,4': 'f5', '6,4': 'g5', '7,4': 'h5', '0,5': 'a6', '1,5': 'b6', '2,5': 'c6', '3,5': 'd6', '4,5': 'e6', '5,5': 'f6', '6,5': 'g6', '7,5': 'h6', '0,6': 'a7', '1,6': 'b7', '2,6': 'c7', '3,6': 'd7', '4,6': 'e7', '5,6': 'f7', '6,6': 'g7', '7,6': 'h7', '0,7': 'a8', '1,7': 'b8', '2,7': 'c8', '3,7': 'd8', '4,7': 'e8', '5,7': 'f8', '6,7': 'g8', '7,7': 'h8'}

from utils_threatened_squares_specific import normalized_arithmetic, isValidBoardCoordinates

def pawn_move_validity(current_position, current_board):
    pawn_threats = []
    x_coord = squares[current_position][0]
    y_coord = squares[current_position][1]
    color = current_board[current_position][2][0]
    base_row_dict = {"w": 1, "b": 6}
    PAWN_HAS_NOT_MOVED = y_coord == base_row_dict[str(color).lower()]
    first_square_ahead_y_coord = normalized_arithmetic(color, "sum", y_coord, 1)
    first_square_ahead_is_valid = isValidBoardCoordinates(x_coord, first_square_ahead_y_coord)
    first_square_ahead_position = inverted_squares_map[str(x_coord)+','+str(first_square_ahead_y_coord)] if first_square_ahead_is_valid else 'invalid_square'
    first_square_ahead_piece = current_board[first_square_ahead_position][2] if first_square_ahead_is_valid else 'invalid_piece'
    second_square_ahead_y_coord = normalized_arithmetic(color, "sum", y_coord, 2)
    second_square_ahead_is_valid = isValidBoardCoordinates(x_coord, second_square_ahead_y_coord)
    second_square_ahead_position = inverted_squares_map[str(x_coord)+','+str(second_square_ahead_y_coord)] if second_square_ahead_is_valid else 'invalid_square'
    second_square_ahead_piece = current_board[second_square_ahead_position][2] if second_square_ahead_is_valid else 'invalid_piece'
    if(first_square_ahead_is_valid and len(first_square_ahead_piece)==0):
        pawn_threats.append(first_square_ahead_position)
        if(second_square_ahead_is_valid and PAWN_HAS_NOT_MOVED and len(second_square_ahead_piece) == 0):
            pawn_threats.append(second_square_ahead_position)
    top_right_x_coord = normalized_arithmetic(color, "sum", x_coord, 1)
    top_right_y_coord = normalized_arithmetic(color, "sum", y_coord, 1)
    top_left_x_coord = normalized_arithmetic(color, "diff", x_coord, 1)
    top_left_y_coord = normalized_arithmetic(color, "sum", y_coord, 1)
    top_right_square_is_valid = isValidBoardCoordinates(top_right_x_coord, top_right_y_coord)
    top_left_square_is_valid = isValidBoardCoordinates(top_left_x_coord, top_left_y_coord)
     #using ternary operator to prevent key error when the coordinates are invalid
    right_target_position = inverted_squares_map[str(top_right_x_coord)+','+str(top_right_y_coord)] if top_right_square_is_valid else 'invalid_square'
    left_target_position = inverted_squares_map[str(top_left_x_coord)+','+str(top_left_y_coord)] if top_left_square_is_valid else 'invalid_square'
    right_target_piece = current_board[right_target_position][2] if top_right_square_is_valid else 'invalid_piece'
    left_target_piece = current_board[left_target_position][2] if top_left_square_is_valid else 'invalid_piece'

    #Check if the top right square is valid, empty or of a different color
    if(top_right_square_is_valid and len(right_target_piece)>=1 and right_target_piece[0]!=color):
        pawn_threats.append(right_target_position)
    #Check if the top left square is valid, empty or of a different color
    if(top_left_square_is_valid and len(left_target_piece)>=1 and left_target_piece[0]!=color):
        pawn_threats.append(left_target_position)

    return pawn_threats

def knight_move_validity(current_position, current_board):
    """
    The knight has 8 potentially valid destination squares it can attack.
    We'll check each of these to see if they're:
    1. On the board
    2. Are occupied by any pieces (and the color of the occupying piece)
    3. Determine based on 1 and 2 whether the square is threatened by the knight
    """
    knight_threats = []
    x_coord = squares[current_position][0]
    y_coord = squares[current_position][1]
    color = current_board[current_position][2][0]
    top_near_right_x_coord = normalized_arithmetic(color, "sum", x_coord, 2)
    top_near_right_y_coord = normalized_arithmetic(color, "sum", y_coord, 1)
    top_far_right_x_coord = normalized_arithmetic(color, "sum", x_coord, 1)
    top_far_right_y_coord = normalized_arithmetic(color, "sum", y_coord, 2)
    top_near_left_x_coord = normalized_arithmetic(color, "diff", x_coord, 2)
    top_near_left_y_coord = normalized_arithmetic(color, "sum", y_coord, 1)
    top_far_left_x_coord = normalized_arithmetic(color, "diff", x_coord, 1)
    top_far_left_y_coord = normalized_arithmetic(color, "sum", y_coord, 2)
    bottom_near_right_x_coord = normalized_arithmetic(color, "sum", x_coord, 2)
    bottom_near_right_y_coord = normalized_arithmetic(color, "diff", y_coord, 1)
    bottom_far_right_x_coord = normalized_arithmetic(color, "sum", x_coord, 1)
    bottom_far_right_y_coord = normalized_arithmetic(color, "diff", y_coord, 2)
    bottom_near_left_x_coord = normalized_arithmetic(color, "diff", x_coord, 2)
    bottom_near_left_y_coord = normalized_arithmetic(color, "diff", y_coord, 1)
    bottom_far_left_x_coord = normalized_arithmetic(color, "diff", x_coord, 1)
    bottom_far_left_y_coord = normalized_arithmetic(color, "diff", y_coord, 2)


    #Check if potential target squares are present on the board
    top_near_right_square_is_valid = isValidBoardCoordinates(top_near_right_x_coord, top_near_right_y_coord)
    top_far_right_square_is_valid = isValidBoardCoordinates(top_far_right_x_coord, top_far_right_y_coord)
    top_near_left_square_is_valid = isValidBoardCoordinates(top_near_left_x_coord, top_near_left_y_coord)
    top_far_left_square_is_valid = isValidBoardCoordinates(top_far_left_x_coord,top_far_left_y_coord)
    bottom_near_right_square_is_valid = isValidBoardCoordinates(bottom_near_right_x_coord, bottom_near_right_y_coord)
    bottom_far_right_square_is_valid = isValidBoardCoordinates(bottom_far_right_x_coord, bottom_far_right_y_coord)
    bottom_near_left_square_is_valid = isValidBoardCoordinates(bottom_near_left_x_coord, bottom_near_left_y_coord)
    bottom_far_left_square_is_valid = isValidBoardCoordinates(bottom_far_left_x_coord, bottom_far_left_y_coord)

    #map potential target square coordinates to a board position in standard chess notation
    top_near_right_target_position = inverted_squares_map[str(top_near_right_x_coord)+','+str(top_near_right_y_coord)] if top_near_right_square_is_valid else 'invalid_square'
    top_far_right_target_position = inverted_squares_map[str(top_far_right_x_coord)+','+str(top_far_right_y_coord)] if top_far_right_square_is_valid else 'invalid_square'
    top_near_left_target_position = inverted_squares_map[str(top_near_left_x_coord)+','+str(top_near_left_y_coord)] if top_near_left_square_is_valid else 'invalid_square'
    top_far_left_target_position = inverted_squares_map[str(top_far_left_x_coord)+','+str(top_far_left_y_coord)] if top_far_left_square_is_valid else 'invalid_square'
    bottom_near_right_target_position = inverted_squares_map[str(bottom_near_right_x_coord)+','+str(bottom_near_right_y_coord)] if bottom_near_right_square_is_valid else 'invalid_square'
    bottom_far_right_target_position = inverted_squares_map[str(bottom_far_right_x_coord)+','+str(bottom_far_right_y_coord)] if bottom_far_right_square_is_valid else 'invalid_square'
    bottom_near_left_target_position = inverted_squares_map[str(bottom_near_left_x_coord)+','+str(bottom_near_left_y_coord)] if bottom_near_left_square_is_valid else 'invalid_square'
    bottom_far_left_target_position = inverted_squares_map[str(bottom_far_left_x_coord)+','+str(bottom_far_left_y_coord)] if bottom_far_left_square_is_valid else 'invalid_square'
    #check which piece if any is occupying the potential target squares
    top_near_right_target_piece = current_board[top_near_right_target_position][2] if top_near_right_square_is_valid else 'invalid_piece'
    top_far_right_target_piece = current_board[top_far_right_target_position][2] if top_far_right_square_is_valid else 'invalid_piece'
    top_near_left_target_piece = current_board[top_near_left_target_position][2] if top_near_left_square_is_valid else 'invalid_piece'
    top_far_left_target_piece = current_board[top_far_left_target_position][2] if top_far_left_square_is_valid else 'invalid_piece'
    bottom_near_right_target_piece = current_board[bottom_near_right_target_position][2] if bottom_near_right_square_is_valid else 'invalid_piece'
    bottom_far_right_target_piece = current_board[bottom_far_right_target_position][2] if bottom_far_right_square_is_valid else 'invalid_piece'
    bottom_near_left_target_piece = current_board[bottom_near_left_target_position][2] if bottom_near_left_square_is_valid else 'invalid_piece'
    bottom_far_left_target_piece = current_board[bottom_far_left_target_position][2] if bottom_far_left_square_is_valid else 'invalid_piece'

    if(top_near_right_square_is_valid and len(top_near_right_target_piece)==0):
        knight_threats.append(top_near_right_target_position)
    if(top_near_right_square_is_valid and len(top_near_right_target_piece)>=1 and top_near_right_target_piece[0]!=color):
        knight_threats.append(top_near_right_target_position)

    if(top_far_right_square_is_valid and len(top_far_right_target_piece)==0):
        knight_threats.append(top_far_right_target_position)
    if(top_far_right_square_is_valid and len(top_far_right_target_piece)>=1 and top_far_right_target_piece[0]!=color):
        knight_threats.append(top_far_right_target_position)

    if(top_near_left_square_is_valid and len(top_near_left_target_piece)==0):
        knight_threats.append(top_near_left_target_position)
    if(top_near_left_square_is_valid and len(top_near_left_target_piece)>=1 and top_near_left_target_piece[0]!=color):
        knight_threats.append(top_near_left_target_position)

    if(top_far_left_square_is_valid and len(top_far_left_target_piece)==0):
        knight_threats.append(top_far_left_target_position)
    if(top_far_left_square_is_valid and len(top_far_left_target_piece)>=1 and top_far_left_target_piece[0]!=color):
        knight_threats.append(top_far_left_target_position)

    if(bottom_near_right_square_is_valid and len(bottom_near_right_target_piece)==0):
        knight_threats.append(bottom_near_right_target_position)
    if(bottom_near_right_square_is_valid and len(bottom_near_right_target_piece)>=1 and bottom_near_right_target_piece[0]!=color):
        knight_threats.append(bottom_near_right_target_position)

    if(bottom_far_right_square_is_valid and len(bottom_far_right_target_piece)==0):
        knight_threats.append(bottom_far_right_target_position)
    if(bottom_far_right_square_is_valid and len(bottom_far_right_target_piece)>=1 and bottom_far_right_target_piece[0]!=color):
        knight_threats.append(bottom_far_right_target_position)

    if(bottom_near_left_square_is_valid and len(bottom_near_left_target_piece)==0):
        knight_threats.append(bottom_near_left_target_position)
    if(bottom_near_left_square_is_valid and len(bottom_near_left_target_piece)>=1 and bottom_near_left_target_piece[0]!=color):
        knight_threats.append(bottom_near_left_target_position)

    if(bottom_far_left_square_is_valid and len(bottom_far_left_target_piece)==0):
        knight_threats.append(bottom_far_left_target_position)
    if(bottom_far_left_square_is_valid and len(bottom_far_left_target_piece)>=1 and bottom_far_left_target_piece[0]!=color):
        knight_threats.append(bottom_far_left_target_position)
    
    return knight_threats

def rook_move_validity(current_position, current_board):
    """
    A rook can potentially attack in 4 vertical directions (+x, -x, +y, -y).
    We'll check each of these directions for move_validity and occupation
    Returns a dictionary with key attacking color and value as a list of threatened squares
    """
    rook_threats = []
    x_coord = squares[current_position][0]
    y_coord = squares[current_position][1]
    color = current_board[current_position][2][0]

    #+x direction
    for dx_up in range(1,8):
        x_coord_up = normalized_arithmetic(color, "sum", x_coord, dx_up)
        this_square_is_valid = isValidBoardCoordinates(x_coord_up, y_coord)
        target_position = inverted_squares_map[str(x_coord_up)+','+str(y_coord)] if this_square_is_valid else 'invalid_square'
        target_piece = current_board[target_position][2] if this_square_is_valid else 'invalid_piece'
        if(not this_square_is_valid):
            break
        if(this_square_is_valid and len(target_piece)==0):
            rook_threats.append(target_position)
            continue
        if(this_square_is_valid and len(target_piece) >= 1 and target_piece[0] == color):
            break
        if(this_square_is_valid and len(target_piece) >= 1 and target_piece[0] != color):
            rook_threats.append(target_position)
            break
    
    #-x direction
    for dx_down in range(1,8):
        x_coord_down = normalized_arithmetic(color, "diff", x_coord, dx_down)
        this_square_is_valid = isValidBoardCoordinates(x_coord_down, y_coord)
        target_position = inverted_squares_map[str(x_coord_down)+','+str(y_coord)] if this_square_is_valid else 'invalid_square'
        target_piece = current_board[target_position][2] if this_square_is_valid else 'invalid_piece'
        if(not this_square_is_valid):
            break
        if(this_square_is_valid and len(target_piece)==0):
            rook_threats.append(target_position)
            continue
        if(this_square_is_valid and len(target_piece) >= 1 and target_piece[0] == color):
            break
        if(this_square_is_valid and len(target_piece) >= 1 and target_piece[0] != color):
            rook_threats.append(target_position)
            break

    #+y direction
    for dy_up in range(1,8):
        y_coord_up = normalized_arithmetic(color, "sum", y_coord, dy_up)
        this_square_is_valid = isValidBoardCoordinates(x_coord, y_coord_up)
        target_position = inverted_squares_map[str(x_coord)+','+str(y_coord_up)] if this_square_is_valid else 'invalid_square'
        target_piece = current_board[target_position][2] if this_square_is_valid else 'invalid_piece'
        if(not this_square_is_valid):
            break
        if(this_square_is_valid and len(target_piece)==0):
            rook_threats.append(target_position)
            continue
        if(this_square_is_valid and len(target_piece) >= 1 and target_piece[0] == color):
            break
        if(this_square_is_valid and len(target_piece) >= 1 and target_piece[0] != color):
            rook_threats.append(target_position)
            break

    #-y direction
    for dy_down in range(1,8):
        y_coord_down = normalized_arithmetic(color, "diff", y_coord, dy_down)
        this_square_is_valid = isValidBoardCoordinates(x_coord, y_coord_down)
        target_position = inverted_squares_map[str(x_coord)+','+str(y_coord_down)] if this_square_is_valid else 'invalid_square'
        target_piece = current_board[target_position][2] if this_square_is_valid else 'invalid_piece'
        if(not this_square_is_valid):
            break
        if(this_square_is_valid and len(target_piece)==0):
            rook_threats.append(target_position)
            continue
        if(this_square_is_valid and len(target_piece) >= 1 and target_piece[0] == color):
            break
        if(this_square_is_valid and len(target_piece) >= 1 and target_piece[0] != color):
            rook_threats.append(target_position)
            break
    return rook_threats

def bishop_move_validity(current_position, current_board, include_defended_squares=False):
    """
    A Bishop can potentially attack in 4 diagonal directions (z_up_right(1:15 on a clock), z_down_right(4:15 on a clock), 
    z_up_left(10:15 on a clock), z_down_left(7:15 on a clock)).
    We'll check each of these directions for move_validity and occupation
    """
    bishop_threats = []
    x_coord = squares[current_position][0]
    y_coord = squares[current_position][1]
    color = current_board[current_position][2][0]

    #1:15 direction
    for dz_up_right in range(1,8):
        x_coord_up_right = normalized_arithmetic(color, "sum", x_coord, dz_up_right)
        y_coord_up_right = normalized_arithmetic(color, "sum", y_coord, dz_up_right)
        this_square_is_valid = isValidBoardCoordinates(x_coord_up_right, y_coord_up_right)
        target_position = inverted_squares_map[str(x_coord_up_right)+','+str(y_coord_up_right)] if this_square_is_valid else 'invalid_square'
        target_piece = current_board[target_position][2] if this_square_is_valid else 'invalid_piece'
        if(not this_square_is_valid):
            break
        if(this_square_is_valid and len(target_piece)==0):
            bishop_threats.append(target_position)
            continue
        if(this_square_is_valid and len(target_piece) >= 1 and target_piece[0] == color):
            if(include_defended_squares):
                bishop_threats.append(target_position)
            break
        if(this_square_is_valid and len(target_piece) >= 1 and target_piece[0] != color):
            bishop_threats.append(target_position)
            break
    
    #4:15 direction
    for dz_down_right in range(1,8):
        x_coord_down_right = normalized_arithmetic(color, "sum", x_coord, dz_down_right)
        y_coord_down_right = normalized_arithmetic(color, "diff", y_coord, dz_down_right)
        this_square_is_valid = isValidBoardCoordinates(x_coord_down_right, y_coord_down_right)
        target_position = inverted_squares_map[str(x_coord_down_right)+','+str(y_coord_down_right)] if this_square_is_valid else 'invalid_square'
        target_piece = current_board[target_position][2] if this_square_is_valid else 'invalid_piece'
        if(not this_square_is_valid):
            break
        if(this_square_is_valid and len(target_piece)==0):
            bishop_threats.append(target_position)
            continue
        if(this_square_is_valid and len(target_piece) >= 1 and target_piece[0] == color):
            if(include_defended_squares):
                bishop_threats.append(target_position)
            break
        if(this_square_is_valid and len(target_piece) >= 1 and target_piece[0] != color):
            bishop_threats.append(target_position)
            break

    #10:15 direction
    for dz_up_left in range(1,8):
        x_coord_up_left = normalized_arithmetic(color, "diff", x_coord, dz_up_left)
        y_coord_up_left = normalized_arithmetic(color, "sum", y_coord, dz_up_left)
        this_square_is_valid = isValidBoardCoordinates(x_coord_up_left, y_coord_up_left)
        target_position = inverted_squares_map[str(x_coord_up_left)+','+str(y_coord_up_left)] if this_square_is_valid else 'invalid_square'
        target_piece = current_board[target_position][2] if this_square_is_valid else 'invalid_piece'
        if(not this_square_is_valid):
            break
        if(this_square_is_valid and len(target_piece)==0):
            bishop_threats.append(target_position)
            continue
        if(this_square_is_valid and len(target_piece) >= 1 and target_piece[0] == color):
            if(include_defended_squares):
                bishop_threats.append(target_position)
            break
        if(this_square_is_valid and len(target_piece) >= 1 and target_piece[0] != color):
            bishop_threats.append(target_position)
            break

    #7:15 direction
    for dz_down_left in range(1,8):
        x_coord_down_left = normalized_arithmetic(color, "diff", x_coord, dz_down_left)
        y_coord_down_left = normalized_arithmetic(color, "diff", y_coord, dz_down_left)
        this_square_is_valid = isValidBoardCoordinates(x_coord_down_left, y_coord_down_left)
        target_position = inverted_squares_map[str(x_coord_down_left)+','+str(y_coord_down_left)] if this_square_is_valid else 'invalid_square'
        target_piece = current_board[target_position][2] if this_square_is_valid else 'invalid_piece'
        if(not this_square_is_valid):
            break
        if(this_square_is_valid and len(target_piece)==0):
            bishop_threats.append(target_position)
            continue
        if(this_square_is_valid and len(target_piece) >= 1 and target_piece[0] == color):
            if(include_defended_squares):
                bishop_threats.append(target_position)
            break
        if(this_square_is_valid and len(target_piece) >= 1 and target_piece[0] != color):
            bishop_threats.append(target_position)
            break
    return bishop_threats

def queen_move_validity(current_position, current_board, include_defended_squares=False):

    """
    A Queen combines the moves of both the Bishop and Rook.
    We'll simply call the existing functions and combine their results
    """
    defended_squares_flag = include_defended_squares
    bishop_threats = bishop_move_validity(current_position, current_board, defended_squares_flag)
    rook_threats = rook_move_validity(current_position, current_board, defended_squares_flag)
    return bishop_threats + rook_threats

def king_move_validity(current_position, current_board, include_defended_squares=False):
    """
    The king has 8 potentially valid destination squares it can attack.
    We'll check each of these to see if they're:
    1. On the board
    2. Are occupied by any pieces (and the color of the occupying piece)
    3. Determine based on 1 and 2 whether the square is threatened by the knight
    """
    king_threats = []
    x_coord = squares[current_position][0]
    y_coord = squares[current_position][1]
    color = current_board[current_position][2][0]
    top_90_degrees_y_coord = normalized_arithmetic(color, "sum", y_coord, 1)
    top_45_degrees_left_x_coord = normalized_arithmetic(color, "sum", x_coord, 1)
    top_45_degrees_left_y_coord = normalized_arithmetic(color, "sum", y_coord, 1)
    right_90_degrees_x_coord = normalized_arithmetic(color, "sum", x_coord, 1)
    bottom_45_degrees_right_x_coord = normalized_arithmetic(color, "sum", x_coord, 1)
    bottom_45_degrees_right_y_coord = normalized_arithmetic(color, "diff", y_coord, 1)
    bottom_90_degrees_y_coord = normalized_arithmetic(color, "diff", y_coord, 1)
    bottom_45_degrees_left_x_coord = normalized_arithmetic(color, "diff", x_coord, 1)
    bottom_45_degrees_left_y_coord = normalized_arithmetic(color, "diff", y_coord, 1)
    left_90_degrees_x_coord = normalized_arithmetic(color, "diff", x_coord, 1)
    top_45_degrees_x_coord = normalized_arithmetic(color, "diff", x_coord, 1)
    top_45_degrees_y_coord = normalized_arithmetic(color, "sum", y_coord, 1)

    #Check if potential target squares are present on the board
    top_90_degrees_is_valid = isValidBoardCoordinates(x_coord, top_90_degrees_y_coord)
    top_45_degrees_right_is_valid = isValidBoardCoordinates(top_45_degrees_left_x_coord, top_45_degrees_left_y_coord)
    right_90_degrees_is_valid = isValidBoardCoordinates(right_90_degrees_x_coord, y_coord)
    bottom_45_degrees_right_is_valid = isValidBoardCoordinates(bottom_45_degrees_right_x_coord, bottom_45_degrees_right_y_coord)
    bottom_90_degrees_is_valid = isValidBoardCoordinates(x_coord, bottom_90_degrees_y_coord)
    bottom_45_degrees_left_is_valid = isValidBoardCoordinates(bottom_45_degrees_left_x_coord, bottom_45_degrees_left_y_coord)
    left_90_degrees_is_valid = isValidBoardCoordinates(left_90_degrees_x_coord, y_coord)
    top_45_degrees_left_is_valid = isValidBoardCoordinates(top_45_degrees_x_coord, top_45_degrees_y_coord)

    #map potential target square coordinates to a board position in standard chess notation
    top_90_degrees_target_position = inverted_squares_map[str(x_coord)+','+str(top_90_degrees_y_coord)] if top_90_degrees_is_valid else 'invalid_square'
    top_45_degrees_right_target_position = inverted_squares_map[str(top_45_degrees_left_x_coord)+','+str(top_45_degrees_left_y_coord)] if top_45_degrees_right_is_valid else 'invalid_square'
    right_90_degrees_target_position = inverted_squares_map[str(right_90_degrees_x_coord)+','+str(y_coord)] if right_90_degrees_is_valid else 'invalid_square'
    bottom_45_degrees_right_target_position = inverted_squares_map[str(bottom_45_degrees_right_x_coord)+','+str(bottom_45_degrees_right_y_coord)] if bottom_45_degrees_right_is_valid else 'invalid_square'
    bottom_90_degrees_target_position = inverted_squares_map[str(x_coord)+','+str(bottom_90_degrees_y_coord)] if bottom_90_degrees_is_valid else 'invalid_square'
    bottom_45_degrees_left_target_position = inverted_squares_map[str(bottom_45_degrees_left_x_coord)+','+str(bottom_45_degrees_left_y_coord)] if bottom_45_degrees_left_is_valid else 'invalid_square'
    left_90_degrees_target_position = inverted_squares_map[str(left_90_degrees_x_coord)+','+str(y_coord)] if left_90_degrees_is_valid else 'invalid_square'
    top_45_degrees_left_target_position = inverted_squares_map[str(top_45_degrees_x_coord)+','+str(top_45_degrees_y_coord)] if top_45_degrees_left_is_valid else 'invalid_square'

    if(include_defended_squares):
        if(top_90_degrees_is_valid):
            king_threats.append(top_90_degrees_target_position)
        if(top_45_degrees_right_is_valid):
            king_threats.append(top_45_degrees_right_target_position)
        if(right_90_degrees_is_valid):
            king_threats.append(right_90_degrees_target_position)
        if(bottom_45_degrees_right_is_valid):
            king_threats.append(bottom_45_degrees_right_target_position)
        if(bottom_90_degrees_is_valid):
            king_threats.append(bottom_90_degrees_target_position)
        if(bottom_45_degrees_left_is_valid):
            king_threats.append(bottom_45_degrees_left_target_position)
        if(left_90_degrees_is_valid):
            king_threats.append(left_90_degrees_target_position)
        if(top_45_degrees_left_is_valid):
            king_threats.append(top_45_degrees_left_target_position)

        return king_threats

    #check which piece if any is occupying the potential target squares
    top_90_degrees_target_piece = current_board[top_90_degrees_target_position][2] if top_90_degrees_is_valid else 'invalid_piece'
    top_45_degrees_right_target_piece = current_board[top_45_degrees_right_target_position][2] if top_45_degrees_right_is_valid else 'invalid_piece'
    right_90_degrees_target_piece = current_board[right_90_degrees_target_position][2] if right_90_degrees_is_valid else 'invalid_piece'
    bottom_45_degrees_right_target_piece = current_board[bottom_45_degrees_right_target_position][2] if bottom_45_degrees_right_is_valid else 'invalid_piece'
    bottom_90_degrees_target_piece = current_board[bottom_90_degrees_target_position][2] if bottom_90_degrees_is_valid else 'invalid_piece'
    bottom_45_degrees_left_target_piece = current_board[bottom_45_degrees_left_target_position][2] if bottom_45_degrees_left_is_valid else 'invalid_piece'
    left_90_degrees_target_piece = current_board[left_90_degrees_target_position][2] if left_90_degrees_is_valid else 'invalid_piece'
    top_45_degrees_left_target_piece = current_board[top_45_degrees_left_target_position][2] if top_45_degrees_left_is_valid else 'invalid_piece'

    if(top_90_degrees_is_valid and len(top_90_degrees_target_piece)==0):
        king_threats.append(top_90_degrees_target_position)
    if(top_90_degrees_is_valid and len(top_90_degrees_target_piece)>=1 and top_90_degrees_target_piece[0]!=color):
        king_threats.append(top_90_degrees_target_position)

    if(top_45_degrees_right_is_valid and len(top_45_degrees_right_target_piece)==0):
        king_threats.append(top_45_degrees_right_target_position)
    if(top_45_degrees_right_is_valid and len(top_45_degrees_right_target_piece)>=1 and top_45_degrees_right_target_piece[0]!=color):
        king_threats.append(top_45_degrees_right_target_position)

    if(right_90_degrees_is_valid and len(right_90_degrees_target_piece)==0):
        king_threats.append(right_90_degrees_target_position)
    if(right_90_degrees_is_valid and len(right_90_degrees_target_piece)>=1 and right_90_degrees_target_piece[0]!=color):
        king_threats.append(right_90_degrees_target_position)

    if(bottom_45_degrees_right_is_valid and len(bottom_45_degrees_right_target_piece)==0):
        king_threats.append(bottom_45_degrees_right_target_position)
    if(bottom_45_degrees_right_is_valid and len(bottom_45_degrees_right_target_piece)>=1 and bottom_45_degrees_right_target_piece[0]!=color):
        king_threats.append(bottom_45_degrees_right_target_position)

    if(bottom_90_degrees_is_valid and len(bottom_90_degrees_target_piece)==0):
        king_threats.append(bottom_90_degrees_target_position)
    if(bottom_90_degrees_is_valid and len(bottom_90_degrees_target_piece)>=1 and bottom_90_degrees_target_piece[0]!=color):
        king_threats.append(bottom_90_degrees_target_position)

    if(bottom_45_degrees_left_is_valid and len(bottom_45_degrees_left_target_piece)==0):
        king_threats.append(bottom_45_degrees_left_target_position)
    if(bottom_45_degrees_left_is_valid and len(bottom_45_degrees_left_target_piece)>=1 and bottom_45_degrees_left_target_piece[0]!=color):
        king_threats.append(bottom_45_degrees_left_target_position)

    if(left_90_degrees_is_valid and len(left_90_degrees_target_piece)==0):
        king_threats.append(left_90_degrees_target_position)
    if(left_90_degrees_is_valid and len(left_90_degrees_target_piece)>=1 and left_90_degrees_target_piece[0]!=color):
        king_threats.append(left_90_degrees_target_position)

    if(top_45_degrees_left_is_valid and len(top_45_degrees_left_target_piece)==0):
        king_threats.append(top_45_degrees_left_target_position)
    if(top_45_degrees_left_is_valid and len(top_45_degrees_left_target_piece)>=1 and top_45_degrees_left_target_piece[0]!=color):
        king_threats.append(top_45_degrees_left_target_position)
    
    return king_threats

def is_pawn(piece):
  return any(char.isdigit() for char in piece)

def extract_piece_name_and_color(piece):
  if(is_pawn(piece)):
    return {"name": "p", "color": piece[0].lower()}
  elif(len(piece)==2):
    return {"name": piece[1].lower(), "color": piece[0].lower()}
  else:
    return {"name": piece[2].lower(), "color": piece[0].lower()}

def unique(list_with_duplications):
    return list(set(list_with_duplications))

def all_threatened_and_defended_squares(current_board):
  """
  This function returns a dictionary of all the threatened squares separated by color given the current state of the board.
  Note that the list referenced by index W refers to all black squares threatened by white pieces
  and the list referenced by index B refers to all white squares threatened by black pieces
  """
  piece_mapping = {
    "p": pawn_move_validity,
    "n": knight_move_validity,
    "r": rook_move_validity,
    "b": bishop_move_validity,
    "q": queen_move_validity,
    "k": king_move_validity,
  }

  all_threats = {"w": [], "b": []}

  for(piece_position, value) in current_board.items():
    if(len(value[2]))>0:
      piece_details = extract_piece_name_and_color(value[2])
      piece_threats = piece_mapping[piece_details["name"]](piece_position, current_board, True)
      all_threats[piece_details["color"]] += piece_threats
  all_threats['w'] = unique(all_threats['w'])
  all_threats['b'] = unique(all_threats['b'])
  return all_threats




### Tests

sampleBoard = {"a1":[0,0,""],"b1":[1,0,"WQN"],"c1":[2,0,""],"d1":[3,0,""],"e1":[4,0,""], "f1":[5,0,"WKB"], "g1":[6,0,""], "h1":[7,0,"WKR"], 
         
"a2":[0,1,""],"b2":[1,1,"Wp2"],"c2":[2,1,"Wp3"],"d2":[3,1,"Wp4"],"e2":[4,1,"Wp5"], "f2":[5,1,"Wp6"], "g2":[6,1,"Wp7"], "h2":[7,1,"Wp8"],
         
"a3":[0,2,"Wp1"],"b3":[1,2,""],"c3":[2,2,""],"d3":[3,2,""],"e3":[4,2,""], "f3":[5,2,"WKN"], "g3":[6,2,""], "h3":[7,2,""],

"a4":[0,3,""],"b4":[1,3,""],"c4":[2,3,"WQR"],"d4":[3,3,""],"e4":[4,3,"WK"], "f4":[5,3,""], "g4":[6,3,"WQ"], "h4":[7,3,""],  

"a5":[0,4,""],"b5":[1,4,"BQ"],"c5":[2,4,""],"d5":[3,4,"BQB"],"e5":[4,4,""], "f5":[5,4,""], "g5":[6,4,"BKR"], "h5":[7,4,""],

"a6":[0,5,""],"b6":[1,5,""],"c6":[2,5,"BK"],"d6":[3,5,""],"e6":[4,5,"WQB"], "f6":[5,5,"BKN"], "g6":[6,5,""], "h6":[7,5,""],

"a7":[0,6,"Bp8"],"b7":[1,6,"Bp7"],"c7":[2,6,"Bp6"],"d7":[3,6,"Bp5"],"e7":[4,6,"Bp4"], "f7":[5,6,"Bp3"], "g7":[6,6,"Bp2"], "h7":[7,6,"Bp1"], 

"a8":[0,7,"BQR"],"b8":[1,7,"BQN"],"c8":[2,7,""],"d8":[3,7,""],"e8":[4,7,""], "f8":[5,7,"BKB"], "g8":[6,7,""], "h8":[7,7,""]
         
         }

# print(pawn_move_validity('e7', sampleBoard)) #[]
# print(pawn_move_validity('d7', sampleBoard)) #['e6', 'd6']
# print(pawn_move_validity('a7', sampleBoard)) #['a6', 'a5']
# print(pawn_move_validity('d2', sampleBoard)) #['d3', 'd4']
# print(pawn_move_validity('a3', sampleBoard)) #['a4']
# print(pawn_move_validity('c2', sampleBoard)) #['c3']
# print(knight_move_validity('f3', sampleBoard)) #['h4', 'g5', 'd4', 'e5', 'g1', 'e1']
# print(knight_move_validity('f6', sampleBoard)) #['e8', 'e4', 'h5', 'g4', 'g8']
print(rook_move_validity('c4', sampleBoard)) #['d4', 'b4', 'a4', 'c5', 'c6', 'c3']
print(rook_move_validity('g5', sampleBoard)) #['f5', 'e5', 'h5', 'g4', 'g6']
# print(bishop_move_validity('e6', sampleBoard)) #['f7', 'f5', 'd7', 'd5']
# print(bishop_move_validity('d5', sampleBoard)) #['c4', 'c6', 'e4']
# print(bishop_move_validity('e6', sampleBoard, True)) #['f7', 'f5', 'g4', 'd7', 'd5']
# print(bishop_move_validity('d5', sampleBoard, True)) #['c4', 'c6', 'e4', 'e6']
# print(queen_move_validity('g4', sampleBoard)) #['h5', 'h3', 'f5', 'h4', 'f4', 'g5', 'g3']
# print(queen_move_validity('b5', sampleBoard)) #['a4', 'a6', 'c4', 'a5', 'c5', 'b4', 'b3', 'b2', 'b6']
# print(queen_move_validity('g4', sampleBoard, True)) #['h5', 'h3', 'f5', 'e6', 'f3', 'h4', 'f4', 'e4', 'g5', 'g3', 'g2']
# print(queen_move_validity('b5', sampleBoard, True)) #['a4', 'a6', 'c4', 'c6', 'a5', 'c5', 'd5', 'b4', 'b3', 'b2', 'b6', 'b7']
# print(king_move_validity('e4', sampleBoard)) #['e5', 'f5', 'f4', 'e3', 'd3', 'd4', 'd5']
# print(king_move_validity('c6', sampleBoard)) #['c5', 'b6', 'd6']
# print(king_move_validity('e4', sampleBoard, True)) #['e5', 'f5', 'f4', 'e3', 'd3', 'd4', 'd5', 'f3']
# print(king_move_validity('c6', sampleBoard, True)) #['e5', 'f5', 'f4', 'e3', 'd3', 'd4', 'd5', 'f3']
# print(extract_piece_name_and_color("Bk"))

# all_threatened = all_threatened_and_defended_squares(sampleBoard)
# print(len(all_threatened['w']), len(all_threatened['b']))