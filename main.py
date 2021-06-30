import pygame
import random

def create_snake(snake_size, snake):
    for x in snake:
        pygame.draw.rect(game_display, ([0, 0, 0]), [x[0], x[1], snake_size, snake_size])


def direction_ind(direction_array, direction):
    # To prevent the snake run the opposite direction.
    if direction == left:
        direction_array[left] = 1
        direction_array[up] = 0
        direction_array[right] = 0
        direction_array[down] = 0
    elif direction == up:
        direction_array[left] = 0
        direction_array[up] = 1
        direction_array[right] = 0
        direction_array[down] = 0
    elif direction == right:
        direction_array[left] = 0
        direction_array[up] = 0
        direction_array[right] = 1
        direction_array[down] = 0

    elif direction == down:
        direction_array[left] = 0
        direction_array[up] = 0
        direction_array[right] = 0
        direction_array[down] = 1


def quit_game():
    pygame.quit()
    quit()


def play_game():
    # Game parameter
    direction_array = [0, 0, 0, 0]
    end_game = False
    close_game = False
    x_pos = win_width / 2
    y_pos = win_height / 2
    x_move = 0
    y_move = 0
    snake = []
    snake_length = 1
    food_posx = round(random.randrange(0, win_width-snake_size) / 10) * 10
    food_posy = round(random.randrange(0, win_height-snake_size) / 10) * 10
    #Prevent get score in init-stage
    while food_posx==x_pos:
        food_posx = round(random.randrange(0, win_width) / 10) * 10
    while food_posy==y_pos:
        food_posy= round(random.randrange(0, win_width) / 10) * 10

    while end_game==False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game=True
                quit_game()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction_array[right] != 1:
                    x_move = -snake_size
                    y_move = 0
                    direction_ind(direction_array, 0)
                elif event.key == pygame.K_UP and direction_array[down] != 1:
                    y_move = -snake_size
                    x_move = 0
                    direction_ind(direction_array, 1)
                elif event.key == pygame.K_RIGHT and direction_array[left] != 1:
                    x_move = snake_size
                    y_move = 0
                    direction_ind(direction_array, 2)
                elif event.key == pygame.K_DOWN and direction_array[up] != 1:
                    y_move = snake_size
                    x_move = 0
                    direction_ind(direction_array, 3)
        if x_pos >= win_width or x_pos < 0 or y_pos >= win_height or y_pos < 0:
            end_game = True
        x_pos += x_move
        y_pos += y_move

        game_display.fill([255, 255, 255])
        pygame.draw.rect(game_display, [255, 0, 0], [food_posx, food_posy, snake_size, snake_size])

        head = [x_pos,y_pos]
        snake.append(head)

        if len(snake) > snake_length:
            del snake[0]

        for x in snake[:-1]:
            if x == head:
                end_game = True
        create_snake(snake_size, snake)
        score=str((snake_length - 1) * 10)
        pygame.display.set_caption('My frist Python game' + "  Score: " + str(score))
        pygame.display.update()
        if x_pos == food_posx and y_pos == food_posy:
            food_posx = round(random.randrange(0, win_width - snake_size) / 10) * 10
            food_posy = round(random.randrange(0, win_height - snake_size) / 10) * 10
            snake_length += 1
        #The speed of snake
        clock.tick(15)

    while end_game ==True and close_game!=True:
        game_display.fill([0,0,0])
        pygame.display.set_caption("Please enter r for retry or enter q for quit | "+ "The final score is "+score)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    end_game=False
                    close_game=False
                    play_game()
                elif event.key == pygame.K_q:
                    quit_game()
            elif event.type == pygame.QUIT:
                quit_game()



# init Game
left = 0
up = 1
right = 2
down = 3
snake_size = 10
win_width = 500
win_height = 500
white = (255, 255, 255)
pygame.init()
game_display = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('My frist Python game')

clock = pygame.time.Clock()


play_game()
