from header import *


def menu_selection_musique(events):
    # Declaration des variables
    choix_musique = ["Musique 1", "Musique 2", "Musique 3","Retour"]

    menu_rects = []

    background_image_menu = pygame.image.load("image/Fond_Menu_2.jpg")  

    background_image_menu = pygame.transform.scale(background_image_menu, (screen_width, screen_height))  

    screen.blit(background_image_menu, (0, 0))

    
    # Charger la police du menu
    font = pygame.font.Font("Polices/PressStart2P-Regular.ttf", 30)

    # Charger l'image des boutons vides
    button_image = pygame.image.load("image/bouton_menu_vide.png")  

    button_image_hover = pygame.image.load("image/bouton_menu_vide_hover.png")
    button_width, button_height = button_image.get_size()  


    
    # Taille et espacement des boutons
    spacing=40
    start_y = (screen_height - (button_height * len(choix_musique) + spacing * (len(choix_musique) - 1))) // 2  # Centrer verticalement
    
    cursor_on_button = False

    menu_rects.clear()


    for i, option in enumerate(choix_musique):
        # Calculer la position de chaque bouton
        rect_x = screen_width / 2 - button_width / 2  # Centrer horizontalement
        rect_y = start_y + i * (button_height + spacing)

        # Dessiner le bouton (image)
        # screen.blit(button_image, (rect_x, rect_y))

        is_hovered = pygame.Rect(rect_x, rect_y, button_width, button_height).collidepoint(pygame.mouse.get_pos())


        if is_hovered:
            screen.blit(button_image_hover, (rect_x, rect_y))  # Image de hover
            cursor_on_button = True  # Active le curseur "main"
        else:
            screen.blit(button_image, (rect_x, rect_y)) 

        # Rendre le texte et le centrer dans l'image du bouton
        text_surface = font.render(option.upper(), True, "WHITE")
        if is_hovered:
            # Ajuster la position du texte pour l'image hover
            text_rect = text_surface.get_rect(center=(rect_x + button_width // 2, rect_y + button_height // 2))  
        else:
             # Position du texte pour l'image normale
            text_rect = text_surface.get_rect(center=(rect_x + button_width // 2, (rect_y + button_height // 2)-10))
        
        screen.blit(text_surface, text_rect)

        # Créer un rectangle pour détecter les clics
        rect = pygame.Rect(rect_x, rect_y, button_width, button_height)
        menu_rects.append(rect)

 
   
        # Process events passed to the function
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()  # Get mouse position
            if menu_rects[0].collidepoint(mouse_pos):  # 
                return 1 # 
            elif menu_rects[1].collidepoint(mouse_pos):  # 
                return 2  # 
            elif menu_rects[2].collidepoint(mouse_pos):  # 
                return 3
            elif menu_rects[3].collidepoint(mouse_pos):  # 
                return 10  # 

     

    if cursor_on_button:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # Curseur "main" pour le survol
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)