# Example file showing a basic pygame "game loop"
import pygame

import tkinter as tk

# pygame setup
pygame.init()



# Création d'une fenêtre tkinter
root = tk.Tk()
root.withdraw()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#Configuration de la fenetre de jeu
size = screen_width, screen_height
screen = pygame.display.set_mode(size, pygame.NOFRAME, 0)
clock = pygame.time.Clock()
running = True