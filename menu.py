# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
WIDTH=1280
HEIGHT=720
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True



def afficher_menu():
    # screen.fill("WHITE")

    menu_options = ["Commencer le jeu", "Options", "Instructions", "Quitter"]

    background_image_menu = pygame.image.load("image/Fond_Menu.jpg")  # Remplacez par le chemin de votre image

    background_image_menu = pygame.transform.scale(background_image_menu, (WIDTH, HEIGHT))  # Redimensionne si nécessaire

    screen.blit(background_image_menu, (0, 0))

    font = pygame.font.Font(None, 36)
    
    # Taille et espacement des rectangles
    rect_width, rect_height = 300, 50
    rect_x = (WIDTH - rect_width) // 2  # Centrer horizontalement
    spacing = 20  # Espace entre les rectangles
    start_y = (HEIGHT - (rect_height * len(menu_options) + spacing * (len(menu_options) - 1))) // 2  # Centrer verticalement
    
    # Dessiner chaque option de menu
    for i, option in enumerate(menu_options):
        # Calculer la position de chaque rectangle
        rect_y = start_y + i * (rect_height + spacing)
        
        # Dessiner le rectangle
        rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
        pygame.draw.rect(screen, "GRAY", rect)
        
        # Rendre le texte et le centrer dans le rectangle
        text_surface = font.render(option, True, "BLACK")
        text_rect = text_surface.get_rect(center=(rect_x + rect_width // 2, rect_y + rect_height // 2))
        screen.blit(text_surface, text_rect)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame

    afficher_menu()
    # screen.fill("red")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()