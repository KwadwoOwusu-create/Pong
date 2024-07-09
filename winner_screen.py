import pygame,sys
from Button import Buttons


class winner_screen:
    def __init__(self,screen) -> None:
        self.font = pygame.font.Font("04B_30__.ttf", 60)
        self.screen = screen
        self.background = pygame.image.load("blur.png").convert()
        self.button = Buttons(screen)
        self.point = 5
        self.sound = pygame.mixer.Sound("sounds/Retro Blop StereoUP 09.WAV")
        self.sound2 = pygame.mixer.Sound("sounds/Retro Event UI 01.WAV")
        self.playing = True 
        

    
    #function for drawing the texts on screen 
    def draw_text(self, text, font, text_col, cords, screen):
        img = font.render(text, True, text_col)
        screen.blit(img,(cords))
        
    #if theres a winner it shows who and a play again button to click
    def run(self,p1,p2):
        while True:
            self.screen.blit(self.background,(0,0))
            if self.playing == True:
                self.sound2.play(0)
                self.playing = False
            
            #if player 1 wins then show that 
            if p1 == self.point:
                winner_screen.draw_text(self,"Player1 Wins!", self.font, (0,0,0), (((220//2)), (520//2)), self.screen)
                winner_screen.draw_text(self,"Player1 Wins!", self.font, (255,255,255), (((200//2)), (500//2)), self.screen)
                self.button.draw()

            #if player 2 wins then show that
            elif p2 == self.point:
                winner_screen.draw_text(self,"Player2 Wins!", self.font, (0,0,0), (((220//2)), (520//2)), self.screen)
                winner_screen.draw_text(self,"Player2 Wins!", self.font, (255,255,255), (((200//2)), (500//2)), self.screen)
                self.button.draw()
                

                
            #if the player clicks on play again then it restarts 
            for event in pygame.event.get():
                if self.button.clicked(event) == True:
                    self.sound.play()
                    return
                    
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            
        
    
    