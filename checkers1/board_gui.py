from board import Board
from piece import Piece
from held_piece import HeldPiece
from utils import get_piece_gui_coords, get_surface_mouse_offset, get_piece_position
import pygame

BLACK_PIECE_SURFACE = pygame.image.load("images/black_piece.png")
WHITE_PIECE_SURFACE = pygame.image.load("images/white_piece.png")
BLACK_KING_PIECE_SURFACE = pygame.image.load("images/black_king_piece.png")
WHITE_KING_PIECE_SURFACE = pygame.image.load("images/white_king_piece.png")
BOARD = pygame.image.load("images/board.png")
TOPLEFTBORDER = (34, 34)
SQUARE_DIST = 56

class BoardGUI:
    def __init__(self, board_rect):
        pieces = []
        for opponent_piece in range(0, 12):
            pieces.append(Piece(str(opponent_piece) + 'BN'))
        for player_piece in range(20, 32):
            pieces.append(Piece(str(player_piece) + 'WN'))

        self.board = Board(pieces, "W")
        self.piece_rects = self.get_piece_rects(pieces)
        self.piece_colors = self.get_piece_colors(pieces)
        self.piece_status = self.get_piece_status(pieces)
        self.board_rect = board_rect
        self.held_piece = None
        self.held_piece_index = -1
        self.move_marks = []

    def get_piece_rects(self, pieces):
        rects = []
        for piece in pieces:
            pos = int(piece.get_position())
            row = self.board.get_row_number(pos)
            column = self.board.get_col_number(pos)
            rects.append(pygame.Rect(get_piece_gui_coords((row, column), SQUARE_DIST, TOPLEFTBORDER), (41, 41)))
        return rects

    def get_piece_colors(self, pieces):
        return [piece.get_color() for piece in pieces]

    def get_piece_status(self, pieces):
        return [piece.is_king() for piece in pieces]

    def draw_gui(self, display_surface):
        self.draw_board(display_surface)
        image_rect = pygame.image.load("images/marking.png")
        if self.held_piece is not None:
            for move_mark in self.move_marks:
                display_surface.blit(image_rect, move_mark)
            self.held_piece.draw_piece(display_surface)

    def draw_board(self, display_surface):
        display_surface.blit(BOARD, self.board_rect)
        for index, piece_rect in enumerate(self.piece_rects):
            if self.held_piece is not None and index == self.held_piece_index:
                continue
            surface = self.get_piece_surface(self.piece_colors[index], self.piece_status[index])
            display_surface.blit(surface, piece_rect)

    def hold_piece_with_mouse(self, mouse_pos, allowed_color=None):
         piece_clicked = self.get_piece_on_mouse(mouse_pos)
         if piece_clicked is not None:
        # Check if this piece color is allowed to move (for turn-based gameplay)
            if allowed_color is not None and piece_clicked.get_color() != allowed_color:
                return  # Don't allow move if wrong color for current player
            
        # Clear any existing move marks before showing new ones
         self.move_marks = []
        
         for possible_move in piece_clicked.get_moves(self.board):
            row = self.board.get_row_number(int(possible_move))
            column = self.board.get_col_number(int(possible_move))
            self.move_marks.append(pygame.Rect(get_piece_gui_coords((row, column), SQUARE_DIST, TOPLEFTBORDER), (44, 44)))
        
        # Only hold piece if it has valid moves
         if self.move_marks:
              self.set_held_piece(int(piece_clicked.get_position()), mouse_pos)

    def release_piece(self):
        move_made = False
        if self.held_piece is not None:
            released_on = self.held_piece.check_collision(self.move_marks)
            if released_on is not None:
                self.board.move_piece(self.held_piece_index, get_piece_position((released_on.x, released_on.y), SQUARE_DIST, TOPLEFTBORDER))
                self.update_board()
                move_made = True
            self.set_held_piece(-1, None)
            self.move_marks = []
        return move_made

    def get_piece_on_mouse(self, mouse_pos):
        for index, piece_rect in enumerate(self.piece_rects):
            if piece_rect.collidepoint(mouse_pos):
                return self.board.get_piece_by_index(index)
        return None

    def set_held_piece(self, position, mouse_pos):
        if position == -1:
            self.held_piece = None
            self.held_piece_index = -1
            return
        piece_row = self.board.get_row_number(position)
        piece_column = self.board.get_col_number(position)
        piece_rect = pygame.Rect(get_piece_gui_coords((piece_row, piece_column), SQUARE_DIST, TOPLEFTBORDER), (41, 41))
        for index, rect in enumerate(self.piece_rects):
            if rect.colliderect(piece_rect):
                piece_to_hold = self.board.get_piece_by_index(index)
                offset = get_surface_mouse_offset(piece_rect, mouse_pos)
                self.held_piece = HeldPiece(self.get_piece_surface(piece_to_hold.get_color(), piece_to_hold.is_king()), offset)
                self.held_piece_index = index

    def get_piece_surface(self, color, is_king):
        piece_surfaces = [BLACK_KING_PIECE_SURFACE, WHITE_KING_PIECE_SURFACE] if is_king else [BLACK_PIECE_SURFACE, WHITE_PIECE_SURFACE]
        return piece_surfaces[0] if color == "B" else piece_surfaces[1]

    def update_board(self):
        pieces = self.board.get_pieces()
        self.piece_rects = self.get_piece_rects(pieces)
        self.piece_colors = self.get_piece_colors(pieces)
        self.piece_status = self.get_piece_status(pieces)

    # -------- New method for score ----------
    def get_captured_counts(self):
        total_white = 12
        total_black = 12
        current_white = sum(1 for color in self.piece_colors if color == "W")
        current_black = sum(1 for color in self.piece_colors if color == "B")
        return (total_white - current_white, total_black - current_black)
    
    # -------- Helper method to check if any moves available ----------
    def has_moves_available(self, color):
        """Check if given color has any valid moves available"""
        pieces = self.board.get_pieces()
        for piece in pieces:
            if piece.get_color() == color:
                moves = piece.get_moves(self.board)
                if moves:
                    return True
        return False
    
    def has_valid_moves(self, player_color):
        """Check if player has any valid moves left"""
        for piece in self.board.get_pieces():
            if piece.get_color() == player_color:
                moves = piece.get_moves(self.board)
                if moves:
                    return True
        return False


       