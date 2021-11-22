import pygame
import random
import sys

DIAMOND_ASSETPATH = {
    "red": "./assets/red_diamond.png",
    "green": "./assets/green_diamond.png",
    "blue": "./assets/blue_diamond.png",
    "yellow": "./assets/yellow_diamond.png",
    "tan": "./assets/tan_diamond.png",
    "grey": "./assets/grey_diamond.png",
    "teal": "./assets/teal_diamond.png"
}
HEXAGON_ASSETPATH = {
    "red": "./assets/red_hexagon.png",
    "green": "./assets/green_hexagon.png",
    "blue": "./assets/blue_hexagon.png",
    "yellow": "./assets/yellow_hexagon.png",
    "tan": "./assets/tan_hexagon.png",
    "grey": "./assets/grey_hexagon.png",
    "teal": "./assets/teal_hexagon.png"
}
OCTAGON_ASSETPATH = {
    "red": "./assets/red_octagon.png",
    "green": "./assets/green_octagon.png",
    "blue": "./assets/blue_octagon.png",
    "yellow": "./assets/yellow_octagon.png",
    "tan": "./assets/tan_octagon.png",
    "grey": "./assets/grey_octagon.png",
    "teal": "./assets/teal_octagon.png"
}
SQUARE_ASSETPATH = {
    "red": "./assets/red_square.png",
    "green": "./assets/green_square.png",
    "blue": "./assets/blue_square.png",
    "yellow": "./assets/yellow_square.png",
    "tan": "./assets/tan_square.png",
    "grey": "./assets/grey_square.png",
    "teal": "./assets/teal_square.png"
}
TRIANGLE_ASSETPATH = {
    "red": "./assets/red_triangle.png",
    "green": "./assets/green_triangle.png",
    "blue": "./assets/blue_triangle.png",
    "yellow": "./assets/yellow_triangle.png",
    "tan": "./assets/tan_triangle.png",
    "grey": "./assets/grey_triangle.png",
    "teal": "./assets/teal_triangle.png"
}
"""Coding global variables"""
global FPS_CLOCK, DISPLAYSURF
FPS = 40  # frames per second, the general speed of the program
WINDOWWIDTH = 640  # size of window's width in pixels
WINDOWHEIGHT = 580  # size of windows' height in pixels
REVEALSPEED = 5  # speed boxes' sliding reveals and covers
BOXSIZE = 40  # size of box height & width in pixels
GAPSIZE = 10  # size of gap between boxes in pixels
BOARDWIDTH = 4  # number of columns of icons
BOARDHEIGHT = 3  # number of rows of icons
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)
GAME_SCORE = 0
GAME_LEVEL = 1
GAME_PAUSED = False

#            R    G    B
GRAY = (100, 100, 100)
ROYALBLUE = (0, 35, 102)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

BGCOLOR = ROYALBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

TIMER_PAUSED = False
TIMER_RUNNING = True

SQUARE = 'square'
DIAMOND = 'diamond'
HEXAGON = 'hexagon'
OCTAGON = 'octagon'
TRIANGLE = 'triangle'

SPRITE_RED = "red"
SPRITE_GREEN = "green"
SPRITE_BLUE = "blue"
SPRITE_YELLOW = "yellow"
SPRITE_TAN = "tan"
SPRITE_GREY = "grey"
SPRITE_TEAL = "teal"

ALLCOLORS = (SPRITE_RED, SPRITE_GREEN, SPRITE_BLUE, SPRITE_YELLOW, SPRITE_TAN, SPRITE_GREY, SPRITE_TEAL)
ALLSHAPES = (DIAMOND, HEXAGON, OCTAGON, SQUARE, TRIANGLE)


def level_up():
    """This function add one row and one column everytime user reach next level in order to increase difficulty"""
    global BOARDWIDTH, BOARDHEIGHT
    BOARDWIDTH += 1
    BOARDHEIGHT += 1


def background_music():
    """Adding background music"""
    pygame.mixer.init()
    pygame.mixer.music.load('background_music.mp3')
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.15)


def draw_diamond_sprite(color, left, top, width, height):
    """This function instantiate a gem object using asset path and passing colours.
     It also scale the image to match the height and width of the rectangle in game window.
     By using draw function, it draws the shape in game display window"""
    diamond_image = DIAMOND_ASSETPATH[color] or None
    diamond_image = pygame.transform.scale(pygame.image.load(diamond_image).convert_alpha(), (width, height))
    diamond = Gem((left, top), diamond_image)
    diamond.draw(DISPLAYSURF)


