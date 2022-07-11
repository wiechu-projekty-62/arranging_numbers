import random
import pygame
import sys


class Timer:

    def __init__(self):
        self._start = 0

    def start(self):
        self._start = pygame.time.get_ticks()

    def current(self):
        return round((pygame.time.get_ticks() - self._start) / 60000, 2)


class Element:
    def __init__(self):
        self.val = 0

    def setval(self, val):
        self.val = val

    def delval(self):
        self.val = 0

    def getval(self):
        return self.val


class Board:
    def __init__(self):
        self.board = [[], [], [], []]
        self.prevboard = [[], [], [], []]
        for x in range(0, 4):
            for y in range(0, 4):
                self.board[y].append(Element())
                self.prevboard[y].append(Element())

    def randomizeelement(self):
        # Losowanie nowego elementu
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        while self.board[y][x].getval() != 0:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        self.board[y][x].setval(random.randint(1, 2) * 2)

    def prevsituation(self):
        for x in range(0, 4):
            for y in range(0, 4):
                self.board[y][x].setval(self.prevboard[y][x].getval())

    def right(self):
        self.copytable()
        for z in range(0, 3):
            for x in range(0, 3):
                for y in range(0, 4):
                    x = 2 - x
                    if self.board[y][x + 1].getval() == 0:
                        self.board[y][x + 1].setval(self.board[y][x].getval())
                        self.board[y][x].delval()
                    elif self.board[y][x].getval() == self.board[y][x + 1].getval():
                        self.board[y][x + 1].setval(self.board[y][x].getval() * 2)
                        self.board[y][x].delval()
        for x in range(0, 4):
            for y in range(0, 4):
                if self.prevboard[y][x].getval() != self.board[y][x].getval():
                    return True
        return False

    def left(self):
        self.copytable()
        for z in range(0, 3):
            for x in range(1, 4):
                for y in range(0, 4):
                    if self.board[y][x - 1].getval() == 0:
                        self.board[y][x - 1].setval(self.board[y][x].getval())
                        self.board[y][x].delval()
                    elif self.board[y][x].getval() == self.board[y][x - 1].getval():
                        self.board[y][x - 1].setval(self.board[y][x].getval() * 2)
                        self.board[y][x].delval()
        for x in range(0, 4):
            for y in range(0, 4):
                if self.prevboard[y][x].getval() != self.board[y][x].getval():
                    return True
        return False

    def up(self):
        self.copytable()
        for z in range(0, 3):
            for x in range(0, 4):
                for y in range(1, 4):
                    if self.board[y - 1][x].getval() == 0:
                        self.board[y - 1][x].setval(self.board[y][x].getval())
                        self.board[y][x].delval()
                    elif self.board[y][x].getval() == self.board[y - 1][x].getval():
                        self.board[y - 1][x].setval(self.board[y][x].getval() * 2)
                        self.board[y][x].delval()
        for x in range(0, 4):
            for y in range(0, 4):
                if self.prevboard[y][x].getval() != self.board[y][x].getval():
                    return True
        return False

    def down(self):
        self.copytable()
        for z in range(0, 3):
            for x in range(0, 4):
                for y in range(0, 3):
                    y = 2 - y
                    if self.board[y + 1][x].getval() == 0:
                        self.board[y + 1][x].setval(self.board[y][x].getval())
                        self.board[y][x].delval()
                    elif self.board[y][x].getval() == self.board[y + 1][x].getval():
                        self.board[y + 1][x].setval(self.board[y][x].getval() * 2)
                        self.board[y][x].delval()
        for x in range(0, 4):
            for y in range(0, 4):
                if self.prevboard[y][x].getval() != self.board[y][x].getval():
                    return True
        return False

    def gettable(self):
        return self.board

    def copytable(self):
        for x in range(0, 4):
            for y in range(0, 4):
                self.prevboard[y][x].setval(self.board[y][x].getval())


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([600, 600])
        pygame.display.set_caption("Gra a' la 2048")
        pygame.font.init()
        self.myfont60 = pygame.font.SysFont("Comic Sans MS", 60)
        self.myfont40 = pygame.font.SysFont("Comic Sans MS", 40)

    def draw(self, table):
        self.screen.fill((75, 75, 75))
        color1 = (185, 122, 87)
        pygame.draw.rect(self.screen, color1, pygame.Rect(0, 0, 150, 150), 4)
        pygame.draw.rect(self.screen, color1, pygame.Rect(150, 0, 150, 150), 4)
        pygame.draw.rect(self.screen, color1, pygame.Rect(300, 0, 150, 150), 4)
        pygame.draw.rect(self.screen, color1, pygame.Rect(450, 0, 150, 150), 4)
        pygame.draw.rect(self.screen, color1, pygame.Rect(0, 150, 150, 150), 4)
        pygame.draw.rect(self.screen, color1, pygame.Rect(150, 150, 150, 150), 4)
        pygame.draw.rect(self.screen, color1, pygame.Rect(300, 150, 150, 150), 4)
        pygame.draw.rect(self.screen, color1, pygame.Rect(450, 150, 150, 150), 4)
        pygame.draw.rect(self.screen, color1, pygame.Rect(0, 300, 150, 150), 4)
        pygame.draw.rect(self.screen, color1, pygame.Rect(150, 300, 150, 150), 4)
        pygame.draw.rect(self.screen, color1, pygame.Rect(300, 300, 150, 150), 4)
        pygame.draw.rect(self.screen, color1, pygame.Rect(450, 300, 150, 150), 4)
        pygame.draw.rect(self.screen, color1, pygame.Rect(0, 450, 150, 150), 4)
        pygame.draw.rect(self.screen, color1, pygame.Rect(150, 450, 150, 150), 4)
        pygame.draw.rect(self.screen, color1, pygame.Rect(300, 450, 150, 150), 4)
        pygame.draw.rect(self.screen, color1, pygame.Rect(450, 450, 150, 150), 4)
        # text = self.myfont40.render("      Gra a' la 2048", False, (255, 128, 0))
        # self.screen.blit(text, (0, 0))
        for x in range(0, 4):
            for y in range(0, 4):
                text = self.myfont60.render(str(table[y][x].getval()), False, (255, 255, 0))
                self.screen.blit(text, (x * 150 + 60, y * 150 + 30))
        pygame.display.flip()

    def run(self, board):
        board.randomizeelement()
        while True:
            self.draw(board.gettable())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if board.up():
                            board.randomizeelement()
                    elif event.key == pygame.K_DOWN:
                        if board.down():
                            board.randomizeelement()
                    elif event.key == pygame.K_LEFT:
                        if board.left():
                            board.randomizeelement()
                    elif event.key == pygame.K_RIGHT:
                        if board.right():
                            board.randomizeelement()
                    elif event.key == pygame.K_z:
                        board.prevsituation()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            pygame.time.wait(500)
            print(t.current(), "minutes passed")


board = Board()
game = Game()
t = Timer()
t.start()  # start timera
game.run(board)
