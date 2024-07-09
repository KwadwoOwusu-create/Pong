import sys
from player import player
from player_2 import player_2
from ball import ball
from pause import pause
from winner_screen import winner_screen
from main_menu import main_menu
import pygame
pygame.init()


#countdown for speeding up ball
countdown = 6000
countdown2 = pygame.time.get_ticks()
start_count = 3



#screen displays 
display_width = 800
display_height = 600
middle = (display_height/2 + 70, display_height/2)
middle2 = (display_height/2 + 130, display_height/2)
screen = pygame.display.set_mode((display_width , display_height))
title = "PONG"
pygame.display.set_caption(title)


#clock intialization 
clock = pygame.time.Clock()

#event timer 
event = pygame.USEREVENT + 1

##instances of players, ball, winnerscreen, mainmenu, pause
player = player(display_height)
player_2 = player_2(display_width,display_height)
ball = ball()
pause = pause(screen)
winner_screen = winner_screen(screen)
main_menu = main_menu(screen)


#point system
player_1_point = 0
player_2_point = 0
player_1_point_catch = player_1_point
player_2_point_catch = player_2_point


##display sytem for points
font_ttf = "04B_30__.ttf" 
font = pygame.font.Font(font_ttf, 20)
font1 = pygame.font.Font(font_ttf, 60)
p1_point_num = font.render(str(player_1_point), True, (255,255,255))
p2_point_num = font.render(str(player_2_point), True, (255,255,255))

#sound stuff


#countdown fucntion
def get_ready():
    global start_count
    global countdown2
    if  start_count > 0:
            screen.blit(font1.render("GET READY", True, (255,255,255)),((display_width/2 - 235, display_height/2 - 100)))
            screen.blit(font1.render(str(start_count), True, (255,255,255)),((display_width/2 - 30 , display_height/2 - 10)))
            count_timer = pygame.time.get_ticks()
            if (count_timer - countdown2) > 1000:
                start_count-=1
                countdown2 = count_timer 

#main_menu
main_menu.run()

#runs the game
while pause.checker:
    
    #if you click the x it quits the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        #keys pressed
        elif event.type == pygame.KEYDOWN:
            
            #if w is pressed player1 moves up, or if the up arrow is pressed player 2 moves up
            if event.key == pygame.K_w:
                player.moving_up = True
            elif event.key == pygame.K_UP:
                player_2.moving_up = True
            elif event.key == pygame.K_SPACE:
                pause.checker = False
                pause.run()
            elif event.key == pygame.K_SPACE and pause.checker == False:
                pause.checker = True 
                
                
             
            #if s is pressed player1 goes down or if down arrow is pressed player2 goes down 
            elif event.key == pygame.K_s:
                player.moving_down = True
            elif event.key == pygame.K_DOWN:
                player_2.moving_down = True
                
        #keys lifted    
        elif event.type == pygame.KEYUP:
            
            ##if w is no longer being pressed player1 doesnt move  or if up arrow is no longer being pressed player2 stops moving 
            if event.key == pygame.K_w:
                player.moving_up = False
            elif event.key == pygame.K_UP:
                player_2.moving_up = False
           
            ##if s is no longer being pressed player1 doesnt move  or if down arrow is no longer being pressed player2 stops moving 
    
            elif event.key == pygame.K_DOWN:
                player_2.moving_down = False 
            elif event.key == pygame.K_s:
                player.moving_down = False           
            
            
    
    
    
    
     
    #fills the screen with grey everyframe
    screen.fill(("grey12"))
    #countdown for the ball speed
    countdown -= 1
    #if anyone scores a predetermined amound then, reset everything to its default state and show the winnerscreen
    if player_1_point == winner_screen.point or player_2_point == winner_screen.point:
        #showws the winner
        winner_screen.run(player_1_point,player_2_point)
        #reset points
        player_1_point,player_2_point = 0,0
        player_1_point_catch,player_2_point_catch = 0,0
        #shows the new points
        p2_point_num = font.render(str(player_2_point), True, (255,255,255))
        p1_point_num = font.render(str(player_1_point), True, (255,255,255))
        
        #reset the ball
        ball.ball.x,ball.ball.y = ball.ball_center
        
        #reset player
        player.player.centery = display_height/2
        player_2.player.midright = display_width,display_height/2
        
        #reset ball speed
        ball.ball_reset()
        
    ##calls the players 
    player.draw(screen)
    player_2.player_2_draw(screen)
    
    #countdown before the game starts 
    if start_count == 0:
        
        #moving functions for the plaer, and ba;;
        player.move()
        player_2.player_2_move()
        ball.draw_ball(screen)
        ball.ball_move(player.player,player_2.player)
        
        
        ##intializes the points on screen default 0,0 in the middle 
        screen.blit(p1_point_num,middle),screen.blit(p2_point_num,middle2)
        
    #if no one score for 6 seconds then the ball speeds up by 10%
    if countdown <= 0 and (player_1_point_catch == player_1_point or player_2_point_catch == player_2_point):
        ball.ball_speed_up()
        countdown = 6000
        
    #if the ball hits the right side then player1 scores
    if ball.ball.right >= 800:
        player_1_point+=1
        player_1_point_catch+=1
        p1_point_num = font.render(str(player_1_point), True, (255,255,255))  
        countdown = 6000
        ball.ball_reset()
        start_count = 4
        get_ready()
        

            
    #if the ball hits the left side then player2 scores   
    if ball.ball.left <= 0:
        player_2_point+=1
        player_1_point_catch+=1
        p2_point_num = font.render(str(player_2_point), True, (255,255,255)) 
        countdown = 6000 
        ball.ball_reset()
        start_count = 4
        get_ready()
          
            
    
    
    #counter logic 
    get_ready()

        
        
    #updates the display according with the screen fill
    pygame.display.update()
    
    #runs the game at 300 fps 
    clock.tick(300)
    