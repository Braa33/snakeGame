import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Set up the snake
snake = [(100, 100), (90, 100), (80, 100)]
snake_color = (255, 255, 255)
snake_direction = "right"

# Set up the food
food_pos = (random.randint(0, screen_width//10)*10, random.randint(0, screen_height//10)*10)
food_color = (255, 0, 0)

# Set up the score counter
score = 0
font = pygame.font.Font(None, 30)

# Set up the game loop
while True:
    # Handle user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "down":
                snake_direction = "up"
            elif event.key == pygame.K_DOWN and snake_direction != "up":
                snake_direction = "down"
            elif event.key == pygame.K_LEFT and snake_direction != "right":
                snake_direction = "left"
            elif event.key == pygame.K_RIGHT and snake_direction != "left":
                snake_direction = "right"

    # Move the snake
    if snake_direction == "up":
        new_head = (snake[0][0], snake[0][1] - 10)
    elif snake_direction == "down":
        new_head = (snake[0][0], snake[0][1] + 10)
    elif snake_direction == "left":
        new_head = (snake[0][0] - 10, snake[0][1])
    elif snake_direction == "right":
        new_head = (snake[0][0] + 10, snake[0][1])

    snake.insert(0, new_head)
    snake.pop()

    # Check for collision with the game boundaries or the snake's body
    if snake[0][0] < 0 or snake[0][0] >= screen_width or snake[0][1] < 0 or snake[0][1] >= screen_height:
        pygame.quit()
        sys.exit()

    for pos in snake[1:]:
        if snake[0][0] == pos[0] and snake[0][1] == pos[1]:
            pygame.quit()
            sys.exit()

    # Check for collision with the food
    if snake[0][0] == food_pos[0] and snake[0][1] == food_pos[1]:
        snake.append(snake[-1])
        food_pos = (random.randint(0, screen_width//10)*10, random.randint(0, screen_height//10)*10)
        score += 1

    # Draw the game screen
    screen.fill((0, 0, 0))
    for pos in snake:
        pygame.draw.rect(screen, snake_color, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, food_color, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

    pygame.time.delay(100)
