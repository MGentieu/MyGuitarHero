from menu import *
from header import *
from selection_musique import *
from aide import *
from jouer import *

current_menu = "main_menu"

while running:
    # Poll for events
    events = pygame.event.get()  # Get all events
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if current_menu == "main_menu":
        # Call afficher_menu and check for the quit or play flag
        menu_flag = afficher_menu(events)

        if menu_flag == 10:  # Quit signal
            running = False

        elif menu_flag == 20:  # Launch music selection menu
            current_menu = "music_selection"  # Switch to music selection menu

        elif menu_flag == 30:
            current_menu = "aide" 

    elif current_menu == "music_selection":
        menu_musique_flag=menu_selection_musique(events)

        if menu_musique_flag == 10:  # Quit signal
            current_menu="main_menu"

        elif menu_musique_flag in [1, 2, 3]:  # Lancer une musique spécifique
            current_menu = "jeu"  # Change l'état pour lancer le jeu

        # Call the music selection menu
        
    elif current_menu == "aide":
        aide_flag = afficher_aide(events)

        if aide_flag == 10:  # Retour au menu principal
            current_menu = "main_menu"
    
    elif current_menu == "jeu":
        jouer_flag=jouer(events,menu_musique_flag)
        if jouer_flag == 10:  # Retour au menu selection
            current_menu = "music_selection"
    # Update the display
    pygame.display.flip()

    clock.tick(60)  # Limit FPS to 60

pygame.quit()

