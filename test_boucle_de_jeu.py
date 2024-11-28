from menu import *
from header import *

while running:
    # Poll for events
    events = pygame.event.get()  # Get all events
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Call afficher_menu and check for the quit flag
    quit_flag = afficher_menu(events)

    if quit_flag == 10:
        running = False

    # Update the display
    pygame.display.flip()

    clock.tick(60)  # Limit FPS to 60

pygame.quit()

