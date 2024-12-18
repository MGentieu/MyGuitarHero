
from header import *

from selection_musique import *


def afficher_menu(events):
    # Declaration des variables
    menu_options = ["Jouer", "Options", "Aide", "Quitter"]

    menu_rects = []

    # Charger l'image de fond
    background_image_menu = pygame.image.load("image/Fond_Menu_2.jpg")
    background_image_menu = pygame.transform.scale(background_image_menu, (screen_width, screen_height))
    screen.blit(background_image_menu, (0, 0))

    # Charger la police du menu
    font = pygame.font.Font("Polices/PressStart2P-Regular.ttf", 28)

    # Charger les images de boutons vides
    button_image = pygame.image.load("image/bouton_menu_vide.png")  # Bouton normal
    button_hover_image = pygame.image.load("image/bouton_menu_vide_hover.png")  # Bouton hover
    button_width, button_height = button_image.get_size()

    # Taille et espacement des boutons
    spacing = 40  # Espace entre les boutons
    start_y = (screen_height - (button_height * len(menu_options) + spacing * (len(menu_options) - 1))) // 2  # Centrer verticalement

    cursor_on_button = False

    menu_rects.clear()

    # Dessiner chaque option de menu
    for i, option in enumerate(menu_options):
        # Calculer la position de chaque bouton
        rect_x = screen_width / 2 - button_width / 2  # Centrer horizontalement
        rect_y = start_y + i * (button_height + spacing)

        # Vérifier si la souris survole le bouton
        is_hovered = pygame.Rect(rect_x, rect_y, button_width, button_height).collidepoint(pygame.mouse.get_pos())

        # Dessiner l'image correspondante (normale ou hover)
        if is_hovered:
            screen.blit(button_hover_image, (rect_x, rect_y))  # Image de hover
            cursor_on_button = True  # Active le curseur "main"
        else:
            screen.blit(button_image, (rect_x, rect_y))  # Image par défaut

        # Ajouter le texte et le centrer dynamiquement sur le bouton
        text_surface = font.render(option.upper(), True, "WHITE")
        if is_hovered:
            text_rect = text_surface.get_rect(center=(rect_x + button_width // 2, rect_y + button_height // 2))
        else:
            text_rect = text_surface.get_rect(center=(rect_x + button_width // 2, (rect_y + button_height // 2)-10))

        screen.blit(text_surface, text_rect)

        # Ajouter un rectangle pour détecter les clics
        button_rect = pygame.Rect(rect_x, rect_y, button_width, button_height)
        menu_rects.append(button_rect)

    # Modifier le curseur si nécessaire
    if cursor_on_button:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)    
   

        # Process events passed to the function
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()  # Get mouse position
            if menu_rects[3].collidepoint(mouse_pos):  # Check if "Quitter" is clicked
                return 10  # Signal to quit
            elif menu_rects[0].collidepoint(mouse_pos):  # Check if "Jouer" is clicked
                return 20 # Launch game or level selection

            elif menu_rects[2].collidepoint(mouse_pos):
                return 30 #lancer l'aide

     

    if cursor_on_button:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # Curseur "main" pour le survol
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

