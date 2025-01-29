import pygame
import random

pygame.init()

# Display settings
WIDTH, HEIGHT = 600, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load the background image  
background_image = pygame.image.load("background.png")  # Provide the correct image file path
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Load the bird image
bird_image = pygame.image.load("bird.png")  # Provide the correct image file path
bird_image = pygame.transform.scale(bird_image, (40, 40))

# Colors
WHITE = (255, 255, 255)
BLACK = (255, 0, 0)

# Bird settings
bird_x = 50
bird_y = HEIGHT // 2
bird_speed = 0  # Initial speed
bird_gravity = 1
bird_jump = -10

# Pipe settings
pipe_width = 50
pipe_gap = 200 
pipe_speed = 3
pipes = []

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bird_speed = bird_jump

    bird_speed += bird_gravity
    bird_y += bird_speed

    # Update pipes
    for pipe in pipes:
        pipe[0] -= pipe_speed
        if pipe[0] + pipe_width < 0:
            pipes.remove(pipe)

    # Create new pipe
    if len(pipes) == 0 or pipes[-1][0] < WIDTH - 200:
        pipe_height = random.randint(pipe_gap, HEIGHT - pipe_gap)
        pipes.append([WIDTH, pipe_height])

    # Check collision with pipes
    for pipe in pipes:
        if (bird_x + bird_image.get_width() > pipe[0] and
            bird_x < pipe[0] + pipe_width and
            (bird_y < pipe[1] or bird_y + bird_image.get_height() > pipe[1] + pipe_gap)):
            running = False

    # Update bird position
    #bird_y = max(bird_y, 0)
    #bird_y = min(bird_y, HEIGHT - bird_image.get_height())

    # Draw the background image
    win.blit(background_image, (0, 0))

    # Draw the bird image
    win.blit(bird_image, (bird_x, bird_y))

    # Draw pipes
    for pipe in pipes:
        pygame.draw.rect(win, BLACK, (pipe[0], 0, pipe_width, pipe[1]))
        pygame.draw.rect(win, BLACK, (pipe[0], pipe[1] + pipe_gap, pipe_width, HEIGHT))

    pygame.display.update()
    clock.tick(30)

pygame.quit()