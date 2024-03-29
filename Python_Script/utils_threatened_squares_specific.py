"""
TO-DO:
1/ Rewrite Pawn, King, and Knight logic with a for or while loop. Too verbose.
2/ Track all moves and store board position before and after
"""
import util_constants

squares = util_constants.squares
inverted_squares_map = util_constants.inverted_squares_map

def isValidBoardCoordinates(x_coord, y_coord):
    VALID_X_COORD = x_coord>=0 and x_coord<=7
    VALID_Y_COORD = y_coord>=0 and y_coord<=7
    return VALID_X_COORD and VALID_Y_COORD

def normalized_arithmetic(color, operation, value1, value2):
  """
  Since we're rotating the board 180 degrees for black,
  the addition and subtraction movement operations have to be flipped
  """
  if(str(color).lower() == "b"):
    if(operation == "sum"):
      return value1 - value2
    elif(operation == "diff"):
      return value1 + value2
  else:
    if(operation == "sum"):
      return value1 + value2
    elif(operation == "diff"):
      return value1 - value2

def pawn_threatened_squares(current_position, current_board):
    pawn_threats = []
    x_coord = squares[current_position][0]
    y_coord = squares[current_position][1]
    color = current_board[current_position][2][0]
    top_right_x_coord = normalized_arithmetic(color, "sum", x_coord, 1)
    top_right_y_coord = normalized_arithmetic(color, "sum", y_coord, 1)
    top_left_x_coord = normalized_arithmetic(color, "diff", x_coord, 1)
    top_left_y_coord = normalized_arithmetic(color, "sum", y_coord, 1)
    top_right_square_is_valid = isValidBoardCoordinates(top_right_x_coord, top_right_y_coord)
    top_left_square_is_valid = isValidBoardCoordinates(top_left_x_coord, top_left_y_coord)
     #using ternary operator to prevent key error when the coordinates are invalid
    right_target_position = inverted_squares_map[str(top_right_x_coord)+','+str(top_right_y_coord)] if top_right_square_is_valid else 'invalid_square'
    left_target_position = inverted_squares_map[str(top_left_x_coord)+','+str(top_left_y_coord)] if top_left_square_is_valid else 'invalid_square'

    #Check if the top right square is valid, empty or of a different color
    if(top_right_square_is_valid):
        pawn_threats.append(right_target_position)
    #Check if the top left square is valid, empty or of a different color
    if(top_left_square_is_valid):
        pawn_threats.append(left_target_position)

    return pawn_threats

def knight_threatened_squares(current_position, current_board):
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

    if(top_near_right_square_is_valid):
        knight_threats.append(top_near_right_target_position)

    if(top_far_right_square_is_valid):
        knight_threats.append(top_far_right_target_position)

    if(top_near_left_square_is_valid):
        knight_threats.append(top_near_left_target_position)

    if(top_far_left_square_is_valid):
        knight_threats.append(top_far_left_target_position)

    if(bottom_near_right_square_is_valid):
        knight_threats.append(bottom_near_right_target_position)

    if(bottom_far_right_square_is_valid):
        knight_threats.append(bottom_far_right_target_position)

    if(bottom_near_left_square_is_valid):
        knight_threats.append(bottom_near_left_target_position)

    if(bottom_far_left_square_is_valid):
        knight_threats.append(bottom_far_left_target_position)
    
    return knight_threats

def rook_threatened_squares(current_position, current_board):
    """
    A rook can potentially attack in 4 vertical directions (+x, -x, +y, -y).
    We'll check each of these directions for validity and occupation
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
        if(this_square_is_valid and len(target_piece) >= 1):
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
        if(this_square_is_valid and len(target_piece) >= 1):
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
        if(this_square_is_valid and len(target_piece) >= 1):
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
        if(this_square_is_valid and len(target_piece) >= 1):
            rook_threats.append(target_position)
            break
    return rook_threats

def bishop_threatened_squares(current_position, current_board):
    """
    A Bishop can potentially attack in 4 diagonal directions (z_up_right(1:15 on a clock), z_down_right(4:15 on a clock), 
    z_up_left(10:15 on a clock), z_down_left(7:15 on a clock)).
    We'll check each of these directions for validity and occupation
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
        if(this_square_is_valid and len(target_piece) >= 1):
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
        if(this_square_is_valid and len(target_piece) >= 1):
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
        if(this_square_is_valid and len(target_piece) >= 1):
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
        if(this_square_is_valid and len(target_piece) >= 1):
            bishop_threats.append(target_position)
            break
    return bishop_threats

