"""

Made by Beaumont Spinks
Hosted on Github on BasicSyntax

Made 15 June 2020
Using Python and PyGame

"""

import pygame
import random
import sys

pygame.init()

pygame.display.set_caption("TicTacToe with Machine Learning by BSpinks")
clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsans', 20, True)
h1_font = pygame.font.SysFont('comicsans', 40, True)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

YLW = (234, 255, 123)
BBY_GRN = (0, 255, 171)
TEAL = (41, 189, 193)
GNTL_RED = (216, 66, 66)
PURPLE = (145, 63, 146)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

colour = WHITE
click_loop = 0
click = False
game_state = False
turn = 0
run = False
winner = 0
blank_board = [' ' for _ in range(10)]
b = blank_board[:]
screenWidth = 900
screenHeight = 900
win = pygame.display.set_mode((screenWidth, screenHeight))


class Tiles(object):
    x = pygame.image.load('images/x_orange.png')
    o = pygame.image.load('images/o_blue.png')
    grid = pygame.image.load('images/bg_box.png')

    def __init__(self, rect, clicked=False):
        self.rect = rect
        self.clicked = clicked

    def draw_grid(self):
        win.blit(self.grid, self.rect)

    def draw(self, move):
        if self.clicked is False:
            if move == 'X':
                win.blit(self.x, self.rect)
            elif move == 'O':
                win.blit(self.o, self.rect)
            else:
                print('wrong move passed to tile !')
            self.clicked = True
        else:
            print('tile is already clicked')


def draw_text(t, f, c, s, x, y):
    text_obj = f.render(t, 1, c)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    s.blit(text_obj, text_rect)


def play_move(move):
    c = b[:]
    if 360 >= pygame.mouse.get_pos()[0]:
        if 360 >= pygame.mouse.get_pos()[1]:
            if not T1.clicked:
                T1.draw(move)
                b[1] = move
        elif 540 >= pygame.mouse.get_pos()[1] >= 360:
            if not T2.clicked:
                T2.draw(move)
                b[2] = move
        else:
            if not T3.clicked:
                T3.draw(move)
                b[3] = move
    elif 540 >= pygame.mouse.get_pos()[0] >= 360:
        if 360 >= pygame.mouse.get_pos()[1]:
            if not T4.clicked:
                T4.draw(move)
                b[4] = move
        elif 540 >= pygame.mouse.get_pos()[1] >= 360:
            if not T5.clicked:
                T5.draw(move)
                b[5] = move
        else:
            if not T6.clicked:
                T6.draw(move)
                b[6] = move
    else:
        if 360 >= pygame.mouse.get_pos()[1]:
            if not T7.clicked:
                T7.draw(move)
                b[7] = move
        elif 540 >= pygame.mouse.get_pos()[1] >= 360:
            if not T8.clicked:
                T8.draw(move)
                b[8] = move
        else:
            if not T9.clicked:
                T9.draw(move)
                b[9] = move

    if c == b:
        return False
    else:
        return True


def comp_move():
    possible_moves = [x for x, letter in enumerate(b) if letter == ' ' and x != 0]
    move = 0
    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = b[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                if move == 1:
                    if not T1.clicked:
                        T1.draw('O')
                elif move == 3:
                    if not T3.clicked:
                        T3.draw('O')
                elif move == 7:
                    if not T7.clicked:
                        T7.draw('O')
                elif move == 9:
                    if not T9.clicked:
                        T9.draw('O')
                elif move == 2:
                    if not T2.clicked:
                        T2.draw('O')
                elif move == 4:
                    if not T4.clicked:
                        T4.draw('O')
                elif move == 6:
                    if not T6.clicked:
                        T6.draw('O')
                else:
                    if not T8.clicked:
                        T8.draw('O')
                return move

    if 5 in possible_moves:
        move = 5
        T5.draw('O')
        return move

    corners_open = []

    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)

    if len(corners_open) >= 1:
        move = corners_open[random.randrange(0, (len(corners_open)))]
        if move == 1:
            T1.draw('O')
        elif move == 3:
            T3.draw('O')
        elif move == 7:
            T7.draw('O')
        else:
            T9.draw('O')
        return move

    edges_open = []

    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)

    if len(edges_open) >= 1:
        move = corners_open[random.randrange(0, (len(corners_open)))]

    if move == 2:
        T2.draw('O')
    elif move == 4:
        T4.draw('O')
    elif move == 6:
        T6.draw('O')
    else:
        T8.draw('O')
    return move


