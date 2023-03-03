import pygame


# Button class
class Button:
    red_color = (255, 0, 0)
    green_color = (0, 255, 0)
    black_color = (0, 0, 0)
    white_color = (255, 255, 255)

    def __init__(self, x, y, width, height, text, color, selected_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.selected_color = selected_color
        self.selected = False

    def draw(self, surface):
        # Draw the button
        pygame.draw.rect(
            surface, self.selected_color if self.selected else self.color, self.rect, 2
        )

        # Draw the button text
        text_surface = font.render(self.text, True, black_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
