import pygame, sys
import random
from pygame.math import Vector2

pygame.init()

FPS = 60
BLOCK_SIZE = 20
BLOCK_NUMBER = 20
SPEED = 200

clock = pygame.time.Clock()
screen = pygame.display.set_mode((BLOCK_SIZE*BLOCK_NUMBER, BLOCK_NUMBER*BLOCK_SIZE))
score_screen = pygame.Surface((BLOCK_SIZE*BLOCK_NUMBER, BLOCK_SIZE))

#text
font = pygame.font.SysFont("Verdana", 15)

class Snake():
    def __init__(self):
        
        self.body = [Vector2(10, 10), Vector2(9, 10), Vector2(8, 10)]
        self.direction = Vector2(1, 0) #вектор направление
        
    def draw_snake(self):
        for block in self.body:
            #body_rect = pygame.Rect(block.x * BLOCK_SIZE, 
                                    #block.y * BLOCK_SIZE, 
                                    #BLOCK_SIZE, BLOCK_SIZE)
            #pygame.draw.rect(screen, 
                             #(45, 125, 53), 
                             #body_rect, 5)
            if block == self.body[0]:
                col = (6, 7, 4)
            else:
                col = (45, 150, 53)
            pygame.draw.circle(surface=screen, color=col, center=(block.x * BLOCK_SIZE + BLOCK_SIZE/2, block.y * BLOCK_SIZE + BLOCK_SIZE/2), radius = BLOCK_SIZE/2, )
    
    def move_snake(self):
        body_copy = self.body[:-1] #удаляем последний блок и копируем , в конец добавляем новый вектор + направление
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy
    
    def add_block(self):
        self.body.insert(0, self.body[0] + self.direction)
        
class Fruit:
    def __init__(self):
        self.randomize_pos()
    def draw_fruit(self):
        
        fruit_rect = pygame.Rect(self.pos.x * BLOCK_SIZE, #что бы были ровно по сетке
                                 self.pos.y * BLOCK_SIZE, 
                                 BLOCK_SIZE, 
                                 BLOCK_SIZE)
        pygame.draw.rect(surface = screen
                         ,color = (250, 2, 31), 
                         rect = fruit_rect)
    def randomize_pos(self):
        self.x = random.randint(0, BLOCK_NUMBER - 1)
        self.y = random.randint(1, BLOCK_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)
        
class Big_fruit():
    def __init__(self):
        super().__init__(self)
        self.randomize_pos()
        self.is_time = False
        self.rect = pygame.Rect(self.pos.x * BLOCK_SIZE, #что бы были ровно по сетке
                                 self.pos.y * BLOCK_SIZE, 
                                 2*BLOCK_SIZE, 
                                 2*BLOCK_SIZE)
    def draw_fruit(self):
        
        pygame.draw.rect(surface = screen
                         ,color = (250, 2, 31), 
                         rect = self.rect)
    def randomize_pos(self):
        self.x = random.randint(0, BLOCK_NUMBER - 1)
        self.y = random.randint(1, BLOCK_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)
    
        
      
class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.score = 0
        self.level = 1
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        self.check_level()
    def draw_elements(self):

        if self.fruit.pos not in self.snake.body:
            self.fruit.draw_fruit()
        else:
            self.fruit.randomize_pos()
        self.snake.draw_snake()
        
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]: # if collision
            self.fruit.randomize_pos()
            self.snake.add_block()
            self.score += 1
        
            
    def check_fail(self):
        head_pos = self.snake.body[0]
        if not 0 <= head_pos.x < BLOCK_NUMBER or not 1 <= head_pos.y < BLOCK_NUMBER: # hitting the wall
            self.game_over()
        for body in self.snake.body[1:]:
            if head_pos == body:
                self.game_over()
    def check_level(self):
        if self.score/5 == self.level:
            self.level += 1
            global SPEED
            SPEED -= 10
            pygame.time.set_timer(SCREEN_UPDATE, SPEED)
   
            
    def game_over(self):
        pygame.quit()
        sys.exit()
            
        
main_game = Main()

SCREEN_UPDATE = pygame.USEREVENT  + 1
BIG_FRUIT = pygame.USEREVENT
pygame.time.set_timer(BIG_FRUIT, 10000)
pygame.time.set_timer(SCREEN_UPDATE, SPEED) # кастомное событье которая происходит раз в 150 мс

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()
            
        if event.type == SCREEN_UPDATE: #каждые 150 мс двигаем змею
            main_game.update()
        
        if event.type == BIG_FRUIT:
            pass
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction != (0, 1):
                    main_game.snake.direction = (0, -1) 
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction != (0, -1): 
                    main_game.snake.direction = (0, 1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction != (-1, 0):
                    main_game.snake.direction = (1, 0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction != (1, 0):
                    main_game.snake.direction = (-1, 0)
        
    screen.fill((247, 214, 92))
    score_screen.fill((100, 100, 250))
    
    scores = font.render("score:"+ str(main_game.score),True, (0, 0, 0))
    levels = font.render("level:" + str(main_game.level), True, (0, 0, 0))
    score_screen.blit(scores,(0, 0))
    score_screen.blit(levels,(200, 0))
    
    screen.blit(score_screen, (0, 0))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(FPS)