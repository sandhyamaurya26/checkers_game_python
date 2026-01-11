import pygame as pg
from sys import exit
from pygame.locals import *
from board_gui import BoardGUI
import main_menu
import ai

def draw_button(surface, rect, text, font, base_color, hover_color, mouse_pos):
    color = base_color
    if rect.collidepoint(mouse_pos):
        color = hover_color
    pg.draw.rect(surface, color, rect, border_radius=8)
    text_surf = font.render(text, True, (255, 255, 255))
    text_rect = text_surf.get_rect(center=rect.center)
    surface.blit(text_surf, text_rect)
    return rect

def main(mode="AI"):
    pg.init()
    FPS = 30
    
    BOARD_WIDTH = 500
    BOARD_HEIGHT = 500
    SIDEBAR_WIDTH = 200
    WINDOW_SIZE = (BOARD_WIDTH + SIDEBAR_WIDTH, BOARD_HEIGHT)
    
    DISPLAYSURF = pg.display.set_mode(WINDOW_SIZE)
    pg.display.set_caption('Checkers in Python')
    fps_clock = pg.time.Clock()
    
    board_gui = BoardGUI((26, 26))
    
    font = pg.font.SysFont("Arial", 24, bold=True)
    
    # Sidebar Buttons
    restart_btn = pg.Rect(BOARD_WIDTH + 20, 180, 160, 40)
    back_btn = pg.Rect(BOARD_WIDTH + 20, 240, 160, 40)
    
    TOTAL_PIECES = 12
    winner = None
    
    current_player = "W"
    ai_move_delay = 0
    AI_MOVE_DELAY = 30

    running = True
    while running:
        DISPLAYSURF.fill((0, 0, 0))
        mouse_pos = pg.mouse.get_pos()

        board_gui.draw_gui(DISPLAYSURF)

        # Sidebar
        pg.draw.rect(DISPLAYSURF, (10, 40, 80), (BOARD_WIDTH, 0, SIDEBAR_WIDTH, BOARD_HEIGHT))
        mode_text = font.render(f"Mode: {mode}", True, (255, 255, 255))
        DISPLAYSURF.blit(mode_text, (BOARD_WIDTH + 20, 20))

        if not winner:
            if mode == "AI":
                turn_text = "Human Turn" if current_player == "W" else "AI Turn"
                turn_color = (0, 255, 0) if current_player == "W" else (255, 100, 100)
            else:  # Two Player mode
                turn_text = "Player 1 Turn" if current_player == "W" else "Player 2 Turn"
                turn_color = (0, 255, 0) if current_player == "W" else (255, 100, 100)
            DISPLAYSURF.blit(font.render(turn_text, True, turn_color), (BOARD_WIDTH + 20, 50))

        # Score
        DISPLAYSURF.blit(font.render("Score:", True, (255, 255, 255)), (BOARD_WIDTH + 20, 90))
        white_captured, black_captured = board_gui.get_captured_counts()
        white_score_val = black_captured
        black_score_val = white_captured
        
        if mode == "AI":
            DISPLAYSURF.blit(font.render("Human:", True, (255, 255, 255)), (BOARD_WIDTH+20,120))
            DISPLAYSURF.blit(font.render(str(white_score_val), True, (255, 255, 255)), (BOARD_WIDTH+100,120))
            DISPLAYSURF.blit(font.render("AI:", True, (255, 255, 255)), (BOARD_WIDTH+20,150))
            DISPLAYSURF.blit(font.render(str(black_score_val), True, (255, 255, 255)), (BOARD_WIDTH+100,150))
        else:  # Two Player mode
            DISPLAYSURF.blit(font.render("Player 1:", True, (255, 255, 255)), (BOARD_WIDTH+20,120))
            DISPLAYSURF.blit(font.render(str(white_score_val), True, (255, 255, 255)), (BOARD_WIDTH+100,120))
            DISPLAYSURF.blit(font.render("Player 2:", True, (255, 255, 255)), (BOARD_WIDTH+20,150))
            DISPLAYSURF.blit(font.render(str(black_score_val), True, (255, 255, 255)), (BOARD_WIDTH+100,150))

        # Winner check
        if not winner:
            if white_captured >= TOTAL_PIECES:
                winner = "Player 2" if mode == "2P" else "AI"
            elif black_captured >= TOTAL_PIECES:
                winner = "Player 1" if mode == "2P" else "Human"
            else:
                if not board_gui.has_valid_moves("W"):
                    winner = "Player 2" if mode == "2P" else "AI"
                elif not board_gui.has_valid_moves("B"):
                    winner = "Player 1" if mode == "2P" else "Human"

        # Draw sidebar buttons
        draw_button(DISPLAYSURF, restart_btn, "Restart", font, (70,130,180), (100,160,220), mouse_pos)
        draw_button(DISPLAYSURF, back_btn, "Back", font, (180,50,50), (220,80,80), mouse_pos)

        # Game Over overlay
        if winner:
            pg.draw.rect(DISPLAYSURF, (51,153,255), (0,0,WINDOW_SIZE[0],WINDOW_SIZE[1]))
            big_font = pg.font.SysFont("Arial",48,bold=True)
            small_font = pg.font.SysFont("Arial",28,bold=True)
            win_text = big_font.render(f"{winner} Wins!", True, (0,0,139))
            DISPLAYSURF.blit(win_text, win_text.get_rect(center=(WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2-80)))
            over_text = small_font.render("Game Over", True, (255,255,255))
            DISPLAYSURF.blit(over_text, over_text.get_rect(center=(WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2-30)))

            # Game Over buttons
            button_width, button_height = 150, 60
            spacing = 40
            total_width = button_width*2 + spacing
            start_x = WINDOW_SIZE[0]//2 - total_width//2
            y_pos = WINDOW_SIZE[1]//2 + 50
            restart_btn_rect = pg.Rect(start_x, y_pos, button_width, button_height)
            exit_btn_rect = pg.Rect(start_x + button_width + spacing, y_pos, button_width, button_height)

            draw_button(DISPLAYSURF, restart_btn_rect, "Restart", small_font, (0,0,139), (0,0,180), mouse_pos)
            draw_button(DISPLAYSURF, exit_btn_rect, "Exit", small_font, (200,0,0), (255,50,50), mouse_pos)

        # AI move
        if mode=="AI" and current_player=="B" and not winner:
            if ai_move_delay<=0:
                if ai.ai_move(board_gui.board):
                    board_gui.update_board()
                    current_player="W"
                    ai_move_delay=AI_MOVE_DELAY
                else:
                    winner="Human"
            else:
                ai_move_delay -=1

        # Events
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if not winner:
                    if restart_btn.collidepoint(event.pos):
                        main(mode)
                        return
                    if back_btn.collidepoint(event.pos):
                        main_menu.menu()
                        return
                    
                    # MAIN FIX: Proper player turn checking
                    if mode=="AI" and current_player=="W":
                        board_gui.hold_piece_with_mouse(event.pos, "W")  # Only white pieces for human
                    elif mode=="2P":
                        # Two player mode - restrict pieces based on current player
                        board_gui.hold_piece_with_mouse(event.pos, current_player)
                        
                else:
                    if restart_btn_rect.collidepoint(event.pos):
                        main(mode)
                        return
                    if exit_btn_rect.collidepoint(event.pos):
                        pg.quit()
                        exit()
                        
            if event.type == MOUSEBUTTONUP and not winner:
                if mode=="AI" and current_player=="W":
                    move_made = board_gui.release_piece()
                    if move_made:
                        current_player="B"
                        ai_move_delay=AI_MOVE_DELAY
                elif mode=="AI" and current_player=="B":
                    # AI ki turn hai - human ko release nahi karne dena
                    pass  # Do nothing during AI turn
                elif mode=="2P":
                    move_made = board_gui.release_piece()
                    if move_made:
                        current_player = "B" if current_player=="W" else "W"

        pg.display.update()
        fps_clock.tick(FPS)

if __name__=="__main__":
    main()