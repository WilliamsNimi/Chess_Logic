
from utils_castling import board_letters
def move_validity_knight(knight_move, Board):
    """
    1. Checks the validity of a knight's move. Typically, the distance((x1 -x2)/(y1-y2)) between the current position (x1, y1) of a knight and the proposed posiiton (x2, y2) should be -0.5, or 0.5, or -2. or 2
    2. Also checks to see if the square is emply or contains a piece of the same color

    returns True if move is valid and false otherwise

    """

    x_coord = 0
    y_coord = 0
    for key, value in Board.items():
        if key == knight_move[1]:
            x_coord = Board[knight_move[2]][0]
            y_coord = Board[knight_move[2]][1]

            if((((x_coord - value[0] ) /(y_coord - value[1])) == -0.5 or
                    (((x_coord - value[0]) / (y_coord - value[1])) == -2) or (
                         (x_coord - value[0]) / (y_coord - value[1])) == 2 or (
                         (x_coord - value[0]) / (y_coord - value[1])) == 0.5) and (
                    value[2] == "" or value[2][0] != knight_move[0][0])):
                return True


def move_validity_Rook(move, Board):
    """
    1. Checks the validity of a Rook's move. A move is valid for a rook at position (x1, y1), moving to (x2, y2) is either (X1 - X2) = 0 or (y1 - y2) = 0
    2. Also checks to see if the square is emply or contains a piece of the same color
    3. Also checks to see that all valid squares before that square are empty, since Rooks don't jump over pieces'

    returns True if move is valid and false otherwise

    """

    x_coord = 0
    y_coord = 0
    for key, value in Board.items():
        if key == move[1]:
            x_coord = Board[move[2]][0]
            y_coord = Board[move[2]][1]

            if (((x_coord - value[0]) == 0 or (y_coord - value[1]) == 0) and (
                    value[2] == "" or value[2][0] != move[0][0])):
                if ((x_coord - value[0] == 0)):
                    if ((y_coord - value[1]) < 0):
                        while (y_coord < int(move[1][1]) - 1):
                            y_coord += 1
                            strKey = board_letters[x_coord] + str(y_coord + 1)
                            if (Board[strKey][2] != ""):
                                return False
                    elif ((y_coord - value[1]) > 0):
                        while (y_coord > int(move[1][1]) - 1):
                            y_coord -= 1
                            strKey = board_letters[x_coord] + str(y_coord + 1)
                            if (Board[strKey][2] != ""):
                                return False
                elif ((y_coord - value[1] == 0)):
                    count = 0
                    if ((x_coord - value[0]) < 0):
                        while (x_coord < int(move[1][1]) - 1):
                            x_coord += 1
                            strKey = board_letters[x_coord + 1] + str(y_coord)
                            if (Board[strKey][2] != ""):
                                return False
                            count += 1
                    elif ((x_coord - value[0]) > 0):
                        while (x_coord > int(move[1][1]) - 1):
                            x_coord -= 1
                            strKey = board_letters[x_coord - 1] + str(y_coord)
                            if (Board[strKey][2] != ""):
                                return False
                return True


def move_validity_Bishop(move, Board):
    """
    1. Checks the validity of a Bishop's move. Typically, the distance((x1 -x2)/(y1-y2)) between the current position (x1, y1) of a Bishop and the proposed posiiton (x2, y2) should be -1 or 1
    2. Also checks to see if the square is emply or contains a piece of the same color
    3. Also checks to see that all valid squares before that square are empty, since Bishops don't jump over pieces'

    returns True if move is valid and false otherwise
    """
    x_coord = 0
    y_coord = 0
    for key, value in Board.items():
        if key == move[1]:
            x_coord = Board[move[2]][0]
            y_coord = Board[move[2]][1]

            if ((((x_coord - value[0]) / (y_coord - value[1])) == -1 or (
                    (x_coord - value[0]) / (y_coord - value[1])) == 1) and (
                    value[2] == "" or value[2][0] != move[0][0])):
                if (((x_coord - value[0]) / (y_coord - value[1])) == 1):
                    while (y_coord < int(move[1][1]) - 1):
                        y_coord += 1
                        strKey = board_letters[x_coord + 2] + str(y_coord + 2)
                        if (Board[strKey][2] != ""):
                            return False
                elif (((x_coord - value[0]) / (y_coord - value[1])) == -1):
                    if (y_coord < int(move[1][1])):
                        while (y_coord < int(move[1][1])):
                            y_coord += 1
                            strKey = board_letters[x_coord - 2] + str(y_coord + 2)
                            if (Board[strKey][2] != ""):
                                return False
                    elif (y_coord > int(move[1][1])):
                        while (y_coord > int(move[1][1])):
                            x_coord += 1
                            strKey = board_letters[x_coord] + str(y_coord)
                            if (Board[strKey][2] != ""):
                                return False
                            y_coord -= 1

                return True


def move_validity_Queen(move, Board):
    if (move_validity_Bishop(move) == True or move_validity_Rook(move) == True):
        return True
    else:
        return False


def move_validity_pawn(move, Board):
    """ This function calculates the validity of a pawn move. The difference between the new square and the old square for a white pawn is always negative. That of the black pawn is always positive (Because we started out coordinats with a1 being 0,0). To move either the white or the black pawn, check that the x coordinates of the old and new position are the same (Except during capture), also check that the difference in y coordinate is not more than 2, check that the pawn is in its initial position. For black, the old position will have a 7, for white, it will have a 2.

    TO:DO En passant and promotion

    """
    x_coord = 0
    y_coord = 0
    for key, value in Board.items():
        if key == move[1]:
            x_coord = Board[move[2]][0]
            y_coord = Board[move[2]][1]

            if (int(move[2][1]) == 7 or int(move[2][1]) == 2):  # Check that the pawn is yet to move
                if (((y_coord - value[1]) == 1 or (y_coord - value[1]) == 2 or (y_coord - value[1]) == -1 or (
                        y_coord - value[1]) == -2) and (x_coord - value[0]) == 0):  # validates basic pawn move
                    return True
            elif (Board[board_letters[x_coord] + str(y_coord)][2] != "" and
                  Board[board_letters[x_coord] + str(y_coord)][2][0] != move[0][0]):  # validates capture
                return True
            elif ((y_coord - value[1] == -1 and move[0][0] == "W") or (y_coord - value[1] == 1 and move[0][0] == "B")):
                return True


def move_validity_king(move, Board):
    """This function calculates the validity of a King move and returns a boolean value. The king can only move 1 step in any direction. Thus, the difference between the current position and new position cannot be greater than 1 or -1. i.e. y2 -y1 not greater than 1 or -1. x2 - x1 not greater than 1 or -1"""
    x_coord = 0
    y_coord = 0

    for key, value in Board.items():
        if key == move[1]:
            x_coord = Board[move[2]][0]
            y_coord = Board[move[2]][1]

            if (value[2] != ""):
                return False
            if (((y_coord - value[1]) == 1 and (x_coord - value[0]) == 0) or (
                    (y_coord - value[1]) == -1 and (x_coord - value[0]) == 0) or (
                    (x_coord - value[0]) == 1 and (y_coord - value[1]) == 0) or (
                    (x_coord - value[0]) == 1 and (y_coord - value[1]) == -1) or (
                    (x_coord - value[0]) == -1 and (y_coord - value[1]) == -1) or (
                    (x_coord - value[0]) == -1 and (y_coord - value[1]) == 0) or (
                    (x_coord - value[0]) == -1 and (y_coord - value[1]) == 1) or (
                    (x_coord - value[0]) == 1 and (y_coord - value[1]) == 1)):
                return True