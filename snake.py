"""
Snake Eater
Made with PyGame
"""

import pygame, sys, time, random, requests, json
import controller

controller.start_controller()

size = 320
difficulty = 25

# Window size
frame_size_x = 320
frame_size_y = 320

# Checks for errors encountered
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    #print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')


# Initialise game window
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)

# FPS (frames per second) controller
fps_controller = pygame.time.Clock()
def game_over(me):
    if me:
        message = "Game Over!"
        color = red
    else:
        message = "Win!"
        color = green

    my_font = pygame.font.SysFont('times new roman', 40)
    game_over_surface = my_font.render('Game Over!', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, color, 'times', 20)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()
    sys.exit()


# Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score: Player 1: ' + str(scores[0]) + ', Player 2: ' + str(scores[1]), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x/10, 15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)

scores = [0, 0, 0]
game_board = []


# Main logic
while True:

    res = requests.get("http://5.253.27.186:5000/get_board")
    #print("res get")
    res = json.loads(res.text)
    game_board = res["board"]
    user_lost = res["lost"]
    scores = res["scores"]
    if user_lost == "1":
        print("end game")
        game_over(True)
    elif user_lost == "2":
        print("win game")
        game_over(False)
    # print(len(game_board))
    # print(game_board)
    game_window.fill(black)
    # print("blacked out")
    for i in range(0, 32):
        for j in range(0, 32):
            # print(game_board[i][j])
            if game_board[i][j] == 9:
                # print("here is the food: ", i, j)
                pygame.draw.rect(game_window, white, (i * 10, j * 10, 10, 10))
            elif game_board[i][j] == 1:
                # print("here is the snake: ", i, j)
                pygame.draw.rect(game_window, green, (i * 10, j * 10, 10, 10))
            elif game_board[i][j] == 2:
                # print("here is the snake: ", i, j)
                pygame.draw.rect(game_window, red, (i * 10, j * 10, 10, 10))
            elif game_board[i][j] == 8:
                pygame.draw.rect(game_window, yello, (i * 10, j * 10, 10, 10))
            elif game_board[i][j] == 8:
                pygame.draw.rect(game_window, yello, (i * 10, j * 10, 10, 10))
    pygame.display.update()
    fps_controller.tick(difficulty)
    time.sleep(0.4)


