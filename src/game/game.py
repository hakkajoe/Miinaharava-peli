import pygame
import os
from game.piece import Piece

class Game():
    def __init__(self, board, screensize):
        self._board = board
        self._screensize = screensize
        self._piecesize = self._screensize[0] // self._board.GetSize()[1], self._screensize[1] // self._board.GetSize()[0]
        self._load_images()

    def run(self):
        pygame.init()
        self._screen = pygame.display.set_mode(self._screensize)
        running = True
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
            self._draw()
            pygame.display.flip()
        pygame.quit()

    def _draw(self):
        top_left = (0,0)
        for row in range(self._board.GetSize()[0]):
            for col in range(self._board.GetSize()[1]):
                piece = self._board.GetPiece((row, col))
                image = self._GetImage(piece)
                self._screen.blit(image, top_left)
                top_left = top_left[0] + self._piecesize[0], top_left[1]
            top_left = 0, top_left[1] + self._piecesize[1]

    def _load_images(self):
        self._images = {}
        dirname = os.path.dirname(__file__)
        for file in os.listdir(f"{dirname}/assets"):
            if (not file.endswith(".png")):
                continue
            image = pygame.image.load(f"{dirname}/assets/" + file)
            image = pygame.transform.scale(image, self._piecesize)
            self._images[file.split(".")[0]] = image

    def _GetImage(self, piece):
        string = "bomb" if piece.GetHasBomb() else "empty_unclicked"
        return self._images[string]