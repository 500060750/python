import pygame
import sys
import random
import time

class snake():
    def _init_(self):
        self.position = [100,50]
        self.body = [[100,50],[90,50],[80,50]]
        self.direction = "RIGHT"
        self.changedirectionto = self.direction

    def changedirto(self,dir):
        if dir == "RIGHT" and not self.direction == "LEFT":
            self.direction= "RIGHT"
        if dir == "LEFT" and not self.direction == "RIGHT":
            self.direction= "LEFT"
        if dir == "UP" and not self.direction == "DOWN":
            self.direction= "UP"
        if dir == "DOWN" and not self.direction == "UP":
            self.direction= "DOWN"

    def move(self,foodpos):
        if self.direction == "RIGHT":
            self.position[0]  += 10
        if self.direction == "LEFT":
            self.position[0]  -= 10
        if self.direction == "UP":
            self.position[1]  -= 10
        if self.direction == "DOWN":
            self.position[1]  += 10

        self.body.insert(0,list(self.position))
        if self.position == foodpos:
            return 1
        else:
            self.body.pop()
            return 0

    def checkcollision(self):
        if self.position[0] >490 or self.position[0] <0:
            return 1
        elif self.position[1] > 490 or self.position[1] <0:
            return 1
        for bodypart in self.body[1:]:
            if self.position == bodypart:
                return 1

        return 0

    def getheadpos(self):
        return self.position
    def getbody(self):
        return self.body


class foodspawer():
    def _init_(self):
        self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
        self.isfoodonscr = True

    def spawnfood(self):
        if self.isfoodonscr == False:
            self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
            self.isfoodonscr = True
        return self.position

    def setfoodonscr(self,b):
        self.isfoodonscr = b

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("wow snake")
fps = pygame.time.Clock()

score = 0

snake = snake()
foodspawner = foodspawer()

def gameover():
        pygame.quit()
        sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
                gameover();
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.k_RIGHT:
                    snake.changedirto('RIGHT')
            if event.key == pygame.k_UP:
                    snake.changedirto('UP')
            if event.key == pygame.k_DOWN:
                    snake.changedirto('DOWN')
            if event.key == pygame.k_LEFT:
                    snake.changedirto('LEFT')

    foodpos = foodspawner.spawnfood()
    if(snake.move(foodpos)==1):
        score+=1
        foodspawner.setfoodonscr(False)

    window.fill(pygame.color(225,225,225))
    for pos in snake.getbody():
        pygame.draw.rect(window,pygame.color(0,225,0),pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(window,pygame.color(225,0,0),pygame.Rect(foodpos[0],foodpos[1],10,10))
    if(snake.checkcollision()==1):
        gameover()

    pygame.display.set_caption("wow snake | score: "+ str(score))
    pygame.display.flip()
    fps.tick(24)
        
                                   
        
                    
                    
    
        
            

    
