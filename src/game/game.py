import pygame
import os
from time import sleep, time

from game.piece import Piece
from game.board import Board
from services.game_service import game_service


class Game():
    """acts as an index for handling events in game
    """
    def __init__(self, board, screensize):
        """sets up game

        Args:
            board: contains info on board size and asset coordinates
            screensize: screensize
        """
        self._board = board
        self._screensize = screensize
        self._piecesize = self._screensize[0] // self._board.get_size(
        )[1], self._screensize[1] // self._board.get_size()[0]
        self._init = True
        self._load_images()

    def start(self):
        """runs pygame window
        """
        pygame.init()
        pygame.display.set_caption('Minesweeper')
        self._font = pygame.font.SysFont("Arial", 20)
        self._screen = pygame.display.set_mode(self._screensize)
        self.run()

    def end(self):
        """closes pygame window
        """
        pygame.quit()

    def event_handler(self):
        """gets user input

        Returns:
            pygame event: action imposed by player
        """
        return pygame.event.get()

    def run(self, testevent=None, testpos=None):
        """contains game loop

        Args:
            testevent (optional): event used for testing purposes
            testpos (optional): mouse coordinates used for testing purposes.
        """
        self._start_time = time()
        self._running = True
        while self._running:
            if testevent != None:
                position = testpos
                self._screen = False
                rightclick = False
                self.handle_click_game(position, rightclick)
            else:
                for event in self.event_handler():
                    if event.type == pygame.QUIT:
                        score = 0
                        status = "lost"
                        game_service.register_game_data(score, status)
                        self._running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        position = pygame.mouse.get_pos()
                        rightclick = pygame.mouse.get_pressed()[2]
                        self.handle_click_game(position, rightclick)
            self._draw()
            if self._screen != False:
                pygame.display.flip()
            if self._board.get_won():
                self.won_info()
            if self._board.get_lost():
                self.lost_info()
        self.end()

    def _draw(self):
        """updates the pygame view during the course of the game
        """
        top_left = (0, 0)
        for row in range(self._board.get_size()[0]):
            for col in range(self._board.get_size()[1]):
                piece = self._board._get_piece((row, col))
                image = self._get_image(piece)
                if self._screen != False:
                    self._screen.blit(image, top_left)
                top_left = top_left[0] + self._piecesize[0], top_left[1]
            top_left = 0, top_left[1] + self._piecesize[1]

    def _load_images(self):
        """retrieves images used in the game
        """
        self._images = {}
        dirname = os.path.dirname(__file__)
        for file in os.listdir(f"{dirname}/assets"):
            if not file.endswith(".png"):
                continue
            image = pygame.image.load(f"{dirname}/assets/" + file)
            image = pygame.transform.scale(image, self._piecesize)
            self._images[file.split(".")[0]] = image

    def _get_image(self, piece):
        """fetches correct image in accordance with board coordinates

        Args:
            piece: image assigned to click location

        Returns:
            dict: image file that corresponds with key name
        """
        string = None
        if piece.get_clicked():
            string = "bomb" if piece.get_has_bomb() else str(piece.get_num_around())
        else:
            string = "flag" if piece.get_flagged() else "empty_unclicked"
        return self._images[string]

    def handle_click_game(self, position, rightclick):
        """sets up events that result from clicking game board

        Args:
            position: click coordinates
            rightclick: boolean value of whether right-side click was made
        """
        if self._init == False:
            if self._board.get_lost():
                return
            index = position[1] // self._piecesize[1], position[0] // self._piecesize[0]
            piece = self._board._get_piece(index)
            self._board.handle_click_board(piece, rightclick)
        elif self._init == True:
            index = position[1] // self._piecesize[1], position[0] // self._piecesize[0]
            self._init = False
            self._board.set_bombs(index)
            piece = self._board._get_piece(index)
            self._board.handle_click_board(piece, rightclick)

    def won_info(self):
        """handles events for when player wins game
        """
        sleep(2)
        end_time = time()
        score = round(end_time - self._start_time, 2)
        status = "won"
        game_service.register_game_data(score, status)
        if self._screen != False:
            self._wontext1 = self._font.render(("Congratulations!"), True, (0, 0, 0))
            self._wontext2 = self._font.render((f"you beat the game in"), True, (0, 0, 0))
            self._wontext3 = self._font.render((f"{score} seconds!"), True, (0, 0, 0))
            self._screen.fill((255, 255, 255))
            self._screen.blit(self._wontext1, (self._screensize[0] // 2 - 80, self._screensize[1] // 2 - 30))
            self._screen.blit(self._wontext2, (self._screensize[0] // 2 - 100, self._screensize[1] // 2))
            self._screen.blit(self._wontext3, (self._screensize[0] // 2 - 80, self._screensize[1] // 2 + 30))
            pygame.display.flip()
            sleep(3)
        self._running = False

    def lost_info(self):
        """handles events for when player loses game
        """
        sleep(2)
        score = 0
        status = "lost"
        game_service.register_game_data(score, status)
        self._losttext = self._font.render(("Better luck next time!"), True, (0, 0, 0))
        self._screen.fill((255, 255, 255))
        self._screen.blit(self._losttext, (self._screensize[0] // 2 - 100, self._screensize[1] // 2))
        pygame.display.flip()
        sleep(3)
        self._running = False