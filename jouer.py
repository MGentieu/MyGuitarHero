from header import *  # Assure que header.py contient les constantes et initialisations nécessaires

def jouer(events,choix_musique):
    # Charger l'image de fond
    background_image_menu = pygame.image.load("image/Fond_Menu_2.jpg")
    background_image_menu = pygame.transform.scale(background_image_menu, (screen_width, screen_height))
    screen.blit(background_image_menu, (0, 0))

    # Charger les polices
    font = pygame.font.Font("Polices/PressStart2P-Regular.ttf", 30)
    font2 = pygame.font.Font("Polices/PressStart2P-Regular.ttf", 15)  # Réduire la taille pour gérer plus de texte

    # Texte d'aide
    aide_text = (
        f"Sous programme de jeu de la musique {choix_musique}"
    )

    # Taille et position du rectangle contenant l'aide
    rect_width, rect_height = 600, 300
    rect_x = (screen_width - rect_width) // 2
    rect_y = (screen_height - rect_height) // 2
    rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

    # Dessiner le rectangle rouge
    pygame.draw.rect(screen, (0, 0, 0), rectangle.inflate(10, 10))
    pygame.draw.rect(screen, (242,104,104), rectangle)

    # Calculer la largeur disponible pour le texte dans le rectangle
    text_width = rect_width - 40  # Ajouter une marge de 20px de chaque côté
    margin_x = rect_x + 20  # Positionner le texte avec une marge
    text_y = rect_y + 20  # Initialiser la position verticale

    # Diviser le texte pour qu'il tienne dans la largeur du rectangle
    words = aide_text.split(" ")
    lines = []
    current_line = ""

    for word in words:
        # Tester si on peut ajouter le mot à la ligne actuelle
        test_line = current_line + word + " "
        if font2.size(test_line)[0] <= text_width:  # Tester si la ligne reste dans la largeur
            current_line = test_line
        else:
            lines.append(current_line)  # Sauvegarder la ligne actuelle
            current_line = word + " "  # Démarrer une nouvelle ligne

    if current_line:  # Ajouter la dernière ligne
        lines.append(current_line)

    # Calculer la hauteur totale occupée par toutes les lignes pour centrer verticalement
    total_text_height = len(lines) * font2.size(lines[0])[1]
    centered_text_y = rect_y + (rect_height - total_text_height) // 2  # Point de départ vertical centré

    # Afficher les lignes dans le rectangle
    for line in lines:
        text_surface = font2.render(line, True, "WHITE")
        text_rect = text_surface.get_rect(center=(rect_x + rect_width // 2, centered_text_y))  # Centrer horizontalement
        screen.blit(text_surface, text_rect)
        centered_text_y += font2.size(line)[1]  # Décaler verticalement pour la ligne suivante

        # Arrêter si le texte dépasse la hauteur du rectangle
        if centered_text_y > rect_y + rect_height - 20:
            break

    # Bouton "Retour"
    button_image = pygame.image.load("image/bouton_menu_vide.png")
    button_image_hover = pygame.image.load("image/bouton_menu_vide_hover.png")
    button_width, button_height = button_image.get_size()

    # Positionner le bouton "Retour"
    rect_x = (screen_width - button_width) // 2
    rect_y = screen_height - button_height - 50  # Position en bas de l'écran
    menu_rect = pygame.Rect(rect_x, rect_y, button_width, button_height)

    # Gérer le survol du bouton
    is_hovered = menu_rect.collidepoint(pygame.mouse.get_pos())

    if is_hovered:
        screen.blit(button_image_hover, (rect_x, rect_y))
    else:
        screen.blit(button_image, (rect_x, rect_y))

    # Ajouter le texte "Retour" centré sur le bouton
    text_surface = font.render("RETOUR", True, "WHITE")
    if is_hovered:
        text_rect = text_surface.get_rect(center=(rect_x + button_width // 2, rect_y + button_height // 2))
    else:
        text_rect = text_surface.get_rect(center=(rect_x + button_width // 2, (rect_y + button_height // 2)-10))
    
    screen.blit(text_surface, text_rect)

    # Mettre à jour l'écran
    pygame.display.flip()

    # Gérer les événements
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if menu_rect.collidepoint(mouse_pos):  # Si on clique sur le bouton "Retour"
                return 10  # Retour au menu principal
    return 0
