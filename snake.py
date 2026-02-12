import pygame
import time
import random
#speed
snake_speed=15
#window
window_x=720
window_y=480
#colours
black=pygame.Color(0,0,0)
white=pygame.Color(255,255,255)
red=pygame.Color(255,0,0)
green=pygame.Color(0,255,0)
blue=pygame.Color(0,0,255)
#initialise pygame
pygame.init()
#game window
pygame.display.set_caption('Snake Game')
game_window=pygame.display.set_mode((window_x,window_y))
fps=pygame.time.Clock()
#position
snake_postition=[100,50]
snake_body=[[100,50],[90,50],[80,50],[70,50]]
#fruit
fruit_postion=[random.randrange(1,(window_x//10))*10, random.randrange(1,(window_y//10))*10]
fruit_spawn=True
direction='RIGHT'
change_to=direction
#score
score=0
def show_score(choice,colour,font,size):
    score_font=pygame.font.SysFont(font,size)
    score_surface=score_font.render('Score : '+str(score),True,colour)
    score_rect=score_surface.get_rect()
    game_window.blit(score_surface,score_rect)
#game_over function
def game_over():
    my_font=pygame.font.SysFont('sans-serif',50)
    game_over_surface=my_font.render('your score is:'+str(score),True,red)
    game_over_rect=game_over_surface.get_rect()
    game_over_rect.midtop=(window_x/2,window_y/4)
    game_window.blit(game_over_surface,game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()
#controls
while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                change_to='UP'
            if event.key==pygame.K_s:
                change_to='DOWN'
            if event.key==pygame.K_a:
                change_to='LEFT'
            if event.key==pygame.K_d:
                change_to='RIGHT'
    #validation of direction
    if change_to=='UP' and direction!='DOWN':
        direction='UP'
    if change_to=='DOWN' and direction!='UP':
        direction='DOWN'
    if change_to=='LEFT' and direction!='RIGHT':
        direction='LEFT'
    if change_to=='RIGHT' and direction!='LEFT':
        direction='RIGHT'
    #moving the snake
    if direction=='UP':
        snake_postition[1]-=10
    if direction=='DOWN':
        snake_postition[1]+=10
    if direction=='LEFT':
        snake_postition[0]-=10
    if direction=='RIGHT':
        snake_postition[0]+=10
    #snake body growing mechanism
    snake_body.insert(0,list(snake_postition))
    if snake_postition[0]==fruit_postion[0] and snake_postition[1]==fruit_postion[1]:
        score+=10
        fruit_spawn=False
    else:
        snake_body.pop()
    if not fruit_spawn:
        fruit_postion=[random.randrange(1,(window_x//10))*10, random.randrange(1,(window_y//10))*10]
        fruit_spawn=True
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window,green,pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(game_window,white,pygame.Rect(fruit_postion[0],fruit_postion[1],10,10))
    #game over conditions
    if snake_postition[0]<0 or snake_postition[0]>window_x-10:
        game_over()
    if snake_postition[1]<0 or snake_postition[1]>window_y-10:
        game_over()
    for block in snake_body[1:]:
        if snake_postition[0]==block[0] and snake_postition[1]==block[1]:
            game_over()
    show_score(1,white,'consolas',20)
    pygame.display.update()
    fps.tick(snake_speed)