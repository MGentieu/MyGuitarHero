import pygame
import pygame.gfxdraw 

import numpy as np
import tkinter as tk

def VertGradientColumn(surf, topcolor, bottomcolor):
    "creates a new 3d vertical gradient array"
    topcolor = np.asarray(topcolor)
    bottomcolor = np.asarray(bottomcolor)
    diff = bottomcolor - topcolor
    width, height = surf.get_size()
    # create array from 0.0 to 1.0 triplets
    column = np.arange(height, dtype="float") / height
    column = np.repeat(column[:, np.newaxis], 3, axis=1)
    # create a single column of gradient
    column = topcolor + (diff * column).astype("int")
    # make the column a 3d image by adding width dimension
    column = np.tile(column, (width, 1, 1)).astype("uint8")
    return column

def DisplayGradient(surf):
    "choose random colors and show them"
    colors = np.array([[55, 20, 55], [0, 0, 10]])  # Deux couleurs en tableau numpy
    column = VertGradientColumn(surf, colors[0], colors[1])
    pygame.surfarray.blit_array(surf, column)
    pygame.display.flip()

def main():
    

# Création d'une fenêtre tkinter
    root = tk.Tk()
    root.withdraw()  # Cache la fenêtre tkinter

# Récupération de la largeur et de la hauteur de l'écran
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()


    pygame.init()
    size = screen_width, screen_height
    screen = pygame.display.set_mode(size, pygame.NOFRAME, 0)
    #screen.fill((10, 10, 55))
    color = (255,255,255)
    points = [(40,40),(200,200),(40,200)]
    points2=[(500,40),(700,200),(500,200)]
    Coordonnees_manche = [(2*screen_width/3, screen_height), (screen_width/3, screen_height), 
                          (2*screen_width/5, screen_height/4), (3*screen_width/5, screen_height/4)]
    texture = pygame.image.load("../microphone.jpg")

    DisplayGradient(screen)
    #pygame.gfxdraw.filled_polygon(screen, points, color)
    #pygame.gfxdraw.textured_polygon(screen, points2, texture, -50, -50)
    #pygame.gfxdraw.filled_polygon(screen, Coordonnees_manche, color)
    pygame.gfxdraw.textured_polygon(screen, Coordonnees_manche, texture, 0, 0)
    pygame.display.flip()
    try:
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.unicode == "q":
                    break
            
    finally:
        pygame.quit()
        
main()