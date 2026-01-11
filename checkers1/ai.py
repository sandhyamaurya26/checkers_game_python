import random
def ai_move(board):
    """
    AI (computer) ek random move karega black pieces (B) ke liye.
    board: Board object (board.py se)
    """
    pieces = board.get_pieces()
    all_moves = []

    for idx, piece in enumerate(pieces):
        if piece.get_color() == "B":  # AI ka color Black
            moves = piece.get_moves(board)
            if moves:
                for move in moves:
                    all_moves.append((idx, int(move)))

    if not all_moves:
        print("Doesn't have any move to ai . game over!.")
        return False

    # Randomly ek move choose karo
    piece_index, move_position = random.choice(all_moves)
    board.move_piece(piece_index, move_position)

    return True 