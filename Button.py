import pygame,sys

class Buttons:
    def __init__(self,screen) -> None:
        self.screen = screen
        self.button_rect = pygame.Rect(200, (700//2), 400, 50)
        self.font = pygame.font.Font("04B_30__.ttf", 40)
        self.main_play_again = None
        self.shaddow_play_again = None
        
    
    #draws text    
    def draw_text(self, text, font, text_col, cords):
        img = font.render(text, True, text_col)
        self.screen.blit(img,(cords))
    
    #creates the play again and adds button 
    def draw(self):
        pygame.draw.rect(self.screen, "grey12", self.button_rect)
        self.main_play_again = self.draw_text("PLAY AGAIN", self.font, (0,0,0), (220, 700//2) )
        self.shaddow_play_again = self.draw_text("PLAY AGAIN", self.font, (255,255,255), (210, 680//2) )
        
    #when a button is clicked set whatever is needed to true     
    def clicked(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                return True
        return False
        