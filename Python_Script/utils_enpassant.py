import util_constants
import utils_threatened_squares_specific
def is_valid_enpassant_move(current_square, destination_square, current_board, current_color, last_game_move):
  y_coord = util_constants.squares[current_square][1]
  if(y_coord != util_constants.enpassant_attacking_column_map[current_color.lower()]):
    return False
  (destination_x_coord, destination_y_coord) = util_constants.squares[destination_square]
  target_y_coord = utils_threatened_squares_specific.normalized_arithmetic(current_color, "diff", destination_y_coord, 1)
  target_square = util_constants.inverted_squares_map[str(destination_x_coord)+','+str(target_y_coord)]
  target_piece = current_board[target_square][2]
  if(not bool(target_piece)):
    return False
  target_piece_info = utils_threatened_squares_specific.extract_piece_name_and_color(target_piece)
  if(target_piece_info["name"] != "p" or target_piece_info["color"] == current_color):
    return False
  if(last_game_move["destination_square"] != target_square or target_piece != last_game_move["piece"]):
    return False
  target_piece_move_difference = util_constants.squares[last_game_move["destination_square"]][1] - util_constants.squares[last_game_move["current_square"]][1]
  opponent_color = utils_threatened_squares_specific.flip_colors(current_color)
  if(target_piece_move_difference != util_constants.enpassant_forward_pawn_move_diff_map[opponent_color]):
    return False
  return True

# sampleBoard = {"a1":[0,0,""],"b1":[1,0,"WQN"],"c1":[2,0,""],"d1":[3,0,""],"e1":[4,0,""], "f1":[5,0,"WKB"], "g1":[6,0,""], "h1":[7,0,"WKR"], 
         
# "a2":[0,1,""],"b2":[1,1,""],"c2":[2,1,""],"d2":[3,1,"Wp4"],"e2":[4,1,"Wp5"], "f2":[5,1,"Wp6"], "g2":[6,1,"Wp7"], "h2":[7,1,"Wp8"],
         
# "a3":[0,2,""],"b3":[1,2,""],"c3":[2,2,""],"d3":[3,2,""],"e3":[4,2,""], "f3":[5,2,"WKN"], "g3":[6,2,""], "h3":[7,2,""],

# "a4":[0,3,"Wp1"],"b4":[1,3,"Bp2"],"c4":[2,3,"Wp3"],"d4":[3,3,""],"e4":[4,3,"WK"], "f4":[5,3,""], "g4":[6,3,"WQ"], "h4":[7,3,""],  

# "a5":[0,4,""],"b5":[1,4,"BQ"],"c5":[2,4,""],"d5":[3,4,"BQB"],"e5":[4,4,""], "f5":[5,4,""], "g5":[6,4,"BKR"], "h5":[7,4,""],

# "a6":[0,5,""],"b6":[1,5,""],"c6":[2,5,"BK"],"d6":[3,5,""],"e6":[4,5,"WQB"], "f6":[5,5,"BKN"], "g6":[6,5,""], "h6":[7,5,""],

# "a7":[0,6,"Bp8"],"b7":[1,6,"Bp7"],"c7":[2,6,"Bp6"],"d7":[3,6,"Bp5"],"e7":[4,6,"Bp4"], "f7":[5,6,"Bp3"], "g7":[6,6,"Bp2"], "h7":[7,6,"Bp1"], 

# "a8":[0,7,"BQR"],"b8":[1,7,"BQN"],"c8":[2,7,""],"d8":[3,7,""],"e8":[4,7,""], "f8":[5,7,"BKB"], "g8":[6,7,""], "h8":[7,7,""]
         
#          }
# print(is_valid_enpassant_move('b4', 'c3', sampleBoard, 'b', {"piece": "Wp3","destination_square": 'c4', "current_square": 'c3'}))