def is_winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or
            (bo[3] == le and bo[5] == le and bo[7] == le))


def game_over():
    global game_state

    game_state = False
    T1.clicked = True
    T2.clicked = True
    T3.clicked = True
    T4.clicked = True
    T5.clicked = True
    T6.clicked = True
    T7.clicked = True
    T8.clicked = True
    T9.clicked = True


def game_restart():
    global click
    global click_loop
    global b
    global game_state
    global turn
    global run
    global winner

    win.fill(colour)
    game_state = True
    click = False
    click_loop = 0
    run = True
    turn = 1
    winner = 0
    b = blank_board[:]

    T1.clicked = False
    T2.clicked = False
    T3.clicked = False
    T4.clicked = False
    T5.clicked = False
    T6.clicked = False
    T7.clicked = False
    T8.clicked = False
    T9.clicked = False


T1 = Tiles((180, 180))
T2 = Tiles((180, 360))
T3 = Tiles((180, 540))
T4 = Tiles((360, 180))
T5 = Tiles((360, 360))
T6 = Tiles((360, 540))
T7 = Tiles((540, 180))
T8 = Tiles((540, 360))
T9 = Tiles((540, 540))


def main_menu():
    global click
    global colour

    btn_1 = pygame.Rect(100, 150, 100, 40)
    btn_2 = pygame.Rect(250, 150, 100, 40)
    btn_3 = pygame.Rect(400, 150, 100, 40)

    def draw():
        win.fill(colour)

        pygame.draw.rect(win, (0, 255, 0), btn_1)
        pygame.draw.rect(win, (255, 255, 0), btn_2)
        pygame.draw.rect(win, (255, 0, 255), btn_3)

        if colour == BLACK:
            draw_text('Main Menu', h1_font, WHITE, win, 20, 20)
            draw_text('Bckspc to go back', font, WHITE, win, 20, 360)
            draw_text('Esc to quit', font, WHITE, win, 20, 540)
        else:
            draw_text('Main Menu', h1_font, BLACK, win, 20, 20)
            draw_text('Bckspc to go back', font, BLACK, win, 20, 360)
            draw_text('Esc to quit', font, BLACK, win, 20, 540)

        draw_text('2 player', font, BLACK, win, 100, 150)
        draw_text('vs computer', font, BLACK, win, 250, 150)
        draw_text('options menu', font, BLACK, win, 400, 150)

    while True:
        mmx, mmy = pygame.mouse.get_pos()

        if btn_1.collidepoint(mmx, mmy):
            if click:
                game_vs_player()
        if btn_2.collidepoint(mmx, mmy):
            if click:
                game_vs_comp()
        if btn_3.collidepoint(mmx, mmy):
            if click:
                options()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        draw()
        pygame.display.update()
        clock.tick(30)


