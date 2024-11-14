import pygame
import pygame.gfxdraw 

import numpy as np
import tkinter as tk

def VertGradientColumn(surf, topcolor, bottomcolor):
    "creates a new 3d vertical gradient array"
    topcolor = np.array(topcolor, copy=False)
    bottomcolor = np.array(bottomcolor, copy=False)
    diff = bottomcolor - topcolor
    width, height = surf.get_size()
    # create array from 0.0 to 1.0 triplets
    column = np.arange(height, dtype="float") / height
    column = np.repeat(column[:, np.newaxis], [3], 1)
    # create a single column of gradient
    column = topcolor + (diff * column).astype("int")
    # make the column a 3d image column by adding X
    column = column.astype("uint8")[np.newaxis, :, :]
    # 3d array into 2d array
    return pygame.surfarray.map_array(surf, column)

def DisplayGradient(surf):
    "choose random colors and show them"
    #colors = np_random.randint(0, 255, (2, 3))
    colors = [[255, 255, 255], [55, 55, 55]]
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

    DisplayGradient(screen)
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
        
if __name__ == "__main__":
    main()