import pygame, sys

class main_menu:
    def __init__(self,screen) -> None:
        self.font_ttf = "04B_30__.ttf"
        self.winner = True
        self.font = pygame.font.Font(self.font_ttf, 40)
        self.mainfont = pygame.font.Font(self.font_ttf, 50)
        self.pongfont =  pygame.font.Font(self.font_ttf, 90)
        self.screen = screen
        self.background = "grey12"
        self.menu = True
        #button for quit
        self.quit = pygame.Rect(310, 700//2, 140, 50)
        #button for multiplayer
        self.multip = pygame.Rect(179, 500//2, 405, 50)
        #button for arcade
        self.arcade = pygame.Rect(179,600/2, 405, 50)
        self.sound = pygame.mixer.Sound("sounds/Retro Blop StereoUP 09.WAV")
        

        
    #draws the text on screen
    def draw_text(self, text, font, text_col, cords, screen):
        img = font.render(text, True, text_col)
        screen.blit(img,(cords))
        
    
    #draws Pong and mainmenu on top 
    def draw_main(self):
        #self.draw_text("POMG", self.pongfont, (0,0,0),       (240, 80//2),self.screen ) #shadow
        self.draw_text("POMG", self.pongfont, (255,255,255),     (230, 60//2), self.screen )
        #self.draw_text("Main Menu", self.mainfont, (0,0,0),       (228, 255//2),self.screen ) #shadow
        #self.draw_text("Main Menu", self.mainfont, (255,255,255), (218, 235//2), self.screen )
        
    #draws multiplayer and button
    def draw_play(self):
        pygame.draw.rect(self.screen, self.background, self.multip)
        #self.draw_text("Multi Player", self.font, "black", (195, 420//2),self.screen ) #shadow
        self.draw_text("Play", self.font, (255,255,255), (320, 500//2), self.screen )
     
    #draws arcade mode and button   
    # def draw_arcade(self):
    #     pygame.draw.rect(self.screen, self.background, self.arcade)
    #     #self.draw_text("Arcade Mode", self.font, "black", (205, 620//2),self.screen ) #shadow
    #     self.draw_text("Arcade Mode", self.font, (255,255,255), (205, 600//2), self.screen )
    
    #draws quit and button
    def draw_quit(self):
        pygame.draw.rect(self.screen, self.background, self.quit)
       # self.draw_text("Quit", self.font, "black", (330, 720//2),self.screen ) #shadow
        self.draw_text("Quit", self.font, (255,255,255), (330, 600//2), self.screen )

    # runs the main menu
    def run(self):
        while self.menu:
            
            self.screen.fill("grey12")
            
            #runs all the draw functions
            main_menu.draw_main(self)
            main_menu.draw_play(self)
            #main_menu.draw_arcade(self)
            main_menu.draw_quit(self)
            
            #clicks
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
                #if mouse clicks quit it quits
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.quit.collidepoint(event.pos):
                        
                        pygame.quit
                        sys.exit()
                    #if mouse clicks multiplayer then menu equals falls and starts multiplayer game
                    elif self.multip.collidepoint(event.pos):
                        self.sound.play()
                        self.menu = False
                    
                    
            pygame.display.update()