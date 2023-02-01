import utils_threatened_squares_specific
import utils_valid_moves_specific

# def piece_is_attacked_by_a_pinner(surrounding_piece_square):
# for key, value in all_threatened_squares.items():
# if(key in ['rook', 'bishop', 'queen'] and surrounding_piece_square in value):
# return True
# return False

# pinned_squares = []
# for piece in surrounding_pieces:
# if piece_is_attacked_by_a_pinner(surrounding_piece_square):
# pinned_squares.append(piece)

# If you have a square in pinned_squares, return False early in validation logic
#squares = {"a1":(0,0),"b1":(1,0),"c1":(2,0),"d1":(3,0),"e1":(4,0),"f1":(5,0),"g1":(6,0),"h1":(7,0),"a2":(0,1),"b2":(1,1),"c2":(2,1),"d2":(3,1),"e2":(4,1),"f2":(5,1),"g2":(6,1),"h2":(7,1),"a3":(0,2),"b3":(1,2),"c3":(2,2),"d3":(3,2),"e3":(4,2),"f3":(5,2),"g3":(6,2),"h3":(7,2),"a4":(0,3),"b4":(1,3),"c4":(2,3),"d4":(3,3),"e4":(4,3),"f4":(5,3),"g4":(6,3),"h4":(7,3),"a5":(0,4),"b5":(1,4),"c5":(2,4),"d5":(3,4),"e5":(4,4),"f5":(5,4),"g5":(6,4),"h5":(7,4),"a6":(0,5),"b6":(1,5),"c6":(2,5),"d6":(3,5),"e6":(4,5),"f6":(5,5),"g6":(6,5),"h6":(7,5),"a7":(0,6),"b7":(1,6),"c7":(2,6),"d7":(3,6),"e7":(4,6),"f7":(5,6),"g7":(6,6),"h7":(7,6),"a8":(0,7),"b8":(1,7),"c8":(2,7),"d8":(3,7),"e8":(4,7),"f8":(5,7),"g8":(6,7),"h8":(7,7)}
def generate_surrounding_squares(king_square, current_board):
    (king_x_coord, king_y_coord) = utils_threatened_squares_specific.squares[king_square]
    valid_king_move_directions = [[-1, +0], [+1, +0], [+0, -1], [+0, +1], [-1, -1], [+1, +1], [-1, +1], [+1, -1]]
    surrounding_pieces = []
    king_color = current_board[king_square][2][0].lower()
    for direction in valid_king_move_directions:
        for n in range(1, 8):
            x_coord = utils_threatened_squares_specific.normalized_arithmetic(king_color, "sum", king_x_coord, n*direction[0])
            y_coord = utils_threatened_squares_specific.normalized_arithmetic(king_color, "sum", king_y_coord, n*direction[1])
            current_square_is_valid = utils_valid_moves_specific.isValidBoardCoordinates(x_coord, y_coord)
            if current_square_is_valid:
                current_square = utils_valid_moves_specific.inverted_squares_map[str(x_coord)+','+str(y_coord)]
                current_piece = current_board[current_square][2]
                if len(current_piece) == 0:
                    continue
                if len(current_piece) >= 1 and current_piece[0].lower() != king_color:
                    break
                if len(current_piece) >= 1 and current_piece[0].lower() == king_color:
                    surrounding_pieces.append(current_square)
                    break
    return surrounding_pieces
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

# "a5":[0,4,""],"b5":[1,4,"BQ"],"c5":[2,4,""],"d5":[3,4,"BQB"],"e5":[4,4,""], "f5":[5,4,""], "g5":[6,4,"BKR"], "h5":[7,4,""],

# "a6":[0,5,""],"b6":[1,5,""],"c6":[2,5,"BK"],"d6":[3,5,""],"e6":[4,5,"WQB"], "f6":[5,5,"BKN"], "g6":[6,5,""], "h6":[7,5,""],

# "a7":[0,6,"Bp8"],"b7":[1,6,"Bp7"],"c7":[2,6,"Bp6"],"d7":[3,6,"Bp5"],"e7":[4,6,"Bp4"], "f7":[5,6,"Bp3"], "g7":[6,6,"Bp2"], "h7":[7,6,"Bp1"], 

# "a8":[0,7,"BQR"],"b8":[1,7,"BQN"],"c8":[2,7,""],"d8":[3,7,""],"e8":[4,7,""], "f8":[5,7,"BKB"], "g8":[6,7,""], "h8":[7,7,""]
         
#          }


# print(generate_surrounding_squares('e1', sampleInertiaBoard)) #['d1', 'f1', 'e2', 'f2', 'd2']
# print(generate_surrounding_squares('e8', sampleInertiaBoard)) #['f8', 'd8', 'e7', 'd7', 'f7']
# print(generate_surrounding_squares('e4', sampleChaosBoard)) #['c4', 'g4', 'e2', 'e6', 'c2', 'f3']
# print(generate_surrounding_squares('c6', sampleChaosBoard)) #['c7', 'd7', 'b5', 'd5', 'b7']