def draw_hexagon_sprite(color, left, top, width, height):
    hexagon_image = HEXAGON_ASSETPATH[color] or None
    hexagon_image = pygame.transform.scale(pygame.image.load(hexagon_image).convert_alpha(), (width, height))
    hexagon = Gem((left, top), hexagon_image)
    hexagon.draw(DISPLAYSURF)


def draw_octagon_sprite(color, left, top, width, height):
    octagon_image = OCTAGON_ASSETPATH[color] or None
    octagon_image = pygame.transform.scale(pygame.image.load(octagon_image).convert_alpha(), (width, height))
    octagon = Gem((left, top), octagon_image)
    octagon.draw(DISPLAYSURF)


def draw_square_sprite(color, left, top, width, height):
    square_image = SQUARE_ASSETPATH[color] or None
    square_image = pygame.transform.scale(pygame.image.load(square_image).convert_alpha(), (width, height))
    square = Gem((left, top), square_image)
    square.draw(DISPLAYSURF)


def draw_triangle_sprite(color, left, top, width, height):
    triangle_image = TRIANGLE_ASSETPATH[color] or None
    triangle_image = pygame.transform.scale(pygame.image.load(triangle_image).convert_alpha(), (width, height))
    triangle = Gem((left, top), triangle_image)
    triangle.draw(DISPLAYSURF)


class Gem(pygame.sprite.Sprite):
    """It is a python sprite class which takes position and image as argument,
    it takes the image and place it in right position"""
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)

    def draw(self, screen):
        """it uses blit method in order to draw object in game window
        screen argument is represented by DISPLAYSURF which is pygame main window"""
        screen.blit(self.image, self.rect)


