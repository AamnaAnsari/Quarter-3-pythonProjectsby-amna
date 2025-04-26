import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Colors
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
black = (0, 0, 0)

# Window size
window_width = 600
window_height = 400

# Create game window
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('🐍 Snake Game')

# Snake settings
snake_size = 15
snake_speed = 15

clock = pygame.time.Clock()

# Font
font_style = pygame.font.SysFont(None, 35)

# Functions
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [window_width / 6, window_height / 3])

def our_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, black, [x[0], x[1], snake_size, snake_size])

def gameLoop():
    game_over = False
    game_close = False

    x1 = window_width / 2
    y1 = window_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Food
    foodx = round(random.randrange(0, window_width - snake_size) / 15.0) * 15.0
    foody = round(random.randrange(0, window_height - snake_size) / 15.0) * 15.0

    while not game_over:

        while game_close:
            game_window.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0

        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        game_window.fill(white)
        pygame.draw.rect(game_window, green, [foodx, foody, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # snake collides
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_size, snake_list)
        pygame.display.update()

        # snake eats the foods 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_size) / 15.0) * 15.0
            foody = round(random.randrange(0, window_height - snake_size) / 15.0) * 15.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

# Start the game
gameLoop()
