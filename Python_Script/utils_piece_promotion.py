def is_promotion_move(piece, destination_square):
    if(str(piece[1]).lower() == 'p'):
        return (str(piece[0]).lower() == 'w' and int(destination_square[1]) == 8) or (str(piece[0]).lower() == 'b' and int(destination_square[1]) == 1)
    else:
      return False

def get_promoted_official(desired_official, current_number, color):
    return str(color).upper() + str(desired_official).upper() + str(current_number+1)


#print(get_promoted_official('q', 1, 'w'))