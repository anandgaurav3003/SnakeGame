import pygame
import time
import random

pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Define display dimensions
display_width = 800
display_height = 600

# Initialize the display
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game by Gaurav')

# Set clock and snake block size
clock = pygame.time.Clock()
snake_block = 20  # Increased snake block size
initial_snake_speed = 15  # Initial speed of the snake

# Define fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Load sounds
try:
    eat_sound = pygame.mixer.Sound(r"c:\Users\Chhatrapal\HTML Tutorial\Downloads\snakehit.wav")
    game_over_sound = pygame.mixer.Sound(r"c:\Users\Chhatrapal\HTML Tutorial\Downloads\mixkit-arcade-retro-game-over-213.wav")
    print("Sound files loaded successfully.")
except pygame.error as e:
    print(f"Error loading sound files: {e}")
    eat_sound = None
    game_over_sound = None

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [display_width / 6, display_height / 3])

def draw_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    display.blit(value, [0, 0])

def gameLoop():
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, display_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, display_height - snake_block) / 20.0) * 20.0

    snake_speed = initial_snake_speed  # Initialize snake speed

    while not game_over:

        while game_close:
            display.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            if game_over_sound:
                pygame.mixer.Sound.play(game_over_sound)

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
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(blue)
        pygame.draw.rect(display, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        draw_score(Length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, display_height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1
            if eat_sound:
                print("Playing eat sound")
                pygame.mixer.Sound.play(eat_sound)
            snake_speed += 0.5

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
