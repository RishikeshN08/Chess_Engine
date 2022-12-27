import pygame as p
import sys

import ChessEngine

width = height = 800
Squares = 8
size = height // Squares
images = {}

def get_images():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load("/Users/rishin/Documents/GitHub/Chess_Engine/images/" +
                                                       piece + ".png"),(size, size))

def main():
    # Create a pygame display
    p.init()
    screen = p.display.set_mode((width, height))
    running = True
    get_images()
    game = ChessEngine.Game()
    while running:
        for e in p.event.get():

            # Quit
            if e.type == p.QUIT:
                p.quit()
                sys.exit()
        board(screen)
        pieces(screen, game.board)
        p.display.update()



def board(screen):
    """
    Draw the squares on the board.
    The top left square is always light.
    """
    colors = [p.Color("white"), p.Color(170, 210, 236)]
    for row in range(Squares):
        for col in range(Squares):
            color = colors[((row + col) % 2)]
            p.draw.rect(screen, color, p.Rect(col * size, row * size, size, size))


def pieces(screen, board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != "--":
                screen.blit(images[piece], p.Rect(col * size, row * size, size, size))


if __name__ == "__main__":
    main()