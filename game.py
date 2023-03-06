import pygame
from button import Button

# general comment
## tag comment for Ctrl + F

## available tags: screen_config clock time rectangle_config rect_placement color_variables images image_load button_config game_loop key_input input

def game_loop():
    # Initialize Pygame
    ## init
    pygame.init()

    # Set up the screen
    ## screen_config
    
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("My Pygame")

    # Set up the clock
    ## clock time
    clock = pygame.time.Clock()

    # Set up the rectangle
    ## rectangle_config rect_placement
    
    rect_color = (0, 0, 0)
    rect_width = 750
    rect_height = 175
    rect_position = (
        screen_width / 2 - rect_width / 2,
        (screen_height - rect_height) - 20,
    )
    rect_thickness = 2
    
    ## color_variables
    red_color = (255, 0, 0)
    green_color = (0, 255, 0)
    black_color = (0, 0, 0)
    white_color = (255, 255, 255)

    # Load an image from disk
    ## images image_load
    
    image1 = pygame.image.load("images/charizard.png")
    image2 = pygame.image.load("images/venasaur.png")
    image3 = pygame.image.load("images/blastoise.png")
    
    # TODO: mess around with positions to get this to change according to the player specifically.
    image2 = pygame.transform.flip(image2, True, False)

    # Get the rectangle representing the loaded image
    ## image_load
    
    charizard_image = image1.get_rect()
    venasaur_image = image2.get_rect()
    image_rect3 = image3.get_rect()

    # Set the position of each image using the Rect attributes
    enemy_position_x = 450
    enemy_position_y = 25
    player_position_x = 75
    player_position_y = 200
    
    charizard_image.left = enemy_position_x
    charizard_image.top = enemy_position_y
    
    venasaur_image.left = player_position_x
    venasaur_image.top = player_position_y

    

    
    # image_rect1.left = 100
    # image_rect1.top = 100
    # image_rect2.right = 500
    # image_rect2.bottom = 400
    # image_rect3.centerx = 320
    # image_rect3.centery = 240
    

    # Set up the buttons
    ## button_config
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
    ## game_loop
    
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            ## key_input input
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
        ## update_loops
        for i, button in enumerate(buttons):
            button.selected = i == selected_button_index

        # Draw on the screen
        screen.fill((255, 255, 255))
        rect = pygame.draw.rect(
            screen,
            rect_color,
            (rect_position, (rect_width, rect_height)),
            rect_thickness,
        )
        
        venasaur_image.bottom = rect.top - 10


        # Draw the image on the screen
        screen.blit(image1, charizard_image)
        screen.blit(image2, venasaur_image)
        # screen.blit(image3, image_rect3)

        for button in buttons:
            button.draw(screen)

        # Update the screen
        pygame.display.update()

        # Set the FPS
        clock.tick(60)
