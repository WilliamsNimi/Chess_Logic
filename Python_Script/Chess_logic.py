# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 06:21:01 2022

@author: Nimi Williams
"""
import numpy as np
import pandas as pd


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

Board = {"a1":[0,0,"WQR"],"b1":[1,0,"WQN"],"c1":[2,0,"WQB"],"d1":[3,0,"WQ"],"e1":[4,0,"WK"], "f1":[5,0,"WKB"], "g1":[6,0,"WKN"], "h1":[7,0,"WKR"], 
         
"a2":[0,1,"Wp1"],"b2":[1,1,"Wp2"],"c2":[2,1,"Wp3"],"d2":[3,1,"Wp4"],"e2":[4,1,"Wp5"], "f2":[5,1,"Wp6"], "g2":[6,1,"Wp7"], "h2":[7,1,"Wp8"],
         
"a3":[0,2,""],"b3":[1,2,""],"c3":[2,2,""],"d3":[3,2,""],"e3":[4,2,""], "f3":[5,2,""], "g3":[6,2,""], "h3":[7,2,""],

"a4":[0,3,""],"b4":[1,3,""],"c4":[2,3,""],"d4":[3,3,""],"e4":[4,3,""], "f4":[5,3,""], "g4":[6,3,""], "h4":[7,3,""],  

"a5":[0,4,""],"b5":[1,4,""],"c5":[2,4,""],"d5":[3,4,""],"e5":[4,4,""], "f5":[5,4,""], "g5":[6,4,""], "h5":[7,4,""],

"a6":[0,5,""],"b6":[1,5,""],"c6":[2,5,""],"d6":[3,5,""],"e6":[4,5,""], "f6":[5,5,""], "g6":[6,5,""], "h6":[7,5,""],

"a7":[0,6,"Bp8"],"b7":[1,6,"Bp7"],"c7":[2,6,"Bp6"],"d7":[3,6,"Bp5"],"e7":[4,6,"Bp4"], "f7":[5,6,"Bp3"], "g7":[6,6,"Bp2"], "h7":[7,6,"Bp1"], 

"a8":[0,7,"BQR"],"b8":[1,7,"BQN"],"c8":[2,7,"BQB"],"d8":[3,7,"BQ"],"e8":[4,7,"BK"], "f8":[5,7,"BKB"], "g8":[6,7,"BKN"], "h8":[7,7,"BKR"]
         
         }

squares = {"a1":(0,0),"b1":(1,0),"c1":(2,0),"d1":(3,0),"e1":(4,0),"f1":(5,0),"g1":(6,0),"h1":(7,0),"a2":(0,1),"b2":(1,1),"c2":(2,1),"d2":(3,1),"e2":(4,1),"f2":(5,1),"g2":(6,1),"h2":(7,1),"a3":(0,2),"b3":(1,2),"c3":(2,2),"d3":(3,2),"e3":(4,2),"f3":(5,2),"g3":(6,2),"h3":(7,2),"a4":(0,3),"b4":(1,3),"c4":(2,3),"d4":(3,3),"e4":(4,3),"f4":(5,3),"g4":(6,3),"h4":(7,3),"a5":(0,4),"b5":(1,4),"c5":(2,4),"d5":(3,4),"e5":(4,4),"f5":(5,4),"g5":(6,4),"h5":(7,4),"a6":(0,5),"b6":(1,5),"c6":(2,5),"d6":(3,5),"e6":(4,5),"F6":(5,5),"g6":(6,5),"h6":(7,5),"a7":(0,6),"b7":(1,6),"c7":(2,6),"d7":(3,6),"e7":(4,6),"f7":(5,6),"g7":(6,6),"h7":(7,6),"a8":(0,7),"b8":(1,7),"c8":(2,7),"d8":(3,7),"e8":(4,7),"f8":(5,7),"g8":(6,7),"h8":(7,7)}
inverted_squares_map = {'0,0': 'a1', '1,0': 'b1', '2,0': 'c1', '3,0': 'd1', '4,0': 'e1', '5,0': 'f1', '6,0': 'g1', '7,0': 'h1', '0,1': 'a2', '1,1': 'b2', '2,1': 'c2', '3,1': 'd2', '4,1': 'e2', '5,1': 'f2', '6,1': 'g2', '7,1': 'h2', '0,2': 'a3', '1,2': 'b3', '2,2': 'c3', '3,2': 'd3', '4,2': 'e3', '5,2': 'f3', '6,2': 'g3', '7,2': 'h3', '0,3': 'a4', '1,3': 'b4', '2,3': 'c4', '3,3': 'd4', '4,3': 'e4', '5,3': 'f4', '6,3': 'g4', '7,3': 'h4', '0,4': 'a5', '1,4': 'b5', '2,4': 'c5', '3,4': 'd5', '4,4': 'e5', '5,4': 'f5', '6,4': 'g5', '7,4': 'h5', '0,5': 'a6', '1,5': 'b6', '2,5': 'c6', '3,5': 'd6', '4,5': 'e6', '5,5': 'F6', '6,5': 'g6', '7,5': 'h6', '0,6': 'a7', '1,6': 'b7', '2,6': 'c7', '3,6': 'd7', '4,6': 'e7', '5,6': 'f7', '6,6': 'g7', '7,6': 'h7', '0,7': 'a8', '1,7': 'b8', '2,7': 'c8', '3,7': 'd8', '4,7': 'e8', '5,7': 'f8', '6,7': 'g8', '7,7': 'h8'}

threatened_squares = {}

board_letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

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

def isValidBoardCoordinates(x_coord, y_coord):
    VALID_X_COORD = x_coord>=0 and x_coord<=7
    VALID_Y_COORD = y_coord>=0 and y_coord<=7
    return VALID_X_COORD and VALID_Y_COORD

def pawn_threatened_squares(current_position, current_board):
    pawn_threats = []
    x_coord = squares[current_position][0]
    y_coord = squares[current_position][1]
    top_right_square_is_valid = isValidBoardCoordinates(x_coord+1, y_coord+1)
    top_left_square_is_valid = isValidBoardCoordinates(x_coord-1, y_coord+1)
    right_target_position = inverted_squares_map[str(x_coord+1)+','+str(y_coord+1)]
    left_target_position = inverted_squares_map[str(x_coord-1)+','+str(y_coord+1)]
    right_target_piece = current_board[right_target_position][2]
    left_target_piece = current_board[left_target_position][2]
    color = current_board[current_position][2][0]

    #Check if the top right square is valid, empty or of a different color
    if(top_right_square_is_valid and len(right_target_piece)==0):
        pawn_threats.append(right_target_position)
    if(top_right_square_is_valid and len(right_target_piece)>=1 and right_target_piece[0]!=color):
        pawn_threats.append(right_target_position)
    #Check if the top left square is valid, empty or of a different color
    if(top_left_square_is_valid and len(left_target_piece)==0):
        pawn_threats.append(left_target_position)
    if(top_left_square_is_valid and len(left_target_piece)>=1 and left_target_piece[0]!=color):
        pawn_threats.append(left_target_position)
    return pawn_threats

def move_validity_knight(knight_move):
    """
    1. Checks the validity of a knight's move. Typically, the distance((x1 -x2)/(y1-y2)) between the current position (x1, y1) of a knight and the proposed posiiton (x2, y2) should be -0.5, or 0.5, or -2. or 2
    2. Also checks to see if the square is emply or contains a piece of the same color
    
    returns True if move is valid and false otherwise
    
    """
    knight_threatened_squares = []
    x_coord = 0
    y_coord = 0
    for key, value in Board.items():
        if key == knight_move[1]:
            x_coord = Board[knight_move[2]][0]
            y_coord = Board[knight_move[2]][1]
            print(value[2])
            
            if knight_move[1] in squares:
                for square_key, values in squares.items():
                    num = (values[0]-squares[knight_move[1]][0])
                    div = (values[1]-squares[knight_move[1]][1])
                    if(div != 0 and (num >= -2 and num <=2) and (div >= -2 and div <=2)): #ensures the denominator is not zero. to avoid ZeroDivisionError
                        check = num/div
                        if(check == 0.5 or check == -0.5 or check == 2 or check == -2): #Checks to see all the valid possible positions the knight can move to
                            if(square_key not in threatened_squares):
                                if(Board[square_key][2] != ""):#Checks if the square is not empty
                                    if(Board[square_key][2][0] != knight_move[0][0]):#Checks if the color of the piece occupying the square is the same as the piece that is attacking it.
                                        knight_threatened_squares.append(square_key) #Appends all the possible squares to the threatened square list.
                                else:
                                    knight_threatened_squares.append(square_key)  # Appends all the possible squares to the threatened square list.
            knight_threatened_squares.append(knight_move[2])
            threatened_squares[knight_move[0]] = knight_threatened_squares
            print(threatened_squares)
            
            if((((x_coord - value[0])/(y_coord - value[1])) == -0.5 or (((x_coord - value[0])/(y_coord - value[1])) == -2) or ((x_coord - value[0])/(y_coord - value[1])) == 2 or ((x_coord - value[0])/(y_coord - value[1])) == 0.5) and (value[2] == "" or value[2][0]!=knight_move[0][0])):
                return True
            
def move_validity_Rook(move):
    """
    1. Checks the validity of a Rook's move. A move is valid for a rook at position (x1, y1), moving to (x2, y2) is either (X1 - X2) = 0 or (y1 - y2) = 0 
    2. Also checks to see if the square is emply or contains a piece of the same color
    3. Also checks to see that all valid squares before that square are empty, since Rooks don't jump over pieces'
    
    returns True if move is valid and false otherwise
    
    """
    
    x_coord = 0
    y_coord = 0
    rook_threatened_squares = []
    for key, value in Board.items():
        if key == move[1]:
            x_coord = Board[move[2]][0]
            y_coord = Board[move[2]][1]

            if move[1] in squares:
                for square_key, values in squares.items():
                    num = (values[0]-squares[move[1]][0])
                    div = (values[1]-squares[move[1]][1])
                    if(num == 0 or div == 0): #Checks to see all the valid possible positions the rook can move to
                        if(square_key not in threatened_squares):
                            if (Board[square_key][2] != ""):#Checks if the square is not empty
                                if (Board[square_key][2][0] != move[0][0]):#Checks if the color of the piece occupying the square is the same as the piece that is attacking it.
                                    rook_threatened_squares.append(
                                        square_key)  # Appends all the possible squares to the threatened square list.
                            else:
                                rook_threatened_squares.append(square_key)  # Appends all the possible squares to the threatened square list.

            rook_threatened_squares.append(move[2])
            threatened_squares[move[0]] = rook_threatened_squares
            print(threatened_squares)
            
            if(((x_coord - value[0]) == 0 or (y_coord - value[1]) == 0) and (value[2] == "" or value[2][0]!= move[0][0])):
                if((x_coord - value[0] == 0)):
                    if((y_coord - value[1])< 0):
                        while(y_coord < int(move[1][1]) - 1):
                            y_coord += 1
                            strKey = board_letters[x_coord] + str(y_coord + 1)
                            if(Board[strKey][2] != ""):
                                return False
                    elif((y_coord - value[1])> 0):
                        while(y_coord > int(move[1][1])-1):
                            y_coord -= 1
                            strKey = board_letters[x_coord] + str(y_coord-1)
                            if(Board[strKey][2] != ""):
                                return False
                elif((y_coord - value[1] == 0)):
                    count = 0
                    if((x_coord - value[0])< 0):
                        while(x_coord < int(move[1][1]) - 1):
                            x_coord += 1
                            strKey = board_letters[x_coord+1] + str(y_coord)
                            if(Board[strKey][2] != ""):
                                return False
                            count+=1
                    elif((x_coord - value[0])> 0):
                        while(x_coord > int(move[1][1])-1):
                            x_coord -= 1
                            strKey = board_letters[x_coord-1] + str(y_coord)
                            if(Board[strKey][2] != ""):
                                return False
                return True


def move_validity_Bishop(move):
    """ 
    1. Checks the validity of a Bishop's move. Typically, the distance((x1 -x2)/(y1-y2)) between the current position (x1, y1) of a Bishop and the proposed posiiton (x2, y2) should be -1 or 1
    2. Also checks to see if the square is emply or contains a piece of the same color
    3. Also checks to see that all valid squares before that square are empty, since Bishops don't jump over pieces'
    
    returns True if move is valid and false otherwise
    """
    x_coord = 0
    y_coord = 0
    bishop_threatened_squares = []
    for key, value in Board.items():
        if key == move[1]:
            x_coord = Board[move[2]][0]
            y_coord = Board[move[2]][1]

            if move[1] in squares:
                for square_key, values in squares.items():
                    num = (values[0]-squares[move[1]][0])
                    div = (values[1]-squares[move[1]][1])
                    if(div != 0): #ensures the denominator is not zero. to avoid ZeroDivisionError
                        check = num/div
                        if(check == 1 or check == -1): #Checks to see all the valid possible positions the bishop can move to
                            if(square_key not in threatened_squares):
                                if (Board[square_key][2] != ""):#Checks if the square is not empty
                                    if (Board[square_key][2][0] != move[0][0]):#Checks if the color of the piece occupying the square is the same as the piece that is attacking it.
                                        bishop_threatened_squares.append(
                                            square_key)  # Appends all the possible squares to the threatened square list.
                                else:
                                    bishop_threatened_squares.append(square_key)  # Appends all the possible squares to the threatened square list.

            bishop_threatened_squares.append(move[2])
            threatened_squares[move[0]] = bishop_threatened_squares
            print(threatened_squares)

            if((((x_coord - value[0])/(y_coord - value[1])) == -1 or ((x_coord - value[0])/(y_coord - value[1])) == 1) and (value[2] == "" or value[2][0]!= move[0][0])):
                if(((x_coord - value[0])/(y_coord - value[1])) == 1):
                    while(y_coord < int(move[1][1]) - 1):
                        y_coord += 1
                        strKey = board_letters[x_coord+2] + str(y_coord+2)
                        if(Board[strKey][2] != ""):
                            return False
                elif(((x_coord - value[0])/(y_coord - value[1])) == -1):
                    if(y_coord < int(move[1][1])):
                        while(y_coord < int(move[1][1])):
                            y_coord += 1
                            strKey = board_letters[x_coord-2] + str(y_coord+2)
                            if(Board[strKey][2] != ""):
                                return False
                    elif(y_coord > int(move[1][1])):
                        while(y_coord > int(move[1][1])):
                            x_coord +=1
                            strKey = board_letters[x_coord] + str(y_coord)
                            if(Board[strKey][2] != ""):
                                return False
                            y_coord -= 1
                
        
                return True
            
def move_validity_Queen(move):
    queen_threatened_squares = []
    if move[1] in squares:
        for square_key, values in squares.items():
            num = (values[0] - squares[move[1]][0])
            div = (values[1] - squares[move[1]][1])
            if (num == 0 or div == 0):  # Checks to see all the valid possible positions the queen(Horizontal and vertical moves) can move to
                if (square_key not in threatened_squares):
                    if (Board[square_key][2] != ""):
                        if (Board[square_key][2][0] != move[0][0]):
                            queen_threatened_squares.append(square_key)  # Appends all the possible squares to the threatened square list.
                    else:
                        queen_threatened_squares.append(square_key)  # Appends all the possible squares to the threatened square list.
            if (div != 0):  # ensures the denominator is not zero. to avoid ZeroDivisionError
                check = num / div
                if (check == 1 or check == -1):  # Checks to see all the valid possible positions the Queen(diagonal) can move to
                    if (square_key not in threatened_squares):
                        if (Board[square_key][2] != ""): #Checks if the square is not empty
                            if (Board[square_key][2][0] != move[0][0]): #Checks if the color of the piece occupying the square is the same as the piece that is attacking it.
                                queen_threatened_squares.append(
                                    square_key)  # Appends all the possible squares to the threatened square list.
                        else:
                            queen_threatened_squares.append(square_key)  # Appends all the possible squares to the threatened square list.
    queen_threatened_squares.append(move[2])
    threatened_squares[move[0]] = queen_threatened_squares
    print(threatened_squares)

    if(move_validity_Bishop(move) == True or move_validity_Rook(move) == True):
        return True
    else:
        return False
    
def move_validity_pawn(move):
    """ This function calculates the validity of a pawn move. The difference between the new square and the old square for a white pawn is always negative. That of the black pawn is always positive (Because we started out coordinats with a1 being 0,0). To move either the white or the black pawn, check that the x coordinates of the old and new position are the same (Except during capture), also check that the difference in y coordinate is not more than 2, check that the pawn is in its initial position. For black, the old position will have a 7, for white, it will have a 2. 
    
    TO:DO En passant and promotion 
    
    """
    x_coord = 0
    y_coord = 0
    pawn_threatened_squares = []
    for key, value in Board.items():
        if key == move[1]:
            x_coord = Board[move[2]][0]
            y_coord = Board[move[2]][1]

            if(move[0][0] == "W"):#Checks if it is a white pawn moving
                for square_key, values in squares.items():
                    if((values[0] == (value[0]+1) and values[1] == (value[1]+1)) or (values[0] == (value[0] - 1) and values[1] == (value[1]+1))):
                        if (Board[square_key][2] != ""):#Checks if the square is not empty
                            if (Board[square_key][2][0] != move[0][0]):#Checks if the color of the piece occupying the square is the same as the piece that is attacking it.
                                pawn_threatened_squares.append(square_key)
                        else:
                            pawn_threatened_squares.append(square_key)
            elif(move[0][0] == "B"):#checks if it is a black pawn moving
                for square_key, values in squares.items():
                    if((values[0] == (value[0]+1) and values[1] == (value[1]-1)) or (values[0] == (value[0] - 1) and values[1] == (value[1]-1))):
                        if (Board[square_key][2] != ""):#Checks if the square is not empty
                            if (Board[square_key][2][0] != move[0][0]):#Checks if the color of the piece occupying the square is the same as the piece that is attacking it.
                                pawn_threatened_squares.append(square_key)
                        else:
                            pawn_threatened_squares.append(square_key)

            threatened_squares[move[0]] = pawn_threatened_squares
            print(threatened_squares)

            if(int(move[2][1]) == 7 or int(move[2][1]) == 2): #Check that the pawn is yet to move
                if(((y_coord - value[1]) == 1 or (y_coord - value[1]) == 2 or (y_coord - value[1]) == -1 or (y_coord - value[1]) == -2) and  (x_coord - value[0]) == 0):#validates basic pawn move
                    return True
            elif(Board[board_letters[x_coord]+str(y_coord)][2] != "" and Board[board_letters[x_coord]+str(y_coord)][2][0] != move[0][0]): #validates capture
                return True
            elif((y_coord - value[1] == -1 and move[0][0] == "W") or (y_coord - value[1] == 1 and move[0][0] == "B")):
                return True
            
def move_validity_king(move):
    """This function calculates the validity of a King move and returns a boolean value. The king can only move 1 step in any direction. Thus, the difference between the current position and new position cannot be greater than 1 or -1. i.e. y2 -y1 not greater than 1 or -1. x2 - x1 not greater than 1 or -1"""
    x_coord = 0
    y_coord = 0
    king_threatened_squares = []


    for key, value in Board.items():
        if key == move[1]:
            x_coord = Board[move[2]][0]
            y_coord = Board[move[2]][1]

            for square_key, values in squares.items():
                if (((values[0] - value[0] == 0) and (values[1] - value[1] == 1)) or ((values[0] - value[0] == 1) and (values[1] - value[1] == 0)) or ((values[0] - value[0] == -1) and (values[1] - value[1] == 0)) or ((values[0] - value[0] == 0) and (values[1] - value[1] == -1))or((values[0] - value[0] == 1) and (values[1] - value[1] == 1)) or((values[0] - value[0] == -1) and (values[1] - value[1] == 1))or((values[0] - value[0] == 1) and (values[1] - value[1] == -1))or((values[0] - value[0] == -1) and (values[1] - value[1] == -1))):
                    if (Board[square_key][2] != ""):#Checks if the square is not empty
                        if (Board[square_key][2][0] != move[0][0]):#Checks if the color of the piece occupying the square is the same as the piece that is attacking it.
                            king_threatened_squares.append(square_key)
                    else:
                        king_threatened_squares.append(square_key)

            king_threatened_squares.append(move[2])
            threatened_squares[move[0]] = king_threatened_squares
            print(threatened_squares)

            if(value[2] != ""):
                return False
            if(((y_coord - value[1]) == 1 and (x_coord - value[0]) == 0) or ((y_coord - value[1]) == -1 and (x_coord - value[0]) == 0) or ((x_coord - value[0]) == 1 and (y_coord - value[1]) == 0) or ((x_coord -  value[0]) == -1 and (x_coord - value[1]) == 0) or ((x_coord - value[0]) == 1 and (y_coord - value[1]) == 1) or ((x_coord - value[0]) == -1 and (y_coord - value[1]) == -1)):
                return True      



def make_move(validCheck, move):
    
    """This functions changes the board values in the dictionary and returns an illegal move message if the move is invalid"""
    global move_successful
    
    if validCheck == True:
        Board[move[1]][2] = move[0]
        Board[move[2]][2] = ""
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
    
    if(piece_to_move[0:2] == "Wp" or piece_to_move[0:2] == "Bp"):
        print(make_move(move_validity_pawn(move), move))
        pieces_moved[piece_to_move] = piece_to_move
    elif(piece_to_move == "WQR" or piece_to_move == "WKR" or piece_to_move == "BQR" or piece_to_move == "BKR"):
        print(make_move(move_validity_Rook(move), move))
        pieces_moved[piece_to_move] = piece_to_move
    elif(piece_to_move == "WQN" or piece_to_move == "WKN" or piece_to_move == "BQN" or piece_to_move == "BKN" ):
        print(make_move(move_validity_knight(move), move))
        pieces_moved[piece_to_move] = piece_to_move
    elif(piece_to_move == "WQB" or piece_to_move == "WKB" or piece_to_move == "BQB" or piece_to_move == "BKB"):
        print(make_move(move_validity_Bishop(move), move))
        pieces_moved[piece_to_move] = piece_to_move
    elif(piece_to_move == "WQ" or piece_to_move == "BQ"):
        print(make_move(move_validity_Queen(move), move))
        pieces_moved[piece_to_move] = piece_to_move
    elif(piece_to_move == "WK" or piece_to_move == "BK"):
        print(make_move(move_validity_king(move), move))
        pieces_moved[piece_to_move] = piece_to_move
    else:
        print("Please check your moves")
        
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
    


    