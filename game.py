class Board:
    def __init__(self):
        self.board = [[-1, -1, -1],[-1, -1, -1],[-1, -1, -1]]
        self.turn = 1

    def checkWinner(self):
        if [1,1,1] in self.winningCombinations():
            return 1
        elif [0,0,0] in self.winningCombinations():
            return 0
        else:
            if self.isFull():
                return 2
            return -1
    def place(self, x, y):


        if self.board[y][x] == -1:
            self.board[y][x] = self.turn
            if self.turn:
                self.turn = 0
            elif not self.turn:
                self.turn = 1
        
        if self.checkWinner() != -1:
            
            return self.checkWinner()

    def isFull(self):
        for i in self.board:
            if -1 in i:
                return False

        return True
        
    def winningCombinations(self):
        winningCombos = [
        # Horizontal
        [self.board[0][0], self.board[0][1], self.board[0][2]],
        [self.board[1][0], self.board[1][1], self.board[1][2]],
        [self.board[2][0], self.board[2][1], self.board[2][2]],
        # Vertical
        [self.board[0][0], self.board[1][0], self.board[2][0]],
        [self.board[0][1], self.board[1][1], self.board[2][1]],
        [self.board[0][2], self.board[1][2], self.board[2][2]],
        # Diagonals
        [self.board[0][0], self.board[1][1], self.board[2][2]],
        [self.board[0][2], self.board[1][1], self.board[2][0]]
        ]
        return winningCombos
        
class Game:
    def __init__(self):
        self.player = {0 : 'O', 1 : 'X'}
        self.board = Board()

    def drawBoard(self, screen):
        pygame.draw.rect(screen,(0,0,0),[150,150,100,100], 2)
        pygame.draw.rect(screen,(0,0,0),[150,150,200,100], 2)
        pygame.draw.rect(screen,(0,0,0),[150,150,300,100], 2)
        pygame.draw.rect(screen,(0,0,0),[150,150,100,200], 2)
        pygame.draw.rect(screen,(0,0,0),[150,150,200,200], 2)
        pygame.draw.rect(screen,(0,0,0),[150,150,300,200], 2)
        pygame.draw.rect(screen,(0,0,0),[150,150,100,300], 2)
        pygame.draw.rect(screen,(0,0,0),[150,150,200,300], 2)
        pygame.draw.rect(screen,(0,0,0),[150,150,300,300], 2)


        font = pygame.font.Font(None, 50)
        text = font.render(f"Turn: {self.player[self.board.turn]}", True, (0,0,0))
        screen.blit(text, (150,100))
        for i in range(len(self.board.board)):
            for j in range(len(self.board.board[i])):
                start_x = j*100+170
                start_y = i*100+170
                if self.board.board[i][j] == 1:
                    pygame.draw.line(screen, (255,0,0), (start_x+60,start_y+60), (start_x, start_y),7)
                    pygame.draw.line(screen, (255,0,0), (start_x,start_y+60), (start_x+60, start_y),7)
                elif self.board.board[i][j] == 0:
                    pygame.draw.circle(screen, (0,0,255), (start_x+30,start_y+30), 35,5)

            


import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Tic-Tac-Toe")
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True


game = Game()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                
                choice = tuple((a-b)//100 for a,b in zip(mouse_pos,(150,150)))
                if not (choice[0] > 2 or choice[0] < 0 or choice[1] > 2 or choice[1] < 0):
                    place = game.board.place(choice[0],choice[1])
                    print(place)
                    if place in [0,1,2]:
                        game.board.board = [[-1, -1, -1],[-1, -1, -1],[-1, -1, -1]]
                    
    screen.fill((255,255,255))

    game.drawBoard(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

