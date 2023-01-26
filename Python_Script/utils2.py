

def threatened_squares_knight(knight, Board, squares):
    ###
    # threatened_squares_knight- This function aims to get the squares threatened by knights
    # Description: This function gets all the squares threatened by any given knight on the board
    # @knight: This is the exact knight piece to check threats for
    # @Board: The exact Board instance to scan
    # @squares: This is the list of standard chess squares it needs to pass to the individual piece functions checking for threats
    # Return: Returns a list of all squares threatened by a given knight
    ###
    knight_threatened_squares = []
    x_coord = 0
    y_coord = 0

    for key, value in Board.items():
        if value[2] == knight:
            x_coord = value[0]
            y_coord = value[1]

            for square_key, values in squares.items():
                num = (values[0] - x_coord)
                div = (values[1] - y_coord)
                if (div != 0 and (num >= -2 and num <= 2) and (
                        div >= -2 and div <= 2)):  # ensures the denominator is not zero. to avoid ZeroDivisionError
                    check = num / div
                    if (
                            check == 0.5 or check == -0.5 or check == 2 or check == -2):  # Checks to see all the valid possible positions the knight can move to
                        if (Board[square_key][2] != ""):  # Checks if the square is not empty
                            knight_threatened_squares.append(square_key)  # Appends all the possible squares to the threatened square list.
                        else:
                            knight_threatened_squares.append(square_key)  # Appends all the possible squares to the threatened square list.
    return (knight_threatened_squares)

def threatened_squares_rook(Rook, Board, squares):
    ###
    # threatened_squares_rook- This function aims to get the squares threatened by rooks
    # Description: This function gets all the squares threatened by any given rook on the board
    # @Rook: This is the exact rook piece to check threats for
    # @Board: The exact Board instance to scan
    # @squares: This is the list of standard chess squares it needs to pass to the individual piece functions checking for threats
    # Return: Returns a list of all squares threatened by a given rook
    ###
    x_coord = 0
    y_coord = 0
    rook_threatened_squares = []
    for key, value in Board.items():
        if value[2] == Rook:
            x_coord = value[0]
            y_coord = value[1]

            for square_key, values in squares.items():
                num = (values[0]-x_coord)
                div = (values[1]-y_coord)
                if(num == 0 or div == 0): #Checks to see all the valid possible positions the rook can move to
                    if (Board[square_key][2] != ""):#Checks if the square is not empty
                        rook_threatened_squares.append(
                            square_key)  # Appends all the possible squares to the threatened square list.
                    else:
                        rook_threatened_squares.append(square_key)  # Appends all the possible squares to the threatened square list.

    return (rook_threatened_squares)

def threatened_squares_bishop(Bishop, Board, squares):
    ###
    # threatened_squares_bishop- This function aims to get the squares threatened by bishop
    # Description: This function gets all the squares threatened by any given bishop on the board
    # @Bishop: This is the exact knight piece to check threats for
    # @Board: The exact Board instance to scan
    # @squares: This is the list of standard chess squares it needs to pass to the individual piece functions checking for threats
    # Return: Returns a list of all squares threatened by a given bishop
    ###
    x_coord = 0
    y_coord = 0
    bishop_threatened_squares = []
    for key, value in Board.items():
        if value[2] == Bishop:
            x_coord = value[0]
            y_coord = value[1]

            for square_key, values in squares.items():
                num = (values[0] - x_coord)
                div = (values[1] - y_coord)
                if (div != 0):  # ensures the denominator is not zero. to avoid ZeroDivisionError
                    check = num / div
                    if (check == 1 or check == -1):  # Checks to see all the valid possible positions the bishop can move to
                        if (Board[square_key][2] != ""):  # Checks if the square is not empty
                            bishop_threatened_squares.append(
                                square_key)  # Appends all the possible squares to the threatened square list.
                        else:
                            bishop_threatened_squares.append(
                                square_key)  # Appends all the possible squares to the threatened square list.

    return (bishop_threatened_squares)

