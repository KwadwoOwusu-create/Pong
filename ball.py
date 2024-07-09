import pygame, random

clock = pygame.time.Clock()

class ball:
    def __init__(self) -> None:
        
        self.size = 10
        self.ball_center = (800/2,600/2)
        self.x_speed = 1
        self.y_speed = 1
        self.color = 255, 255, 255
        self.ball = pygame.Rect(0,0,self.size,self.size)
        self.ball.centery = (self.ball_center)
        self.sound = pygame.mixer.Sound("sounds/airpods case closed 1.WAV")
        
        
    #draws the ball
    def draw_ball (self, screen) -> None:
        pygame.draw.rect(screen, self.color, (self.ball))
    
    #physics for the ball movement 
    def ball_move(self,player1,player2):
        self.ball.x+=self.x_speed
        self.ball.y+=self.y_speed
        if self.ball.bottom >= 600 or self.ball.top <=0 :
            self.sound.play()
            self.y_speed *=-1
        if self.ball.right >= 800 or self.ball.left <= 0 :
            self.sound.play()
            self.x_speed*=-1
        if self.ball.colliderect(player1) or self.ball.colliderect(player2):
            self.sound.play()
            self.x_speed *= -1
    
                    
    #speeds up ball
    def ball_speed_up(self):
        self.x_speed*= 1.9
        self.y_speed*= 1.9
        
    #resets the ball speed 
    def ball_reset(self):
        self.ball.x, self.ball.y = self.ball_center
        self.x_speed = 1
        self.y_speed = 1
        
        
       
            
   
        