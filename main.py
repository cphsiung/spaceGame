import pygame

FPS = 60
WHITE = (255,255,255)
WIDTH = 500
HEIGHT = 600
# Initiate pygame and set window sizes
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
clock = pygame.time.Clock()

while running:
    
    clock.tick(FPS) # Max update FPS times in one sec
    # Get user input
    # Quit game when user click close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game

    # Display game
    screen.fill(WHITE)
    pygame.display.update()
    
pygame.quit()