import pygame
from .constant import  RED,WHITE,BORDER,SQUARE_SIZE,GREY,CROWN
class Piece:
    PADDING = 15
    OUTLINE = 2
    def __init__(self,row,col,color):
        self.row=row
        self.col=col
        self.color=color
        self.king=False
        self.direction= -1 if self.color==RED else 1
        self.x=0
        self.y=0
        self.calculate_position()
    def calculate_position(self):
        self.x= SQUARE_SIZE *self.col + SQUARE_SIZE//2
        self.y= SQUARE_SIZE *self.row + SQUARE_SIZE//2
    def create_king():
        self.king=True
    def move(self,row,col):
        self.row=row
        self.col=col
        self.calculate_position()

    def draw(self,win ):
        radius=SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x,self.y), radius+self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x,self.y), radius) 
        if self.king:
            win.blit(CROWN,(self.x-CROWN.get_width()//2,self.y-CROWN.get_height()))
    def __repr__(self):
        return str(self.color)