def threatened_squares_queen(Queen, Board, squares):
    ###
    # threatened_squares_queen- This function aims to get the squares threatened by queens
    # Description: This function gets all the squares threatened by any given queen on the board
    # @Queen: This is the exact knight piece to check threats for
    # @Board: The exact Board instance to scan
    # @squares: This is the list of standard chess squares it needs to pass to the individual piece functions checking for threats
    # Return: Returns a list of all squares threatened by a given Queen
    ###
    queen_threatened_squares = []
    for key, value in Board.items():
        if value[2] == Queen:
            x_coord = value[0]
            y_coord = value[1]
            for square_key, values in squares.items():
                num = (values[0] - x_coord)
                div = (values[1] - y_coord)
                if (
                        num == 0 or div == 0):  # Checks to see all the valid possible positions the queen(Horizontal and vertical moves) can move to
                    if (Board[square_key][2] != ""):
                        queen_threatened_squares.append(
                            square_key)  # Appends all the possible squares to the threatened square list.
                    else:
                        queen_threatened_squares.append(
                            square_key)  # Appends all the possible squares to the threatened square list.
                if (div != 0):  # ensures the denominator is not zero. to avoid ZeroDivisionError
                    check = num / div
                    if (
                            check == 1 or check == -1):  # Checks to see all the valid possible positions the Queen(diagonal) can move to
                        if (Board[square_key][2] != ""):  # Checks if the square is not empty
                            queen_threatened_squares.append(
                                square_key)  # Appends all the possible squares to the threatened square list.
                        else:
                            queen_threatened_squares.append(
                                square_key)  # Appends all the possible squares to the threatened square list.
    return (queen_threatened_squares)

def threatened_squares_pawn(Pawn, Board, squares):
    ###
    # threatened_squares_pawn- This function aims to get the squares threatened by pawns
    # Description: This function gets all the squares threatened by any given pawn on the board
    # @pawn: This is the exact pawn piece to check threats for
    # @Board: The exact Board instance to scan
    # @squares: This is the list of standard chess squares it needs to pass to the individual piece functions checking for threats
    # Return: Returns a list of all squares threatened by a given pawn
    ###
    x_coord = 0
    y_coord = 0
    pawn_threatened_squares = []
    for key, value in Board.items():
        if value[2] == Pawn:
            x_coord = value[0]
            y_coord = value[1]

            if (Pawn[0] == "W"):  # Checks if it is a white pawn moving
                for square_key, values in squares.items():
                    if ((values[0] == (value[0] + 1) and values[1] == (value[1] + 1)) or (
                            values[0] == (value[0] - 1) and values[1] == (value[1] + 1))):
                        if (Board[square_key][2] != ""):  # Checks if the square is not empty
                            pawn_threatened_squares.append(square_key)
                        else:
                            pawn_threatened_squares.append(square_key)
            elif (Pawn[0] == "B"):  # checks if it is a black pawn moving
                for square_key, values in squares.items():
                    if ((values[0] == (value[0] + 1) and values[1] == (value[1] - 1)) or (
                            values[0] == (value[0] - 1) and values[1] == (value[1] - 1))):
                        if (Board[square_key][2] != ""):  # Checks if the square is not empty
                            pawn_threatened_squares.append(square_key)
                        else:
                            pawn_threatened_squares.append(square_key)

    return (pawn_threatened_squares)

def threatened_squares_king(King, Board, squares):
    ###
    # threatened_squares_king- This function aims to get the squares threatened by kings
    # Description: This function gets all the squares threatened by any given king on the board
    # @King: This is the exact king piece to check threats for
    # @Board: The exact Board instance to scan
    # @squares: This is the list of standard chess squares it needs to pass to the individual piece functions checking for threats
    # Return: Returns a list of all squares threatened by a given king
    ###
    x_coord = 0
    y_coord = 0
    king_threatened_squares = []

    for key, value in Board.items():
        if value[2] == King:
            x_coord = value[0]
            y_coord = value[1]

            for square_key, values in squares.items():
                if (((values[0] - value[0] == 0) and (values[1] - value[1] == 1)) or (
                        (values[0] - value[0] == 1) and (values[1] - value[1] == 0)) or (
                        (values[0] - value[0] == -1) and (values[1] - value[1] == 0)) or (
                        (values[0] - value[0] == 0) and (values[1] - value[1] == -1)) or (
                        (values[0] - value[0] == 1) and (values[1] - value[1] == 1)) or (
                        (values[0] - value[0] == -1) and (values[1] - value[1] == 1)) or (
                        (values[0] - value[0] == 1) and (values[1] - value[1] == -1)) or (
                        (values[0] - value[0] == -1) and (values[1] - value[1] == -1))):
                    if (Board[square_key][2] != ""):  # Checks if the square is not empty
                        king_threatened_squares.append(square_key)
                    else:
                        king_threatened_squares.append(square_key)

    return (king_threatened_squares)