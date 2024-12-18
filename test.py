import pygame
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guitar Hero - Prototype")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Ligne de synchronisation
SYNC_LINE_Y = HEIGHT - 100

# Colonnes et touches associées
columns = [
    {"x": WIDTH // 5, "color": "RED", "key": pygame.K_1},
    {"x": WIDTH // 5 * 2, "color": "GREEN", "key": pygame.K_2},
    {"x": WIDTH // 5 * 3, "color": "BLUE", "key": pygame.K_e},
    {"x": WIDTH // 5 * 4, "color": "YELLOW", "key": pygame.K_r},
]

# Liste pour stocker les notes actives
notes = []

# Vitesse des notes
note_speed = 5

# Horloge
clock = pygame.time.Clock()

# Police pour le score
font = pygame.font.Font(None, 36)

# Score
score = 0

# Fonction pour dessiner la ligne de synchronisation
def draw_sync_line():
    pygame.draw.line(screen, WHITE, (0, SYNC_LINE_Y), (WIDTH, SYNC_LINE_Y), 3)

# Fonction pour générer une nouvelle note
def create_note():
    column = random.choice(columns)  # Choisit une colonne aléatoire
    note = {"x": column["x"], "y": 0, "color": column["color"], "column": column}
    notes.append(note)

# Fonction pour dessiner les notes
def draw_notes():
    for note in notes:
        pygame.draw.circle(screen, note["color"], (note["x"], note["y"]), 20)

# Fonction pour gérer le mouvement des notes
def update_notes():
    global score
    for note in notes[:]:
        note["y"] += note_speed
        # Si la note atteint la ligne de synchronisation sans être appuyée, elle est perdue
        if note["y"] > SYNC_LINE_Y + 20:
            notes.remove(note)

# Fonction pour gérer les interactions clavier
def handle_input():
    global score
    keys = pygame.key.get_pressed()
    for note in notes[:]:
        if SYNC_LINE_Y - 20 <= note["y"] <= SYNC_LINE_Y + 20:  # Note proche de la ligne
            if keys[note["column"]["key"]]:  # Bonne touche appuyée
                score += 1  # Augmenter le score
                notes.remove(note)  # Supprimer la note

# Boucle principale
running = True
note_timer = 0
note_interval = 1000  # Intervalle entre les notes en millisecondes

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ajouter des notes à intervalles réguliers
    note_timer += clock.get_time()
    if note_timer > note_interval:
        create_note()
        note_timer = 0

    # Mettre à jour les notes
    update_notes()

    # Gérer les interactions clavier
    handle_input()

    # Afficher les éléments
    screen.fill(BLACK)  # Fond noir
    draw_sync_line()
    draw_notes()

    # Afficher le score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Contrôler la vitesse de la boucle
    clock.tick(60)

# Quitter Pygame
pygame.quit()
