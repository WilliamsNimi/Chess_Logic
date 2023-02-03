import utils_threatened_squares_specific
import utils_valid_moves_specific

def generate_pinned_squares(king_square, current_board, king_color):
    """
    - This function returns a dictionary of pinned squares and the squares to which they are constrained to move
    """
    (king_x_coord, king_y_coord) = utils_threatened_squares_specific.squares[king_square]
    valid_king_move_directions = [[-1, +0], [+1, +0], [+0, -1], [+0, +1], [-1, -1], [+1, +1], [-1, +1], [+1, -1]]
    pinned_squares_map = {}
    for direction in valid_king_move_directions:
        king_defender_encountered = False
        pinned_square = ""
        squares_along_the_line = []
        for n in range(1, 8):
            x_coord = utils_threatened_squares_specific.normalized_arithmetic(king_color, "sum", king_x_coord, n*direction[0])
            y_coord = utils_threatened_squares_specific.normalized_arithmetic(king_color, "sum", king_y_coord, n*direction[1])
            if utils_valid_moves_specific.isValidBoardCoordinates(x_coord, y_coord):
                current_square = utils_valid_moves_specific.inverted_squares_map[str(x_coord)+','+str(y_coord)]
                squares_along_the_line.append(current_square)
                current_piece = current_board[current_square][2]
                if len(current_piece) >= 1 and current_piece[0].lower() != king_color and not king_defender_encountered:
                    break
                if len(current_piece) >= 1 and current_piece[0].lower() == king_color and king_defender_encountered:
                    break
                if len(current_piece) >= 1 and current_piece[0].lower() != king_color and king_defender_encountered: #encountering a different color piece after encountering a same color piece, check if it is a "pinner" then break
                    current_piece_name_color_dict = utils_threatened_squares_specific.extract_piece_name_and_color(current_piece)
                    if(current_piece_name_color_dict["name"] in ["r", "b", "q"]):
                        pinned_squares_map[pinned_square] = squares_along_the_line
                    break
                if len(current_piece) == 0:
                    continue
                if len(current_piece) >= 1 and current_piece[0].lower() == king_color and not king_defender_encountered: #encountering a same color piece for first time. Note it and continue
                    king_defender_encountered = True
                    pinned_square = current_square
                    squares_along_the_line.pop(-1)
                    continue

    return pinned_squares_map

### Tests

# sampleInertiaBoard = {"a1":[0,0,"WQR"],"b1":[1,0,"WQN"],"c1":[2,0,"WQB"],"d1":[3,0,"WQ"],"e1":[4,0,"WK"], "f1":[5,0,"WKB"], "g1":[6,0,"WKN"], "h1":[7,0,"WKR"], 
         
# "a2":[0,1,"Wp1"],"b2":[1,1,"Wp2"],"c2":[2,1,"Wp3"],"d2":[3,1,"Wp4"],"e2":[4,1,"Wp5"], "f2":[5,1,"Wp6"], "g2":[6,1,"Wp7"], "h2":[7,1,"Wp8"],
         
# "a3":[0,2,""],"b3":[1,2,""],"c3":[2,2,""],"d3":[3,2,""],"e3":[4,2,""], "f3":[5,2,""], "g3":[6,2,""], "h3":[7,2,""],

# "a4":[0,3,""],"b4":[1,3,""],"c4":[2,3,""],"d4":[3,3,""],"e4":[4,3,""], "f4":[5,3,""], "g4":[6,3,""], "h4":[7,3,""],  

# "a5":[0,4,""],"b5":[1,4,""],"c5":[2,4,""],"d5":[3,4,""],"e5":[4,4,""], "f5":[5,4,""], "g5":[6,4,""], "h5":[7,4,""],

# "a6":[0,5,""],"b6":[1,5,""],"c6":[2,5,""],"d6":[3,5,""],"e6":[4,5,""], "f6":[5,5,""], "g6":[6,5,""], "h6":[7,5,""],

# "a7":[0,6,"Bp8"],"b7":[1,6,"Bp7"],"c7":[2,6,"Bp6"],"d7":[3,6,"Bp5"],"e7":[4,6,"Bp4"], "f7":[5,6,"Bp3"], "g7":[6,6,"Bp2"], "h7":[7,6,"Bp1"], 

# "a8":[0,7,"BQR"],"b8":[1,7,"BQN"],"c8":[2,7,"BQB"],"d8":[3,7,"BQ"],"e8":[4,7,"BK"], "f8":[5,7,"BKB"], "g8":[6,7,"BKN"], "h8":[7,7,"BKR"]
         
#          }

# sampleChaosBoard = {"a1":[0,0,""],"b1":[1,0,"WQN"],"c1":[2,0,""],"d1":[3,0,""],"e1":[4,0,""], "f1":[5,0,"WKB"], "g1":[6,0,""], "h1":[7,0,"WKR"], 
         
# "a2":[0,1,""],"b2":[1,1,"Wp2"],"c2":[2,1,"Wp3"],"d2":[3,1,"Wp4"],"e2":[4,1,"Wp5"], "f2":[5,1,"Wp6"], "g2":[6,1,"Wp7"], "h2":[7,1,"Wp8"],
         
# "a3":[0,2,"Wp1"],"b3":[1,2,""],"c3":[2,2,""],"d3":[3,2,""],"e3":[4,2,""], "f3":[5,2,"WKN"], "g3":[6,2,""], "h3":[7,2,""],

# "a4":[0,3,""],"b4":[1,3,""],"c4":[2,3,"WQR"],"d4":[3,3,""],"e4":[4,3,"WK"], "f4":[5,3,""], "g4":[6,3,"WQ"], "h4":[7,3,""],  

# "a5":[0,4,""],"b5":[1,4,""],"c5":[2,4,"BQ"],"d5":[3,4,"BQB"],"e5":[4,4,""], "f5":[5,4,""], "g5":[6,4,"BKR"], "h5":[7,4,""],

# "a6":[0,5,""],"b6":[1,5,""],"c6":[2,5,"BK"],"d6":[3,5,""],"e6":[4,5,"WQB"], "f6":[5,5,"BKN"], "g6":[6,5,""], "h6":[7,5,""],

# "a7":[0,6,"Bp8"],"b7":[1,6,"Bp7"],"c7":[2,6,"Bp6"],"d7":[3,6,"Bp5"],"e7":[4,6,"Bp4"], "f7":[5,6,"Bp3"], "g7":[6,6,"Bp2"], "h7":[7,6,"Bp1"], 

# "a8":[0,7,"BQR"],"b8":[1,7,"BQN"],"c8":[2,7,""],"d8":[3,7,""],"e8":[4,7,""], "f8":[5,7,"BKB"], "g8":[6,7,""], "h8":[7,7,""]
         
#          }

# print(generate_pinned_squares('c6', sampleChaosBoard, 'b')) #['c5']