def game_vs_player():
    global click_loop
    global colour
    global b
    global click
    global game_state
    global winner
    global turn
    global run

    board_space = pygame.Rect(180, 180, 540, 540)
    reset_button = pygame.Rect(780, 100, 100, 40)

    game_restart()

    def draw(text):
        pygame.draw.rect(win, (0, 255, 0), reset_button)

        if colour == BLACK:
            grid = pygame.image.load('images/grid_640+360_white.png')
            draw_text(text, h1_font, WHITE, win, 20, 20)
            draw_text('Reset Game', font, WHITE, win, 780, 100)
            draw_text('Bckspc to go back', font, WHITE, win, 20, 360)
            draw_text('Esc to quit', font, WHITE, win, 20, 540)
        else:
            grid = pygame.image.load('images/grid_640+360.png')
            draw_text(text, h1_font, BLACK, win, 20, 20)
            draw_text('Reset Game', font, BLACK, win, 780, 100)
            draw_text('Bckspc to go back', font, BLACK, win, 20, 360)
            draw_text('Esc to quit', font, BLACK, win, 20, 540)

        if not game_state:
            if winner == 0:
                if colour == BLACK:
                    draw_text('Game Over : Tie Game', h1_font, WHITE, win, 200, 100)
                else:
                    draw_text('Game Over : Tie Game', h1_font, BLACK, win, 200, 100)
            elif winner == 1:
                draw_text('Player One Wins !', h1_font, BLUE, win, 200, 100)
            elif winner == 2:
                draw_text('Player Two Wins !', h1_font, BLUE, win, 200, 100)
        # elif game_state:
        #     draw_text('Running: Player ' + str(turn) + '\'s turn !', h1_font, BLUE, win, 200, 100)

        win.blit(grid, (0, 0))

    while run:
        cgx, cgy = pygame.mouse.get_pos()

        if reset_button.collidepoint(cgx, cgy):
            if click:
                game_restart()

        if board_space.collidepoint(cgx, cgy) and click_loop == 0:
            if click:
                move = 'O'

                if turn == 1:
                    move = 'X'
                    turn = 2
                elif turn == 2:
                    move = 'O'
                    turn = 1

                allow_move = play_move(move)

                if allow_move:
                    if b.count(' ') > 1:
                        if is_winner(b, 'O'):
                            print('Sorry, O\'s won this time!')
                            game_over()
                            winner = 2
                        elif is_winner(b, 'X'):
                            print('X\'s won this time! Good Job!')
                            game_over()
                            winner = 1
                    else:
                        print('Tie Game!')
                        game_over()
                        winner = 0
                click_loop = 1

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_BACKSPACE:
                    run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        draw('2 Player Mode')
        pygame.display.update()
        clock.tick(30)

        if click_loop >= 1:
            click_loop += 1
        if click_loop > 8:
            click_loop = 0


def game_vs_comp():
    global click_loop
    global colour
    global b
    global click
    global game_state
    global winner
    global turn
    global run

    board_space = pygame.Rect(180, 180, 540, 540)
    reset_button = pygame.Rect(780, 100, 100, 40)

    game_restart()

    def draw(text):
        pygame.draw.rect(win, (0, 255, 0), reset_button)

        if colour == BLACK:
            grid = pygame.image.load('images/grid_640+360_white.png')
            draw_text(text, h1_font, WHITE, win, 20, 20)
            draw_text('Reset Game', font, WHITE, win, 780, 100)
            draw_text('Bckspc to go back', font, WHITE, win, 20, 360)
            draw_text('Esc to quit', font, WHITE, win, 20, 540)
        else:
            grid = pygame.image.load('images/grid_640+360.png')
            draw_text(text, h1_font, BLACK, win, 20, 20)
            draw_text('Reset Game', font, BLACK, win, 780, 100)
            draw_text('Bckspc to go back', font, BLACK, win, 20, 360)
            draw_text('Esc to quit', font, BLACK, win, 20, 540)

        if not game_state:
            if winner == 0:
                if colour == BLACK:
                    draw_text('Game Over : Tie Game', h1_font, WHITE, win, 200, 100)
                else:
                    draw_text('Game Over : Tie Game', h1_font, BLACK, win, 200, 100)
            elif winner == 1:
                draw_text('You are the winner !', h1_font, BLUE, win, 200, 100)
            elif winner == 2:
                draw_text('Game Over : You Lose', h1_font, RED, win, 200, 100)
        # elif game_state:
        #     draw_text('Game Running', h1_font, BLUE, win, 200, 100)

        win.blit(grid, (0, 0))

    while run:
        cgx, cgy = pygame.mouse.get_pos()

        if reset_button.collidepoint(cgx, cgy):
            if click:
                game_restart()

        if board_space.collidepoint(cgx, cgy) and click_loop == 0:
            if click:
                allow_move = play_move('X')
                if allow_move:
                    if b.count(' ') > 1:
                        m = comp_move()
                        b[m] = 'O'
                        if is_winner(b, 'O'):
                            print('Sorry, O\'s won this time!')
                            game_over()
                            winner = 2
                        elif is_winner(b, 'X'):
                            print('X\'s won this time! Good Job!')
                            game_over()
                            winner = 1
                    else:
                        print('Tie Game!')
                        game_over()
                        winner = 0
                click_loop = 1

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_BACKSPACE:
                    run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        draw('Comp Game')
        pygame.display.update()
        clock.tick(30)

        if click_loop >= 1:
            click_loop += 1
        if click_loop > 8:
            click_loop = 0


