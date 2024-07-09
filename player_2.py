import pygame

class player_2:
    def __init__(self,display_width, display_height) -> None:
        self.thick = 20
        self.long = 130
        self.speed = 3
        self.moving_up = False
        self.moving_down = False
        self.color = 255,255,255
        self.player = pygame.Rect(0,0,self.thick, self.long)
        self.player.midright = (display_width,display_height/2)
        
    
    #moves the player based on the input
    def player_2_move(self) -> None:
        if self.moving_up:
            self.player.y-=self.speed
        elif self.moving_down:
            self.player.y+=self.speed
        if self.player.y <= 1:
            self.moving_up = False 
        elif self.player.y >= 468:
            self.moving_down = False
    
    #draws the player
    def player_2_draw(self, screen) -> None:
       pygame.draw.rect(screen, self.color,(self.player))