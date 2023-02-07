# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 06:21:01 2022

@author: Nimi Williams
"""
import numpy as np
import pandas as pd
import utils_valid_moves_specific
import utils_pinned_pieces
import utils_threatened_squares_specific
import utils_king_check
import util_constants
import utils_piece_promotion


"""Board Initialization


WQR = White's Queen Side Rook
WQN = White's Queen Side Knight
WQB = White's Queen Side Bishop
WQ = White's Queen
WK = White's King
WKB = White's King side Bishop
WKN = White's King side Knight
WKR = White's king side Rook
Wp = White's pawn

BQR = Black's Queen Side Rook
BQN = Blacke's Queen Side Knight
BQB = Black's Queen Side Bishop
BQ = Black's Queen
BK = Black's King
BKB = Black's King side Bishop
BKN = Black's King side Knight
BKR = Black's king side Rook
Bp = Black's pawn

Normal chess notation for squares is used as key in the dictionary. The Values attached to each key is mapped to a cartesian coordinate, with square a1 starting at (0,0)

"""
### Initializing game state values
Board = {"a1":[0,0,"WR2"],"b1":[1,0,"WN2"],"c1":[2,0,"WB2"],"d1":[3,0,"WQ1"],"e1":[4,0,"WK"], "f1":[5,0,"WB1"], "g1":[6,0,"WN1"], "h1":[7,0,"WR1"], 
         
"a2":[0,1,"Wp1"],"b2":[1,1,"Wp2"],"c2":[2,1,"Wp3"],"d2":[3,1,"Wp4"],"e2":[4,1,"Wp5"], "f2":[5,1,"Wp6"], "g2":[6,1,"Wp7"], "h2":[7,1,"Wp8"],
         
"a3":[0,2,""],"b3":[1,2,""],"c3":[2,2,""],"d3":[3,2,""],"e3":[4,2,""], "f3":[5,2,""], "g3":[6,2,""], "h3":[7,2,""],

"a4":[0,3,""],"b4":[1,3,""],"c4":[2,3,""],"d4":[3,3,""],"e4":[4,3,""], "f4":[5,3,""], "g4":[6,3,""], "h4":[7,3,""],  

"a5":[0,4,""],"b5":[1,4,""],"c5":[2,4,""],"d5":[3,4,""],"e5":[4,4,""], "f5":[5,4,""], "g5":[6,4,""], "h5":[7,4,""],

"a6":[0,5,""],"b6":[1,5,""],"c6":[2,5,""],"d6":[3,5,""],"e6":[4,5,""], "f6":[5,5,""], "g6":[6,5,""], "h6":[7,5,""],

"a7":[0,6,"Bp8"],"b7":[1,6,"Bp7"],"c7":[2,6,"Bp6"],"d7":[3,6,"Bp5"],"e7":[4,6,"Bp4"], "f7":[5,6,"Bp3"], "g7":[6,6,"Bp2"], "h7":[7,6,"Bp1"], 

"a8":[0,7,"BR2"],"b8":[1,7,"BN2"],"c8":[2,7,"BB2"],"d8":[3,7,"BQ1"],"e8":[4,7,"BK"], "f8":[5,7,"BB1"], "g8":[6,7,"BN1"], "h8":[7,7,"BR1"]
         
         }

king_square_dict = {"w": "e1", "b": "e8"} #Explicitly specifying the kings' squares so we don't have to do a board look up on every move. Will update this state dictionary any time the king makes a move to a different square.
game_moves = []
moved_pieces = []
current_turn_color = "w"
king_is_in_check = {"w": {"status": False, "valid_moves_map": {}}, "b": {"status": False, "valid_moves_map": {}}}
promotion_numbering_map = {"wq": 1, "bq": 1, "wr": 2, "br": 2, "wb": 2, "bb": 2, "wn": 2, "bn": 2}

### Importing constant values
squares = util_constants.squares
inverted_squares_map = util_constants.inverted_squares_map
castling_rooks_map = util_constants.castling_rooks_map
colors_name_map = util_constants.colors_name_map
board_letters = util_constants.board_letters

def is_castling_move(move):
    x_diff = squares[move[1]][0] - squares[move[2]][0]
    if(len(move[0])!=2 or x_diff not in [2, -2]):
        return []
    if(move[0][1].lower()!='k'):
        return []
    castling_direction = '+ve' if x_diff == 2 else '-ve'
    return castling_rooks_map[move[0][0].lower() + castling_direction]
    

def render_board(Board):
    
    """
    This function is supposed to render the board when called. 
    
    TO:DO find an optimal way to render this board"""
    board_list = []
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    row6 = []
    row7 = []
    row8 = []
    count = 0
    for key, values in Board.items():
        board_list.append(values[2])
    for elements in board_list:
        if(count < 8):
            row1.append(elements)
            count+=1
        elif(count>=8 and count <16):
            row2.append(elements)
            count+=1
        elif(count>=16 and count <24):
            row3.append(elements)
            count+=1
        elif(count>=24 and count<32):
            row4.append(elements)
            count+=1
        elif(count>=32 and count < 40):
            row5.append(elements)
            count+=1
        elif(count>=40 and count< 48):
            row6.append(elements)
            count+=1
        elif(count>=48 and count < 56):
            row7.append(elements)
            count+=1
        else:
            row8.append(elements)
            count+=1
    
    board_array = np.array([row8, row7, row6, row5, row4, row3, row2, row1], dtype=object)
    
    df = pd.DataFrame(board_array, columns = board_letters)
    df.index = [8,7,6,5,4,3,2,1]
    print(df)

def get_squares_threatened_by_black(all_threatened_squares):
    ###
    # get_squares_threatened_by_black- This function aims to get the squares threatened by all black pieces
    # Description: This function gets all the squares threatened by every black piece on the board by looping through the full list of threatened squares
    # @all_threatened_squares: This is the full list of all threatened squares
    # Return: Returns a list of all squares threatened by black
    ###
    black_threats = []
    for key, values in all_threatened_squares.items():
        if (key[0] == "B"):
            for squares in values:
                black_threats.append(squares)

    return black_threats

def get_squares_threatened_by_white(all_threatened_squares):
    ###
    # get_squares_threatened_by_white- This function aims to get the squares threatened by all white pieces
    # Description: This function gets all the squares threatened by every white piece on the board by looping through the full list of threatened squares
    # @all_threatened_squares: This is the full list of all threatened squares
    # Return: Returns a list of all squares threatened by white
    ###
    white_threats = []
    for key, values in all_threatened_squares.items():
        if (key[0] == "W"):
            for squares in values:
                white_threats.append(squares)

    return white_threats

def make_move(validCheck, move):
    
    """This functions changes the board values in the dictionary and returns an illegal move message if the move is invalid"""
    global move_successful
    global current_turn_color # If you're reassigning a global variable within a function (as we're doing for this variable at the end of this function), the local version of the variable shadows the global and you get an unbound exception. Gotta declare it as global to enforce the global value of the variable
    opponent_color = utils_threatened_squares_specific.flip_colors(current_turn_color)
    if validCheck == True:
        castling_rook_and_squares = is_castling_move(move) 
        moved_pieces.append(move[0])
        # Creating a snapshot of the game on every move by recording the move, origin, destination, and before and after boards
        # We probably don't need this yet but it'll come handy if we need to display move history and stuff like that
        move_record = {"piece": move[0], "current_square": move[2],"target_square": move[1], "board_before": Board}
        Board[move[1]][2] = move[0]
        Board[move[2]][2] = ""
        if(castling_rook_and_squares):
            moved_pieces.append(castling_rook_and_squares[0])
            Board[castling_rook_and_squares[2]][2] = castling_rook_and_squares[0]
            Board[castling_rook_and_squares[1]][2] = ""
            move_record["castling_rook"] = castling_rook_and_squares[0]
        move_record["board_after"] = Board
        game_moves.append(move_record)
        if(move[0] in ["BK", "WK"]):
            king_square_dict[move[0][0].lower()] = move[1]
        threatened_squares_and_attackers = utils_threatened_squares_specific.all_threatened_and_defended_squares(Board, opponent_color)
        pieces_checking_opponent_king = utils_threatened_squares_specific.find_attackers(king_square_dict[opponent_color], threatened_squares_and_attackers)
        if(len(pieces_checking_opponent_king) > 0):
            pinned_squares_map = utils_pinned_pieces.generate_pinned_squares(king_square_dict[opponent_color], Board, opponent_color)
            king_is_in_check[opponent_color]["status"] = True
            valid_moves_in_check = utils_king_check.valid_moves_when_in_check(king_square_dict[opponent_color], opponent_color, Board, pinned_squares_map, pieces_checking_opponent_king)
            if(not bool(valid_moves_in_check)):
                render_board(Board)
                print("Checkmate!"+ " " + colors_name_map[current_turn_color].capitalize() + " wins!")
                global exit
                exit = 1
            else:
                print(colors_name_map[opponent_color].capitalize() + " King is in check!!")
                king_is_in_check[opponent_color]["valid_moves_map"] = valid_moves_in_check
        else:
            king_is_in_check[opponent_color]["status"] = False
        if(utils_piece_promotion.is_promotion_move(move[0], move[1])):
            desired_official = input("Please enter the first alphabet of the official you would like your pawn promoted to: ")
            if(str(desired_official).lower() not in util_constants.valid_promotion_officials):
                move_successful = False
                return "Invalid official. Please enter one of the Alphabets: Q, R, B, N"
            promotion_numbering_map_key = current_turn_color.lower() + desired_official.lower()
            current_desired_official_number = promotion_numbering_map[promotion_numbering_map_key]
            promoted_official = utils_piece_promotion.get_promoted_official(desired_official, current_desired_official_number, current_turn_color)
            Board[move[1]][2] = promoted_official
            promotion_numbering_map[promotion_numbering_map_key] += 1
        current_turn_color = utils_threatened_squares_specific.flip_colors(current_turn_color)
        move_successful = True

    else:
        move_successful = False
        return "Illegal Move"

def get_position_of_piece(move):
    """ This function gets the position of the piece the user has indicated to move. If the piece does not exist on the board, it returns an empty string"""
    for key, values in Board.items():
        if move[0] in values:
            return key

def play(piece_to_move, new_position):
    
    pieces_moved = {} #Change to move history and track both black and white's move
    
    move = []
    move.append(piece_to_move)
    move.append(new_position)
    current_pos = get_position_of_piece(move)
    move.append(current_pos)
    king_square = king_square_dict[current_turn_color]
    pinned_squares_map = utils_pinned_pieces.generate_pinned_squares(king_square, Board, current_turn_color)
    name_of_piece_to_move = utils_threatened_squares_specific.extract_piece_name_and_color(piece_to_move)["name"]
    move_validity = False
    if(king_is_in_check[current_turn_color]["status"] == True):
        valid_moves_in_check = king_is_in_check[current_turn_color]["valid_moves_map"]
        move_validity = move[2] in list(valid_moves_in_check.keys()) and move[1] in valid_moves_in_check[move[2]]
    elif(name_of_piece_to_move == "k"):
        move_validity = utils_valid_moves_specific.validity_function_map[name_of_piece_to_move](move, Board, moved_pieces)
    else:
        move_validity = utils_valid_moves_specific.validity_function_map[name_of_piece_to_move](move, Board, pinned_squares_map)
    print(make_move(move_validity, move))
        
exit  = 0  
BlackTurn = False
WhiteTurn = True  


while(exit != 1): 
    render_board(Board)
    if(WhiteTurn == True):
        print("\nWhite's Turn!")
    else:
        print("\nBlack's Turn")
    piece_to_move = input("Please enter the piece name you want to move. Use the board as guide: ")
    new_position = input("Please enter the position you want to move it to in normal chess notation: ")
    if(WhiteTurn == True and piece_to_move[0] == "W"):
        print(play(piece_to_move, new_position))
        if(move_successful == True):
            WhiteTurn  = False
            BlackTurn = True
    elif(BlackTurn  == True and piece_to_move[0] == "B"):
        print(play(piece_to_move, new_position))
        if(move_successful == True):
            WhiteTurn  = True
            BlackTurn = False
    else:
        print("\nPlease check your piece input! Use the board as guide.")
        #exit = input("Please press 1 if you will like to exit: ")
    


    