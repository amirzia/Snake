"""
Snake Eater
Made with PyGame
"""

import pygame, sys, time, random, requests, json
import controller

controller.start_controller()

size = 480
# Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120
difficulty = 25

# Window size
frame_size_x = 480
frame_size_y = 480

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


# FPS (frames per second) controller
fps_controller = pygame.time.Clock()


score = 0
game_board = []


# Main logic
while True:

    res = requests.get("http://localhost:5000/get_board")
    #print("res get")
    res = json.loads(res.text)
    game_board = res["borad"]
    # print(len(game_board))
    # print(game_board)
    game_window.fill(black)
    # print("blacked out")
    for i in range(0, 48):
        for j in range(0, 48):
            # print(game_board[i][j])
            if game_board[i][j] == 9:
                # print("here is the food: ", i, j)
                pygame.draw.rect(game_window, white, (i * 10, j * 10, 10, 10))
            elif game_board[i][j] == 1:
                print("here is the snake: ", i, j)
                pygame.draw.rect(game_window, green, (i * 10, j * 10, 10, 10))
    pygame.display.update()
    fps_controller.tick(difficulty)
    time.sleep(1)

