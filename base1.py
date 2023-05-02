import pygame,sys

class car(pygame.sprite.Sprite):
    def __init__(self,x,y,):
        super().__init__()
        #including images file in the simulation window
        # self.sprites=[]
        # self.sprites.append(pygame.image.load('car.png'))
        # self.sprites.append(pygame.image.load('car.png'))
        # self.image =pygame.Surface([width,height])
        # self.image.fill(color)
        self.image = pygame.image.load('car.png')
        self.rect = self.image.get_rect()
        self.rect.x=300
        self.rect.y=600

pygame.init()
clock = pygame.time.Clock()


screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load("road.png")  
backgrass = pygame.image.load("grass.png")  
strlight = pygame.image.load("newstr.png")
strcar = pygame.image.load("car.png")
strtruck = pygame.image.load("truck.png")
strbike = pygame.image.load("bike.png")
strbus = pygame.image.load("bus.png")

#backlight = pygame.image.load("newstreetoff.png")  

car = car(300,600)
car_group = pygame.sprite.Group()
car_group.add(car)  

velocity = 1
while True:
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
    
    car.rect.x += velocity

    # screen.fill((255, 255, 255))
   
    
    
  
    screen.blit(background,(100,300)) 
    screen.blit(background,(400,300))  #for rendering background display
    screen.blit(background,(795,300))  #for rendering background display
    screen.blit(background,(1190,300))  #for rendering background display
    screen.blit(background,(1300,300))
    screen.blit(backgrass,(253,630))  #for rendering background display
    screen.blit(backgrass,(600,630))  #for rendering background display
    screen.blit(backgrass,(1000,630))  #for rendering background display
    screen.blit(backgrass,(1300,630))  #for rendering background display
    screen.blit(backgrass,(1300,000.1))  #for rendering background display
    screen.blit(backgrass,(1000,000.1))  #for rendering background display
    screen.blit(backgrass,(600,000.1))  #for rendering background display
    screen.blit(backgrass,(253,000.1))  #for rendering background display
    screen.blit(strlight,(300,300))  #for rendering background display
    screen.blit(strlight,(700,300))  #for rendering background display
    screen.blit(strlight,(1100,300))  #for rendering background display
    screen.blit(strlight,(1500,300))  #for rendering background display
    screen.blit(strcar,(300,600))  #for rendering background display
    # screen.blit(strtruck,(400,530))  #for rendering background display
    # screen.blit(strbus,(500,540))  #for rendering background display
    # screen.blit(strbike,(600,450))  #for rendering background display
    # screen.blit(strcar,(700,400))  #for rendering background display
    # screen.blit(strcar,(800,850))  #for rendering background display
   
    pygame.display.flip()
        
        




    car_group.draw(screen)
    clock.tick(60)      
