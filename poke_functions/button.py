from pygame import *
import pygame

red_color = (255, 0, 0)
green_color = (0, 255, 0)
white_color = (255, 255, 255)


# Button class
class Button:
    def __init__(self, x, y, width, height, text, color, selected_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.selected_color = selected_color
        self.selected = False

    def draw(self, surface: Surface):
        black_color = (0, 0, 0)
        # Draw the button
        pygame.draw.rect(
            surface, self.selected_color if self.selected else self.color, self.rect, 2
        )

        # Draw the button text
        ## Set up the font
        font = pygame.font.SysFont(None, 30)
        text_surface = font.render(self.text, True, black_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
