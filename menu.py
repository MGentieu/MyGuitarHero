
from header import *

from selection_musique import *


def afficher_menu(events):
    # Declaration des variables
    menu_options = ["Commencer le jeu", "Options", "Instructions", "Quitter"]

    menu_rects = []

    background_image_menu = pygame.image.load("image/Fond_Menu_2.jpg")  # Remplacez par le chemin de votre image

    background_image_menu = pygame.transform.scale(background_image_menu, (screen_width, screen_height))  # Redimensionne si nécessaire

    screen.blit(background_image_menu, (0, 0))

    font = pygame.font.Font(None, 36)



    button_images = {
        "Commencer le jeu": pygame.image.load("image/bouton_play_menu.png"),
        "Options": pygame.image.load("image/bouton_option_menu.png"),
        "Instructions": pygame.image.load("image/bouton_quit_menu.png"),
        "Quitter": pygame.image.load("image/bouton_quit_menu.png"),
    }
    button_hover_images = {
        "Commencer le jeu": pygame.image.load("image/bouton_play_menu.png"),
        "Options": pygame.image.load("image/bouton_option_menu.png"),
        "Instructions": pygame.image.load("image/bouton_quit_menu.png"),
        "Quitter": pygame.image.load("image/bouton_quit_menu.png"),
    }
    rect_width, rect_height = 350, 150
    
    # Taille et espacement des rectangles
    rect_x = screen_width/2-rect_width/2  # Centrer horizontalement
    spacing = 40  # Espace entre les rectangles
    start_y = (screen_height - (rect_height * len(menu_options) + spacing * (len(menu_options) - 1))) // 2  # Centrer verticalement
    
    cursor_on_button = False

    menu_rects.clear()
   
    # Dessiner chaque option de menu

    for i, option in enumerate(menu_options):
        # Position du bouton
        rect_y = start_y + i * (rect_height + spacing)
        button_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

        # Vérifier le survol
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(pygame.transform.scale(button_images[option], (rect_width, rect_height)), (rect_x, rect_y))
            cursor_on_button = True
        else:
            screen.blit(pygame.transform.scale(button_images[option], (rect_width, rect_height)), (rect_x, rect_y))

        # Ajouter le rectangle à la liste pour gestion des clics
        menu_rects.append(button_rect)    
    # for i, option in enumerate(menu_options):
    #     # Calculer la position de chaque rectangle
    #     rect_y = start_y + i * (rect_height + spacing)
        
    #     # Dessiner le rectangle
    #     button_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

    #     # Draw button with hover effect
    #     if button_rect.collidepoint(pygame.mouse.get_pos()):
    #         screen.blit(button_hover_image, (rect_x, rect_y))
    #         cursor_on_button = True
    #     else:
    #         screen.blit(button_image, (rect_x, rect_y))
            
        
    #     # Rendre le texte et le centrer dans le rectangle
    #     text_surface = font.render(option, True, "BLACK")
    #     text_rect = text_surface.get_rect(center=(rect_x + rect_width // 2, rect_y + rect_height // 2))
    #     screen.blit(text_surface, text_rect)

    #     menu_rects.append(button_rect)


        # Process events passed to the function
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()  # Get mouse position
            if menu_rects[3].collidepoint(mouse_pos):  # Check if "Quitter" is clicked
                return 10  # Signal to quit
            elif menu_rects[0].collidepoint(mouse_pos):  # Check if "Jouer" is clicked
                return 20 # Launch game or level selection

     

    if cursor_on_button:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # Curseur "main" pour le survol
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

