FROM python:3.9 
# Or any preferred Python version.
ADD main.py .
ADD util_constants.py .
ADD utils_castling.py .
ADD utils_enpassant.py .
ADD utils_king_check.py .
ADD utils_piece_promotion.py .
ADD utils_pinned_pieces.py .
ADD utils_threatened_squares_specific.py .
ADD utils_valid_moves_specific.py .
RUN pip3 install numpy pandas
CMD ["python3", "./main.py"] 
# Build command: docker build -t chess_docker .  
# Run command:  docker run -i -t chess_docker   