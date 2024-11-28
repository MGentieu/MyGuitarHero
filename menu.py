
from header import *


def afficher_menu(events):
    # Declaration des variables
    menu_options = ["Commencer le jeu", "Options", "Instructions", "Quitter"]

    menu_rects = []

    background_image_menu = pygame.image.load("image/Fond_Menu_2.jpg")  # Remplacez par le chemin de votre image

    background_image_menu = pygame.transform.scale(background_image_menu, (screen_width, screen_height))  # Redimensionne si nécessaire

    screen.blit(background_image_menu, (0, 0))

    font = pygame.font.Font(None, 36)
    
    # Taille et espacement des rectangles
    rect_width, rect_height = 350, 70
    rect_x = 20  # Centrer horizontalement
    spacing = 40  # Espace entre les rectangles
    start_y = (screen_height - (rect_height * len(menu_options) + spacing * (len(menu_options) - 1))) // 2  # Centrer verticalement
    
    cursor_on_button = False

    menu_rects.clear()
   
    # Dessiner chaque option de menu
    for i, option in enumerate(menu_options):
        # Calculer la position de chaque rectangle
        rect_y = start_y + i * (rect_height + spacing)
        
        # Dessiner le rectangle
        rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
        pygame.draw.rect(screen, "GRAY", rect)

        if rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, "WHITE", rect)  # Couleur de survol
            pygame.draw.rect(screen, "BLACK", rect, 3)
            cursor_on_button = True  # Curseur "main" pour le survol
        else:
            pygame.draw.rect(screen, "GRAY", rect)  # Couleur par défaut
            
        
        # Rendre le texte et le centrer dans le rectangle
        text_surface = font.render(option, True, "BLACK")
        text_rect = text_surface.get_rect(center=(rect_x + rect_width // 2, rect_y + rect_height // 2))
        screen.blit(text_surface, text_rect)

        menu_rects.append(rect)


        # Process events passed to the function
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()  # Get mouse position
            if menu_rects[3].collidepoint(mouse_pos):  # Check if "Quitter" is clicked
                return 10  # Signal to quit
            elif menu_rects[0].collidepoint(mouse_pos):  # Check if "Jouer" is clicked
                print("Launch level selection menu")  # Launch game or level selection

     

    if cursor_on_button:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # Curseur "main" pour le survol
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