def text_objects(text, font):
    """ Font.render()  is used to create an image (Surface) of the text, then blit this image onto the Surface"""
    text_surface = font.render(text, True, (0, 0, 0))
    return text_surface, text_surface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    """msg = str(text for the button), w=width, h=height,ic=inactive_colour,
    ac=active colour, action will execute if the button is clicked  """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(DISPLAYSURF, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(DISPLAYSURF, ic, (x, y, w, h))

    small_text = pygame.font.SysFont("comicsansms", 20)
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    DISPLAYSURF.blit(text_surf, text_rect)


def unpause():
    """It setting the game as unpause by setting GAME_PAUSED variable false"""
    global GAME_PAUSED
    GAME_PAUSED = False


def quit_game():
    """It quits pygame before exiting python"""
    pygame.quit()
    sys.exit()


def pause():
    """It checks if GAME_PAUSED variable is set to true.
    If it is true, it shows a pause menu onto the main window with the 'Resume' and 'Quit' button.
    if resume button is clicked then un_paused method is called, and if the quit button is clicked
    the game will automatically quit and then screen will be updated"""
    font = pygame.font.SysFont("Consolas", 32)
    while GAME_PAUSED:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pause_text = font.render("Game Paused", True, (255, 255, 255))
        pause_rect = pause_text.get_rect(center=(WINDOWWIDTH / 2, WINDOWHEIGHT / 2 - 210))
        print(pause_text.get_size())
        pause_surface = pygame.Surface((210, 145))
        pause_surface.fill((0, 0, 0))
        pause_surface.blit(pause_text, (0, 0))
        DISPLAYSURF.blit(pause_surface, pause_rect)
        button("Resume", WINDOWWIDTH / 2 - 35, WINDOWHEIGHT / 2 - 140, 100, 50, ROYALBLUE, GRAY, unpause)
        button("Quit", WINDOWWIDTH / 2 - 35, WINDOWHEIGHT / 2 - 190, 100, 50, ROYALBLUE, GRAY, quit_game)
        pygame.display.update()
        FPS_CLOCK.tick(FPS)


def main():  # sourcery no-metrics skip: none-compare
    """All main functions are called to run the game"""

    global FPS_CLOCK, DISPLAYSURF, GAME_SCORE, GAME_LEVEL, GAME_PAUSED
    pygame.init()         # to initialize pygame
    background_music()
    FPS_CLOCK = pygame.time.Clock()   # in order to set general time for the game
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))    # to set the main window

    mousex = 0
    mousey = 0
    pygame.display.set_caption('Memory Game')

    main_board = get_randomized_board()   # it randomize all the objects in the board
    revealed_boxes = generate_revealed_boxes_data(False)

    first_selection = None

    DISPLAYSURF.fill(BGCOLOR)
    start_game_animation(main_board)
    pygame.time.get_ticks()

    while True:
        mouse_clicked = False

        DISPLAYSURF.fill(BGCOLOR)
        draw_board(main_board, revealed_boxes)
        font = pygame.font.SysFont("", 32)
        game_score_string = "Score: " + str(GAME_SCORE) + "     Level: " + str(GAME_LEVEL)
        game_score_text = font.render(game_score_string, True, (255, 255, 255))
        game_score_rect = game_score_text.get_rect(center=(120, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:  # to display pause menu
                GAME_PAUSED = True
            elif event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouse_clicked = True
            pause()
        DISPLAYSURF.fill((0, 0, 0), (0, 0, 250, 30))
        DISPLAYSURF.blit(game_score_text, game_score_rect)
        boxx, boxy = get_box_at_pixel(mousex, mousey)
        if boxx is not None and boxy is not None:
            if not revealed_boxes[boxx][boxy]:
                draw_highlight_box(boxx, boxy)
            if not revealed_boxes[boxx][boxy] and mouse_clicked:
                reveal_boxes_animation(main_board, [(boxx, boxy)])
                revealed_boxes[boxx][boxy] = True
                if first_selection is None:
                    first_selection = (boxx, boxy)
                else:
                    icon1shape, icon1color = get_shape_and_color(main_board, first_selection[0], first_selection[1])
                    icon2shape, icon2color = get_shape_and_color(main_board, boxx, boxy)
                    if icon1shape != icon2shape or icon1color != icon2color:
                        pygame.time.wait(1000)
                        cover_boxes_animation(main_board, [(first_selection[0], first_selection[1]), (boxx, boxy)])
                        revealed_boxes[first_selection[0]][first_selection[1]] = False
                        revealed_boxes[boxx][boxy] = False
                    elif has_won(revealed_boxes):
                        game_won_animation(main_board)
                        pygame.time.wait(2000)
                        level_up()
                        GAME_LEVEL += 1
                        main_board = get_randomized_board()
                        revealed_boxes = generate_revealed_boxes_data(False)

                        draw_board(main_board, revealed_boxes)

                        pygame.display.update()
                        pygame.time.wait(1000)
                        start_game_animation(main_board)

                    first_selection = None

        pygame.display.update()

        FPS_CLOCK.tick(FPS)


def generate_revealed_boxes_data(val):
    """It takes a boolean val as argument and return a array of boolean values
    where true value indicates reveal box to show sprite under it and false value indicates cover up each box"""
    return [[val] * BOARDHEIGHT for _ in range(BOARDWIDTH)]


def get_randomized_board():
    """This function get all possible shapes in every possible colours in a list called icons and
    ir randomly shuffles the list items and makes two copy of each item of the list and shuffles again.
    Then two for loop is used to append all the items of icons list in the 2d list called board"""
    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append((shape, color))
    random.shuffle(icons)
    num_icons_used = int(BOARDWIDTH * BOARDHEIGHT / 2)
    icons = icons[:num_icons_used] * 2
    random.shuffle(icons)

    board = []
    for _ in range(BOARDWIDTH):
        column = []
        for _ in range(BOARDHEIGHT):
            column.append(icons[0])
            del icons[0]
        board.append(column)
    # transposeBoard = [*zip(*board)] // might need later on
    return board


def split_into_groups_of(group_size, the_list):
    """It split the game board into a group of boxes
    (ex: it split 16 boxes into a four by four group of boxes and return the result as a list)"""
    return [the_list[i:i + group_size] for i in range(0, len(the_list), group_size)]


def left_top_coords_of_box(boxx, boxy):
    """It transform box coordinate into pixel coordinate to identify which box the user clicks at the time of playing"""
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return left, top


def get_box_at_pixel(x, y):
    """It takes in x and y which is pixel values and goes through boxx and boxy.
    It uses collidepoint function which return True if x and y coordinates are within the bounds of the rectangle.
    It return x and y coordinates of the box"""
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = left_top_coords_of_box(boxx, boxy)
            box_rect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if box_rect.collidepoint(x, y):
                return boxx, boxy
    return None, None


def draw_icon(shape, color, boxx, boxy):
    """This function is used to draw sprite that will displayed on gameboard.
     It takes four parameters to draw appropriate shapes with appropriate colours."""
    # quarter = int(BOXSIZE * 0.25) // Might need later on
    half = int(BOXSIZE * 0.5)

    left, top = left_top_coords_of_box(boxx, boxy)
    if shape == DIAMOND:
        draw_diamond_sprite(color, left + half, top + half, BOXSIZE, BOXSIZE)
    elif shape == HEXAGON:
        draw_hexagon_sprite(color, left + half, top + half, BOXSIZE, BOXSIZE)
    elif shape == OCTAGON:
        draw_octagon_sprite(color, left + half, top + half, BOXSIZE, BOXSIZE)
    elif shape == SQUARE:
        draw_square_sprite(color, left + half, top + half, BOXSIZE, BOXSIZE)
    elif shape == TRIANGLE:
        draw_triangle_sprite(color, left + half, top + half, BOXSIZE, BOXSIZE)


def get_shape_and_color(board, boxx, boxy):
    """It is used to identify shape and colour of a given box position using x and y coordinates of the box position"""
    return board[boxx][boxy][0], board[boxx][boxy][1]


def draw_box_covers(board, boxes, coverage):
    """This function is a frame drawing function for the board.
    It is called repeatedly and with each call all the boxes are given a different coverage amount
    which starts with a positive value and eventually getting to zero value and negative value"""
    # pauseDisplay = False //Might use later on
    for box in boxes:
        left, top = left_top_coords_of_box(box[0], box[1])
        pygame.draw.rect(DISPLAYSURF, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))
        shape, color = get_shape_and_color(board, box[0], box[1])
        draw_icon(shape, color, box[0], box[1])
        if coverage > 0:
            pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, coverage, BOXSIZE))
    pygame.display.update()
    FPS_CLOCK.tick(FPS)


