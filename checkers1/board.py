from utils import get_position_with_row_col

class Board:
    def __init__(self, pieces, color_up):
        self.pieces = pieces
        self.color_up = color_up  # 'W' ya 'B'

    def get_color_up(self):
        return self.color_up

    def switch_turn(self):
        self.color_up = 'B' if self.color_up == 'W' else 'W'

    def get_pieces(self):
        return self.pieces

    def get_piece_by_index(self, index):
        return self.pieces[index]

    def has_piece(self, position):
        string_pos = str(position)
        for piece in self.pieces:
            if piece.get_position() == string_pos:
                return True
        return False

    def get_row_number(self, position):
        return position // 4

    def get_col_number(self, position):
        remainder = position % 4
        column_position = remainder * 2
        is_row_odd = not (self.get_row_number(position) % 2 == 0)
        return column_position + 1 if is_row_odd else column_position

    def get_row(self, row_number):
        row_pos = [str(pos + 4 * row_number) for pos in range(4)]
        return set([piece for piece in self.pieces if piece.get_position() in row_pos])

    def get_pieces_by_coords(self, *coords):
        row_memory = {}
        results = []
        for coord_pair in coords:
            if coord_pair[0] in row_memory:
                current_row = row_memory[coord_pair[0]]
            else:
                current_row = self.get_row(coord_pair[0])
                row_memory[coord_pair[0]] = current_row

            for piece in current_row:
                if self.get_col_number(int(piece.get_position())) == coord_pair[1]:
                    results.append(piece)
                    break
            else:
                results.append(None)
        return results

    def move_piece(self, index, new_position):
        piece_to_move = self.pieces[index]

        # Eat move check
        def is_eat_movement():
            return abs(self.get_row_number(int(piece_to_move.get_position())) - self.get_row_number(new_position)) != 1

        def get_eaten_index():
            current_row = self.get_row_number(int(piece_to_move.get_position()))
            current_col = self.get_col_number(int(piece_to_move.get_position()))
            new_row = self.get_row_number(new_position)
            new_col = self.get_col_number(new_position)
            eaten_row = (current_row + new_row) // 2
            eaten_col = (current_col + new_col) // 2
            eaten_pos = str(get_position_with_row_col(eaten_row, eaten_col))
            for idx, piece in enumerate(self.pieces):
                if piece.get_position() == eaten_pos:
                    return idx

        def is_king_movement():
            if piece_to_move.is_king():
                return False
            end_row = self.get_row_number(new_position)
            king_row = 0 if self.color_up == piece_to_move.get_color() else 7
            return end_row == king_row

        # Eat logic
        if is_eat_movement():
            self.pieces.pop(get_eaten_index())

        # King logic
        if is_king_movement():
            piece_to_move.set_is_king(True)

        # Move the piece
        piece_to_move.set_position(new_position)