def queen_threatened_squares(current_position, current_board):

    """
    A Queen combines the moves of both the Bishop and Rook.
    We'll simply call the existing functions and combine their results
    """
    bishop_threats = bishop_threatened_squares(current_position, current_board)
    rook_threats = rook_threatened_squares(current_position, current_board)
    return bishop_threats + rook_threats

def king_threatened_squares(current_position, current_board):
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

def extract_piece_name_and_color(piece):
  return {"name": piece[1].lower(), "color": piece[0].lower()}

def deduplicate(list_with_duplications):
    return list(set(list_with_duplications))

def all_threatened_and_defended_squares(current_board, king_color):
  """
  This function returns a dictionary of all the threatened squares separated by color given the current state of the board.
  *args: current_board is the current board dictioary
         king_color should be either the string 'w' or 'b' to indicate the color of the king for which threatened squares
         are being checked
  """
  piece_mapping = {
    "p": pawn_threatened_squares,
    "n": knight_threatened_squares,
    "r": rook_threatened_squares,
    "b": bishop_threatened_squares,
    "q": queen_threatened_squares,
    "k": king_threatened_squares,
  }

  all_threats = {}

  for(piece_position, value) in current_board.items():
      if(len(value[2])>0):
          piece_details = extract_piece_name_and_color(value[2])
          if(piece_details["color"]!=king_color.lower()):
              piece_threats = piece_mapping[piece_details["name"]](piece_position, current_board)
              all_threats[piece_position] = piece_threats
  return all_threats

def flatten_a_dictionary_of_arrays(dict):
  all_threats = []
  for(key, value) in dict.items():
    all_threats += value
  return deduplicate(all_threats)


def flip_colors(current_color):
    return "b" if current_color.lower() == "w" else "w"

def find_attackers(square_to_check, threatened_squares_and_attackers):
    ###
    # This function returns a list of squares of pieces threatening a particular square
    # ###
    attacking_squares = []
    for attacker, attacked_squares in threatened_squares_and_attackers.items():
        if(square_to_check in attacked_squares):
            attacking_squares.append(attacker)
    return attacking_squares


### Tests

# sampleBoard = {"a1":[0,0,""],"b1":[1,0,"WQN"],"c1":[2,0,""],"d1":[3,0,""],"e1":[4,0,""], "f1":[5,0,"WKB"], "g1":[6,0,""], "h1":[7,0,"WKR"], 
         
# "a2":[0,1,""],"b2":[1,1,"Wp2"],"c2":[2,1,"Wp3"],"d2":[3,1,"Wp4"],"e2":[4,1,"Wp5"], "f2":[5,1,"Wp6"], "g2":[6,1,"Wp7"], "h2":[7,1,"Wp8"],
         
# "a3":[0,2,"Wp1"],"b3":[1,2,""],"c3":[2,2,""],"d3":[3,2,""],"e3":[4,2,""], "f3":[5,2,"WKN"], "g3":[6,2,""], "h3":[7,2,""],

# "a4":[0,3,""],"b4":[1,3,""],"c4":[2,3,"WQR"],"d4":[3,3,""],"e4":[4,3,"WK"], "f4":[5,3,""], "g4":[6,3,"WQ"], "h4":[7,3,""],  

# "a5":[0,4,""],"b5":[1,4,"BQ"],"c5":[2,4,""],"d5":[3,4,"BQB"],"e5":[4,4,""], "f5":[5,4,""], "g5":[6,4,"BKR"], "h5":[7,4,""],

# "a6":[0,5,""],"b6":[1,5,""],"c6":[2,5,"BK"],"d6":[3,5,""],"e6":[4,5,"WQB"], "f6":[5,5,"BKN"], "g6":[6,5,""], "h6":[7,5,""],

