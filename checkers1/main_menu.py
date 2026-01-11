import pygame as pg
from sys import exit
import checkers

# ------------------  COLOURS  ------------------
BLUE        = (30, 144, 255)
WHITE       = (255, 255, 255)
DARK_BLUE   = (0, 0, 139)
HOVER_BLUE  = (25, 25, 180)
RED         = (220, 20, 60)        # Exit-button base
HOVER_RED   = (255, 50, 50)        # Exit-button hover

# ------------------  HELPERS  ------------------
def draw_text(surface, text, size, x, y, color):
    font  = pg.font.SysFont("Arial", size, bold=True)
    label = font.render(text, True, color)
    rect  = label.get_rect(center=(x, y))
    surface.blit(label, rect)

def draw_button(surface, rect, text, font_size, base_color, hover_color, mouse_pos):
    color = hover_color if rect.collidepoint(mouse_pos) else base_color
    pg.draw.rect(surface, color, rect, border_radius=10)
    draw_text(surface, text, font_size, rect.centerx, rect.centery, WHITE)
    return rect

# ------------------  MENU  ------------------
def menu():
    pg.init()
    screen = pg.display.set_mode((700, 500))
    pg.display.set_caption("Checkers Menu")
    clock  = pg.time.Clock()

   # --- buttons ---
    two_player_btn = pg.Rect(250, 250, 200, 50)   # old size
    vs_ai_btn      = pg.Rect(250, 330, 200, 50)   # old size
    exit_btn       = pg.Rect(270, 410, 160, 40)   # ONLY this one smaller

    while True:
        screen.fill(BLUE)
        mouse_pos = pg.mouse.get_pos()

        # title
        draw_text(screen, "MASTER CHECKERS", 48, 350, 120, WHITE)
        draw_text(screen, "MULTIPLAYER", 28, 350, 170, DARK_BLUE)

        # draw buttons
        draw_button(screen, two_player_btn, "TWO PLAYER",   28, DARK_BLUE, HOVER_BLUE, mouse_pos)
        draw_button(screen, vs_ai_btn,      "VS COMPUTER",  28, DARK_BLUE, HOVER_BLUE, mouse_pos)
        draw_button(screen, exit_btn,       "EXIT",         28, RED,       HOVER_RED,  mouse_pos)  # NEW

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if two_player_btn.collidepoint(event.pos):
                    checkers.main(mode="2P")
                elif vs_ai_btn.collidepoint(event.pos):
                    checkers.main(mode="AI")
                elif exit_btn.collidepoint(event.pos):      # NEW
                    pg.quit()
                    exit()

        pg.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    menu()