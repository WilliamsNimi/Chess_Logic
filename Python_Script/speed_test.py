from datetime import datetime
from utils_threatened_squares_specific import *
from utils2 import *

sampleBoard = {"a1":[0,0,""],"b1":[1,0,"WQN"],"c1":[2,0,""],"d1":[3,0,""],"e1":[4,0,""], "f1":[5,0,"WKB"], "g1":[6,0,""], "h1":[7,0,"WKR"], 
         
"a2":[0,1,""],"b2":[1,1,"Wp2"],"c2":[2,1,"Wp3"],"d2":[3,1,"Wp4"],"e2":[4,1,"Wp5"], "f2":[5,1,"Wp6"], "g2":[6,1,"Wp7"], "h2":[7,1,"Wp8"],
         
"a3":[0,2,"Wp1"],"b3":[1,2,""],"c3":[2,2,""],"d3":[3,2,""],"e3":[4,2,""], "f3":[5,2,"WKN"], "g3":[6,2,""], "h3":[7,2,""],

"a4":[0,3,""],"b4":[1,3,""],"c4":[2,3,"WQR"],"d4":[3,3,""],"e4":[4,3,"WK"], "f4":[5,3,""], "g4":[6,3,"WQ"], "h4":[7,3,""],  

"a5":[0,4,""],"b5":[1,4,"BQ"],"c5":[2,4,""],"d5":[3,4,"BQB"],"e5":[4,4,""], "f5":[5,4,""], "g5":[6,4,"BKR"], "h5":[7,4,""],

"a6":[0,5,""],"b6":[1,5,""],"c6":[2,5,"BK"],"d6":[3,5,""],"e6":[4,5,"WQB"], "f6":[5,5,"BKN"], "g6":[6,5,""], "h6":[7,5,""],

"a7":[0,6,"Bp8"],"b7":[1,6,"Bp7"],"c7":[2,6,"Bp6"],"d7":[3,6,"Bp5"],"e7":[4,6,"Bp4"], "f7":[5,6,"Bp3"], "g7":[6,6,"Bp2"], "h7":[7,6,"Bp1"], 

"a8":[0,7,"BQR"],"b8":[1,7,"BQN"],"c8":[2,7,""],"d8":[3,7,""],"e8":[4,7,""], "f8":[5,7,"BKB"], "g8":[6,7,""], "h8":[7,7,""]
         
         }

def get_piece_from_position(position, board):
  return board[position][2]

def timer(function_to_test, args):
  start_time = datetime.now()
  function_to_test(*args)
  end_time = datetime.now()
  return (end_time - start_time).microseconds

# #Pawn
# samplePawnPosition = 'd7'
# samplePawnPiece = sampleBoard[samplePawnPosition][2]

# print(timer(threatened_squares_pawn, [samplePawnPiece, sampleBoard, squares]))
# print(timer(pawn_threatened_squares, [samplePawnPosition, sampleBoard]))

# #Knight
# sampleKnightPosition = 'f6'
# sampleKnightPiece = sampleBoard[sampleKnightPosition][2]

# print(timer(threatened_squares_knight, [sampleKnightPiece, sampleBoard, squares]))
# print(timer(knight_threatened_squares, [sampleKnightPosition, sampleBoard]))

# #Rook
# sampleRookPosition = 'f6'
# sampleRookPiece = sampleBoard[sampleRookPosition][2]

# print(timer(threatened_squares_rook, [sampleRookPiece, sampleBoard, squares]))
# print(timer(rook_threatened_squares, [sampleRookPosition, sampleBoard]))

# #Bishop
# sampleBishopPosition = 'f6'
# sampleBishopPiece = sampleBoard[sampleBishopPosition][2]

# print(timer(threatened_squares_bishop, [sampleBishopPiece, sampleBoard, squares]))
# print(timer(bishop_threatened_squares, [sampleBishopPosition, sampleBoard]))

# #Queen
# sampleQueenPosition = 'b5'
# sampleQueenPiece = sampleBoard[sampleQueenPosition][2]

# print(timer(threatened_squares_queen, [sampleQueenPiece, sampleBoard, squares]))
# print(timer(queen_threatened_squares, [sampleQueenPosition, sampleBoard]))

#King
sampleKingPosition = 'b5'
sampleKingPiece = sampleBoard[sampleKingPosition][2]

print(timer(threatened_squares_king, [sampleKingPiece, sampleBoard, squares]))
print(timer(king_threatened_squares, [sampleKingPosition, sampleBoard]))