# "a7":[0,6,"Bp8"],"b7":[1,6,"Bp7"],"c7":[2,6,"Bp6"],"d7":[3,6,"Bp5"],"e7":[4,6,"Bp4"], "f7":[5,6,"Bp3"], "g7":[6,6,"Bp2"], "h7":[7,6,"Bp1"], 

# "a8":[0,7,"BQR"],"b8":[1,7,"BQN"],"c8":[2,7,""],"d8":[3,7,""],"e8":[4,7,""], "f8":[5,7,"BKB"], "g8":[6,7,""], "h8":[7,7,""]
         
#          }

# print(pawn_threatened_squares('e7', sampleBoard)) #['d6', 'f6']
# print(pawn_threatened_squares('d7', sampleBoard)) #['e6', 'c6']
# print(pawn_threatened_squares('d2', sampleBoard)) #['e3', 'c3']
# print(pawn_threatened_squares('a3', sampleBoard)) #['b4']
# print(pawn_threatened_squares('c2', sampleBoard)) #['d3', 'b3']
# print(knight_threatened_squares('f3', sampleBoard)) #['h4', 'g5', 'd4', 'e5', 'h2', 'g1', 'd2', 'e1']
# print(knight_threatened_squares('f6', sampleBoard)) #['d5', 'e4', 'h5', 'g4', 'd7', 'e8', 'h7', 'g8']
# print(rook_threatened_squares('c4', sampleBoard)) #['d4', 'e4', 'b4', 'a4', 'c5', 'c6', 'c3', 'c2']
# print(rook_threatened_squares('g5', sampleBoard)) #['f5', 'e5', 'd5', 'h5', 'g4', 'g6', 'g7']
# print(bishop_threatened_squares('e6', sampleBoard)) #['f7', 'f5', 'g4', 'd7', 'd5']
# print(bishop_threatened_squares('d5', sampleBoard)) #['c4', 'c6', 'e4', 'e6']
# print(queen_threatened_squares('g4', sampleBoard)) #['h5', 'h3', 'f5', 'e6', 'f3', 'h4', 'f4', 'e4', 'g5', 'g3', 'g2']
# print(queen_threatened_squares('b5', sampleBoard)) #['a4', 'a6', 'c4', 'c6', 'a5', 'c5', 'd5', 'b4', 'b3', 'b2', 'b6', 'b7']
# print(king_threatened_squares('e4', sampleBoard)) #['e5', 'f5', 'f4', 'e3', 'd3', 'd4', 'd5']
# print(king_threatened_squares('c6', sampleBoard)) #['c5', 'b5', 'b6', 'b7', 'c7', 'd7', 'd6', 'd5']
# print(extract_piece_name_and_color("Bk"))

# print(all_threatened_and_defended_squares(sampleBoard, 'w')) #{'b5': ['a4', 'a6', 'c4', 'c6', 'a5', 'c5', 'd5', 'b4', 'b3', 'b2', 'b6', 'b7'], 'd5': ['c4', 'c6', 'e4', 'e6'], 'g5': ['f5', 'e5', 'd5', 'h5', 'g4', 'g6', 'g7'], 'c6': ['c5', 'b5', 'b6', 'b7', 'c7', 'd7', 'd6', 'd5'], 'f6': ['d5', 'e4', 'h5', 'g4', 'd7', 'e8', 'h7', 'g8'], 'a7': ['b6'], 'b7': ['a6', 'c6'], 'c7': ['b6', 'd6'], 'd7': ['c6', 'e6'], 'e7': ['d6', 'f6'], 'f7': ['e6', 'g6'], 'g7': ['f6', 'h6'], 'h7': ['g6'], 'a8': ['b8', 'a7'], 'b8': ['a6', 'd7', 'c6'], 'f8': ['e7', 'g7']}
# print(flatten_a_dictionary_of_arrays(all_threatened_and_defended_squares(sampleBoard, 'w'))) #['b4', 'b2', 'b7', 'h5', 'a4', 'd6', 'f6', 'b5', 'b6', 'c4', 'g4', 'e7', 'c6', 'g8', 'b3', 'h7', 'e5', 'a7', 'g7', 'h6', 'a5', 'e4', 'c5', 'b8', 'e6', 'f5', 'd7', 'd5', 'g6', 'e8', 'c7', 'a6']