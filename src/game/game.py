import pygame
import os
from time import sleep, time

from game.piece import Piece
from game.board import Board
from services.game_service import game_service


class Game():
    def __init__(self, board, screensize):
        self._board = board
        self._screensize = screensize
        self._piecesize = self._screensize[0] // self._board.GetSize(
        )[1], self._screensize[1] // self._board.GetSize()[0]
        self._load_images()

    def run(self):
        pygame.display.set_caption('Minesweeper')
        pygame.init()
        start_time = time()
        self._screen = pygame.display.set_mode(self._screensize)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    score = 0
                    status = "lost"
                    game_service.update_game_data2(score, status)
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    rightclick = pygame.mouse.get_pressed()[2]
                    self.HandleClick_game(position, rightclick)
            self._draw()
            pygame.display.flip()
            if self._board.GetWon():
                end_time = time()
                score = round(end_time - start_time, 3)
                status = "won"
                game_service.update_game_data2(score, status)
                sleep(3)
                running = False
            if self._board.GetLost():
                score = 0
                status = "lost"
                game_service.update_game_data2(score, status)
                sleep(3)
                running = False
        pygame.quit()

    def _draw(self):
        top_left = (0, 0)
        for row in range(self._board.GetSize()[0]):
            for col in range(self._board.GetSize()[1]):
                piece = self._board._GetPiece((row, col))
                image = self._GetImage(piece)
                self._screen.blit(image, top_left)
                top_left = top_left[0] + self._piecesize[0], top_left[1]
            top_left = 0, top_left[1] + self._piecesize[1]

    def _load_images(self):
        self._images = {}
        dirname = os.path.dirname(__file__)
        for file in os.listdir(f"{dirname}/assets"):
            if not file.endswith(".png"):
                continue
            image = pygame.image.load(f"{dirname}/assets/" + file)
            image = pygame.transform.scale(image, self._piecesize)
            self._images[file.split(".")[0]] = image

    def _GetImage(self, piece):
        string = None
        if piece.GetClicked():
            string = "bomb" if piece.GetHasBomb() else str(piece.GetNumAround())
        else:
            string = "flag" if piece.GetFlagged() else "empty_unclicked"
        return self._images[string]

    def HandleClick_game(self, position, rightclick):
        if self._board.GetLost():
            return
        index = position[1] // self._piecesize[1], position[0] // self._piecesize[0]
        piece = self._board._GetPiece(index)
        self._board.HandleClick_board(piece, rightclick)