def options():
    global click
    global colour
    global run

    run = True
    click = False

    bt_1 = pygame.Rect(100, 300, 100, 40)
    bt_2 = pygame.Rect(250, 300, 100, 40)
    bt_3 = pygame.Rect(400, 300, 100, 40)
    bt_4 = pygame.Rect(550, 300, 100, 40)
    bt_5 = pygame.Rect(700, 300, 100, 40)
    bt_6 = pygame.Rect(100, 450, 100, 40)
    bt_7 = pygame.Rect(250, 450, 100, 40)
    bt_8 = pygame.Rect(400, 450, 100, 40)
    bt_9 = pygame.Rect(550, 450, 100, 40)
    bt_10 = pygame.Rect(700, 450, 100, 40)

    def draw():
        win.fill(colour)

        if colour == BLACK:
            draw_text('Options Menu', font, WHITE, win, 20, 20)
            draw_text('Pick your background colour!', font, WHITE, win, 80, 80)
            draw_text('Bckspc to go back', font, WHITE, win, 20, 360)
            draw_text('Esc to quit', font, WHITE, win, 20, 540)
        else:
            draw_text('Options Menu', font, BLACK, win, 20, 20)
            draw_text('Pick your background colour!', font, BLACK, win, 80, 80)
            draw_text('Bckspc to go back', font, BLACK, win, 20, 360)
            draw_text('Esc to quit', font, BLACK, win, 20, 540)

        pygame.draw.rect(win, BLACK, bt_1)
        pygame.draw.rect(win, WHITE, bt_2)
        pygame.draw.rect(win, YLW, bt_3)
        pygame.draw.rect(win, BBY_GRN, bt_4)
        pygame.draw.rect(win, TEAL, bt_5)
        pygame.draw.rect(win, GNTL_RED, bt_6)
        pygame.draw.rect(win, PURPLE, bt_7)
        pygame.draw.rect(win, RED, bt_8)
        pygame.draw.rect(win, GREEN, bt_9)
        pygame.draw.rect(win, BLUE, bt_10)

    while run:
        omx, omy = pygame.mouse.get_pos()

        if bt_1.collidepoint(omx, omy):
            if click:
                colour = BLACK
                draw()
        if bt_2.collidepoint(omx, omy):
            if click:
                colour = WHITE
                draw()
        if bt_3.collidepoint(omx, omy):
            if click:
                colour = YLW
                draw()
        if bt_4.collidepoint(omx, omy):
            if click:
                colour = BBY_GRN
                draw()
        if bt_5.collidepoint(omx, omy):
            if click:
                colour = TEAL
                draw()
        if bt_6.collidepoint(omx, omy):
            if click:
                colour = GNTL_RED
                draw()
        if bt_7.collidepoint(omx, omy):
            if click:
                colour = PURPLE
                draw()
        if bt_8.collidepoint(omx, omy):
            if click:
                colour = RED
                draw()
        if bt_9.collidepoint(omx, omy):
            if click:
                colour = GREEN
                draw()
        if bt_10.collidepoint(omx, omy):
            if click:
                colour = BLUE
                draw()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_BACKSPACE:
                    run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        draw()
        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    main_menu()
