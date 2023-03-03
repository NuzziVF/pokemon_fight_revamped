import pygame
from button import Button


def game_loop():
    # Initialize Pygame
    pygame.init()

    # Set up the screen
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("My Pygame")

    # Set up the clock
    clock = pygame.time.Clock()

    # Set up the rectangle
    rect_color = (0, 0, 0)
    rect_width = 750
    rect_height = 175
    rect_position = (
        screen_width / 2 - rect_width / 2,
        (screen_height - rect_height) - 20,
    )
    rect_thickness = 2
    red_color = (255, 0, 0)
    green_color = (0, 255, 0)
    black_color = (0, 0, 0)
    white_color = (255, 255, 255)

    # Load an image from disk
    image1 = pygame.image.load("images/charizard.png")
    image2 = pygame.image.load("images/venasaur.png")
    image3 = pygame.image.load("images/blastoise.png")

    # Get the rectangle representing the loaded image
    image_rect1 = image1.get_rect()
    image_rect2 = image2.get_rect()
    image_rect3 = image3.get_rect()

    # Set up the buttons
    button_width = 200
    button_height = 50
    button_margin = 20
    button1 = Button(
        (screen_width / 4 - button_width / 4) - 100,
        screen_height / 1.205 - button_height - button_margin,
        button_width,
        button_height,
        "Button 1",
        white_color,
        black_color,
    )
    button2 = Button(
        (screen_width / 4 - button_width / 4) - 100,
        screen_height / 1.205 + button_margin,
        button_width,
        button_height,
        "Button 2",
        white_color,
        black_color,
    )
    button3 = Button(
        (screen_width / 2 - button_width / 2),
        screen_height / 1.205 - button_height - button_margin,
        button_width,
        button_height,
        "Button 3",
        white_color,
        black_color,
    )
    button4 = Button(
        (screen_width / 2 - button_width / 2),
        screen_height / 1.205 + button_margin,
        button_width,
        button_height,
        "Button 4",
        white_color,
        black_color,
    )

    buttons = [button1, button2, button3, button4]
    selected_button_index = 0

    # Main game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # Handle up arrow key press
                    selected_button_index = (selected_button_index - 1) % len(buttons)
                elif event.key == pygame.K_DOWN:
                    # Handle down arrow key press
                    selected_button_index = (selected_button_index + 1) % len(buttons)
                elif event.key == pygame.K_LEFT:
                    # Handle left arrow key press
                    pass
                elif event.key == pygame.K_RIGHT:
                    # Handle right arrow key press
                    pass
                elif event.key == pygame.K_RETURN:
                    # Handle enter key press
                    if buttons[selected_button_index] == button1:
                        print("Button 1 pressed!")
                    if buttons[selected_button_index] == button2:
                        print("Button 2 pressed!")
                    if buttons[selected_button_index] == button3:
                        print("Button 3 pressed!")
                    if buttons[selected_button_index] == button4:
                        print("Button 4 pressed!")

        # Update game state
        for i, button in enumerate(buttons):
            button.selected = i == selected_button_index

        # Draw on the screen
        screen.fill((255, 255, 255))
        pygame.draw.rect(
            screen,
            rect_color,
            (rect_position, (rect_width, rect_height)),
            rect_thickness,
        )

        # Draw the image on the screen
        screen.blit(image1, image_rect1)
        screen.blit(image2, image_rect2)
        screen.blit(image3, image_rect3)

        for button in buttons:
            button.draw(screen)

        # Update the screen
        pygame.display.update()

        # Set the FPS
        clock.tick(60)
