"""
Snake Eater
Made with PyGame
"""

import pygame, sys, time, random, requests, json
import controller

controller.start_controller()

size = 320
# Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120
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


score = 0
game_board = []

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x/10, 15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)


# Main logic
while True:

    res = requests.get("http://localhost:5000/get_board")
    res = json.loads(res.text)
    game_board = res["board"]
    user_lost = res["lost"]
    if user_lost == True:
        print("end game")
    game_window.fill(black)
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
            elif game_board[i][j] == 3:
                pygame.draw.rect(game_window, blue, (i * 10, j * 10, 10, 10))
            elif game_board[i][j] == 8:
                pygame.draw.rect(game_window, yellow, (i * 10, j * 10, 10, 10))
    show_score()
    pygame.display.update()
    fps_controller.tick(difficulty)
    time.sleep(1)