def reveal_boxes_animation(board, boxes_to_reveal):
    """It takes game board and list of boxes as parameter and in order to do reveal boxes animation,
    it repeatedly call draw_box_cover function.
    Here the positive coverage value indicates that the box should be fully or partially covered
    and A negative or zero value indicates  the box should be revealed"""
    for coverage in range(BOXSIZE, (-REVEALSPEED) - 1, -REVEALSPEED):
        print(coverage)
        if coverage < 0:
            pygame.time.wait(1000)
        draw_box_covers(board, boxes_to_reveal, coverage)


def cover_boxes_animation(board, boxes_to_cover):
    """It is the inverse of reveal_boxes_animation where coverage
    starts with a positive number and goes toward a negative number"""
    for coverage in range(0, BOXSIZE + REVEALSPEED, REVEALSPEED):
        draw_box_covers(board, boxes_to_cover, coverage)


def draw_board(board, revealed):
    """It takes in game board and revealed (a boolean) as parameter, where false means
    the box should be covered and true means the box should be revealed"""
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = left_top_coords_of_box(boxx, boxy)
            if not revealed[boxx][boxy]:
                pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
            else:
                shape, color = get_shape_and_color(board, boxx, boxy)
                draw_icon(shape, color, boxx, boxy)


def draw_highlight_box(boxx, boxy):
    """This function is used to highlight the boxes by blue background
     to make the application more responsive for users"""
    left, top = left_top_coords_of_box(boxx, boxy)
    pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left - 5, top - 5, BOXSIZE + 10, BOXSIZE + 10), 4)


def start_game_animation(board):
    """This function generate a list of boxes, shuffles them and split them into a group of boxes
    and hold it into box_group variable. Next it call draw_board function to draw the board and for box_group,
    reveal_boxes_animation and cover_boxes_animation functions are called to reveal the boxes for one second"""
    covered_boxes = generate_revealed_boxes_data(False)
    boxes = []
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            boxes.append((x, y))
    random.shuffle(boxes)
    box_groups = split_into_groups_of(BOARDWIDTH * BOARDHEIGHT, boxes)

    draw_board(board, covered_boxes)
    for boxGroup in box_groups:
        reveal_boxes_animation(board, boxGroup)
        cover_boxes_animation(board, boxGroup)


def game_won_animation(board):
    """This function is called in main function when it is detected that the game has a winning condition.
    A for loop is used to create end game animation, draw a new game board a level higher, updates window and
    wait 300 milli_seconds before exiting the function"""
    covered_boxes = generate_revealed_boxes_data(True)
    color1 = LIGHTBGCOLOR
    color2 = BGCOLOR

    for _ in range(13):
        color1, color2 = color2, color1
        DISPLAYSURF.fill(color1)
        draw_board(board, covered_boxes)
        pygame.display.update()
        pygame.time.wait(300)


def has_won(revealed_boxes):
    """It is called everytime a matching pair of boxes is found. It increase the game score by 10 everytime
    and goes through revealed_boxes list to check if there is a winning condition"""
    global GAME_SCORE
    GAME_SCORE += 10
    for i in revealed_boxes:
        return False not in i


if __name__ == '__main__':
    main()
